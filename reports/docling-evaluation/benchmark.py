"""Offline PDF conversion benchmark for the three regression documents."""

import argparse
import hashlib
from importlib.metadata import version
import json
import os
from pathlib import Path
import platform
import sys
from time import perf_counter

import psutil


ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / ".conversion-env"
SAMPLES = {
    "feitian-developer": "cn/OpenTrek/飞天助理/*开发指南 20251205.pdf",
    "feitian-overview": "cn/OpenTrek/飞天助理/*产品简介 20251205.pdf",
    "ahm-user": "cn/中间件/应用运维平台/*用户指南 20250529.pdf",
}


def dump(path, value):
    # The lightweight reader returns iterable PyMuPDF rectangles in page metadata.
    path.write_text(json.dumps(value, default=list, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def setup(engine, threads, models):
    if engine == "current":
        from pdfmd_document import convert

        def run(pdf, out):
            return convert(pdf, out / "document.md", "cn"), None

        return run, {"pymupdf": version("pymupdf")}

    if engine == "pymupdf4llm":
        import pymupdf
        import pymupdf4llm

        def run(pdf, out):
            assets = out / "assets"
            assets.mkdir()
            with pymupdf.open(pdf) as source:
                pages = pymupdf4llm.to_markdown(
                    source, page_chunks=True, write_images=True, image_path=str(assets),
                    image_size_limit=0.0, dpi=144, force_text=True, show_progress=False,
                )
            # Make image URLs portable while preserving the engine's placement.
            for page in pages:
                for base in {str(out) + os.sep, out.as_posix() + "/"}:
                    page["text"] = page["text"].replace(base, "").replace("](assets\\", "](assets/")
            (out / "document.md").write_text("\n\n".join(page["text"] for page in pages), encoding="utf-8")
            return {"pages": len(pages)}, lambda: dump(out / "pages.json", pages)

        return run, {pkg: version(pkg) for pkg in ("pymupdf", "pymupdf4llm")}

    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
    os.environ["DO_NOT_TRACK"] = "1"
    from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode, TableStructureOptions
    from docling.document_converter import DocumentConverter, PdfFormatOption
    from docling_core.types.doc import ImageRefMode

    options = PdfPipelineOptions(
        artifacts_path=models,
        do_ocr=False,
        do_table_structure=True,
        table_structure_options=TableStructureOptions(mode=TableFormerMode.ACCURATE, do_cell_matching=True),
        generate_picture_images=True,
        images_scale=2.0,
        accelerator_options=AcceleratorOptions(device=AcceleratorDevice.CPU, num_threads=threads),
        enable_remote_services=False,
    )
    converter = DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=options)})
    converter.initialize_pipeline(InputFormat.PDF)

    def run(pdf, out):
        result = converter.convert(pdf)
        doc = result.document
        doc.save_as_markdown(out / "document.md", image_mode=ImageRefMode.REFERENCED)
        return {
            "pages": doc.num_pages(),
            "status": result.status.value,
            "errors": [str(error) for error in result.errors],
        }, lambda: doc.save_as_json(out / "document.json", image_mode=ImageRefMode.PLACEHOLDER)

    return run, {pkg: version(pkg) for pkg in ("docling-slim", "docling-core", "docling-parse", "torch", "transformers")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("engine", choices=("current", "pymupdf4llm", "docling"))
    parser.add_argument("--output", type=Path, required=True, help="new run directory")
    parser.add_argument("--models", type=Path, default=CACHE / "bench-docling-models")
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--repeat", type=int, default=1)
    parser.add_argument("--sample", action="append", choices=SAMPLES)
    args = parser.parse_args()
    if args.repeat < 1 or args.threads < 1:
        parser.error("--threads and --repeat must be positive")

    args.output = args.output.resolve()
    args.output.mkdir(parents=True, exist_ok=False)
    sys.path[:0] = [str(ROOT / "scripts"), str(CACHE)]
    if args.engine in ("docling", "pymupdf4llm"):
        env_dir = CACHE / ("bench-docling-py" if args.engine == "docling" else "bench-4llm-py")
        # Keep PyMuPDF 1.26.5 on both the production and the lightweight paths.
        sys.path.insert(0 if args.engine == "docling" else 2, str(env_dir))
    os.environ["OMP_NUM_THREADS"] = str(args.threads)
    process = psutil.Process()
    start = perf_counter()
    convert, versions = setup(args.engine, args.threads, args.models.resolve())
    setup_seconds = perf_counter() - start
    print(args.engine, versions, f"setup={setup_seconds:.3f}s", flush=True)
    records = []
    for index in range(1, args.repeat + 1):
        for name in args.sample or SAMPLES:
            pdf, = (ROOT / "docs").glob(SAMPLES[name])
            out = args.output / f"run-{index}" / name
            out.mkdir(parents=True)
            start = perf_counter()
            result, save_structure = convert(pdf, out)
            elapsed = perf_counter() - start
            memory = process.memory_info()
            with pdf.open("rb") as source:
                sha256 = hashlib.file_digest(source, "sha256").hexdigest()
            records.append({
                "sample": name, "repeat": index, "sha256": sha256, "seconds": elapsed,
                "peak_rss_mib": getattr(memory, "peak_wset", memory.rss) / (1024 * 1024),
                "result": result,
            })
            print(f"{name} run {index}: {elapsed:.3f}s", flush=True)
            if save_structure:
                save_structure()
                del save_structure
            dump(args.output / "metrics.json", {
                "engine": args.engine, "versions": versions, "python": platform.python_version(),
                "platform": platform.platform(), "logical_cpus": os.cpu_count(),
                "threads": args.threads, "setup_seconds": setup_seconds, "runs": records,
            })


if __name__ == "__main__":
    main()
