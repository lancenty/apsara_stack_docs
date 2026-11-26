"""Convert one source PDF in reading order, keeping at most one section of layout in memory."""

import hashlib
import re
from pathlib import Path

import pymupdf

from doc_identity import resolve_identity
from pdfmd_body import decorate_events, render_body
from pdfmd_media import atomic_write, extract_figures, fallback_figure, in_box
from pdfmd_structure import body_box, build_structure, heading_events, normalize_text
from pdfmd_tables import attach_image, merge_tables, tables_on_page


ASSET = re.compile(
    r'(?:!\[[^\]\n]*\]\(|<img\b[^>]*?\bsrc=["\'])((?:assets|[a-z0-9][a-z0-9._-]*\.assets)/[a-f0-9]{32}\.[a-z0-9]+)'
)
_QT_TILTED_MATRIX = re.compile(
    rb"(?m)(?:^[ \t]*|[A-Za-z*][ \t]+)[-+.\d]+[ \t]+(?!0[ \t]+0[ \t])[-+.\d]+[ \t]+[-+.\d]+"
    rb"(?:[ \t]+[-+.\d]+){3}[ \t]+(?:Tm|cm)\b"
)
_GLYPH_QUAD = re.compile(r'<char quad="([^"]+)" x="([^"]+)" y="([^"]+)"')


def _glyph_position(x, y):
    return round(float(x) * 10), round(float(y) * 10)


def extract_blocks(page, flags):
    """Preserve synthetic italic runs, including a style change inside a font span."""
    clip = pymupdf.INFINITE_RECT()
    qt = "wkhtml" in ((page.parent.metadata or {}).get("creator") or "").lower()
    if qt and not _QT_TILTED_MATRIX.search(page.read_contents()) and not page.get_xobjects():
        return page.get_text("dict", flags=flags, clip=clip)["blocks"]
    textpage = page.get_textpage(flags=flags, clip=clip)
    slanted = set()
    for quad, x, y in _GLYPH_QUAD.findall(textpage.extractXML()):
        ulx, uly, urx, ury, llx, lly, _, _ = map(float, quad.split())
        dx, dy = urx-ulx, ury-uly
        vx, vy = llx-ulx, lly-uly
        # Rotation preserves the right angle between the top and side of a glyph.
        # Shearing a regular font to synthesize italic changes that angle.
        cross = abs(dx*vy - dy*vx)
        if cross > .001 and .08 * cross < abs(dx*vx + dy*vy) < .85 * cross:
            slanted.add(_glyph_position(x, y))
    if not slanted:
        return textpage.extractDICT()["blocks"]
    blocks = textpage.extractRAWDICT()["blocks"]
    for block in blocks:
        for line in block.get("lines", []):
            runs = []
            for span in line["spans"]:
                chars = span.pop("chars")
                start = 0
                while start < len(chars):
                    italic = _glyph_position(*chars[start]["origin"]) in slanted
                    end = start + 1
                    while end < len(chars) and (_glyph_position(*chars[end]["origin"]) in slanted) == italic:
                        end += 1
                    glyphs = chars[start:end]
                    xs, ys, rights, bottoms = zip(*(c["bbox"] for c in glyphs))
                    runs.append(dict(span, text="".join(c["c"] for c in glyphs), origin=glyphs[0]["origin"],
                                     bbox=(min(xs), min(ys), max(rights), max(bottoms)),
                                     flags=span["flags"] | (2 if italic else 0)))
                    start = end
            line["spans"] = runs
    return blocks


def md_label(s):
    return s.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def front_matter(structure, language):
    cover = "  \n".join(md_label(s) for s in structure["cover"])
    toc = []
    for ent in structure["entries"]:
        indent = "    " * (ent["level"] - 1)
        toc.append(f'{indent}- [{md_label(ent["title"])}](#{ent["anchor"]})')
    return cover + "\n\n**" + ("目录" if language == "cn" else "Table of Contents") + "**\n\n" + "\n".join(toc)


def _edge_text(page, lines, body):
    # At a Qt page break MuPDF may emit only descenders from a clipped line.
    # Use the underlying text drawing operator to recover these fragments.
    candidates = [e for e in lines if (e["bbox"][1] < body[1] + 13 or e["bbox"][3] > body[3] - 13)
                  and len(e["text"].strip()) < 7 and len(e["spans"]) == 1]
    if not candidates:
        return
    traces = page.get_texttrace()
    for trace in traces:
        chars = trace["chars"]
        if not chars or trace["dir"][0] < .99:
            continue
        baseline = chars[0][2][1]
        if body[1]+21 < baseline < body[3]-19 or any(abs(c[2][1] - baseline) > 1 for c in chars):
            continue
        matched = [e for e in candidates if e in lines and
                   e["spans"][0]["font"] == trace["font"] and
                   abs(e["spans"][0]["origin"][1]-baseline) < .15 and
                   e["bbox"][0] >= trace["bbox"][0] - 1 and e["bbox"][2] <= trace["bbox"][2] + 1]
        if not matched:
            continue
        full = "".join(chr(c[0]) for c in chars)
        if len(full.strip()) <= sum(len(e["text"].strip()) for e in matched):
            continue
        first = matched[0]
        x0, _, x1, _ = trace["bbox"]
        bounds = (x0, first["bbox"][1], x1, first["bbox"][3])
        first.update(bbox=bounds, text=full, edge_repaired=True)
        first["spans"][0].update(text=full, bbox=bounds, origin=(x0,baseline))
        for e in matched[1:]:
            lines.remove(e)


def _lines(page, blocks, body):
    result = []
    for block in blocks:
        for line in block.get("lines", []):
            box = line["bbox"]
            if not body[1] <= (box[1]+box[3])/2 <= body[3] or not line["spans"]:
                continue
            result.append(dict(kind="line", text="".join(s["text"] for s in line["spans"]),
                               page=page.number+1, bbox=box, spans=line["spans"], block=block["number"]))
    return result


def _table_contains(table, line):
    x0,y0,x1,y1 = line["bbox"]
    a,b,c,d = table["bbox"]
    return a-3 <= (x0+x1)/2 <= c+3 and b <= (y0+y1)/2 <= d


def page_events(page, structure, directory, asset_prefix="assets"):
    box = body_box(page, structure)
    flags = pymupdf.TEXTFLAGS_DICT
    if structure["_qt"]:
        flags |= pymupdf.TEXT_INHIBIT_SPACES
    blocks = extract_blocks(page, flags)
    lines = _lines(page, blocks, box)
    if structure["_qt"]:
        _edge_text(page, lines, box)
    headings, claimed = heading_events(page, lines, structure)
    drawings = page.get_drawings()
    tables = tables_on_page(page, lines, drawings, box)
    images, covered = extract_figures(
        page, blocks, lines, drawings, tables, box, directory, structure, asset_prefix=asset_prefix
    )
    out = [*headings, *tables]
    out.extend(im for im in images if not any(attach_image(t, im) for t in tables if in_box(im["bbox"], t["bbox"], 3)))
    for i,line in enumerate(lines):
        if i in claimed or i in covered or any(_table_contains(t, line) for t in tables):
            continue
        out.append(line)
    if not out and page.number+1 not in structure.get("continued_figures", {}):
        # A Qt notice background can spill onto a new page without any text,
        # images or other content. Its colored stripe alone is decoration.
        only_rectangles = (structure["_qt"] and not any(b["type"] == 1 for b in blocks)
                           and all(p["type"] == "f" and len(p["items"]) == 1
                                   and p["items"][0][0] == "re" for p in drawings)
                           and any(p["rect"].y0 < box[1] and p["rect"].y1 < box[1]+25
                                   and p["rect"].width > 100 for p in drawings)
                           and all(p["rect"].y1 < box[1]+25 or p["rect"].y0 > box[3] for p in drawings))
        figure = None if only_rectangles else fallback_figure(page, box, directory, asset_prefix=asset_prefix)
        if figure:
            images.append(figure)
            out.append(figure)
            structure["issues"].append(dict(page=page.number+1, reason="Body preserved as a page image; verify text or diagram."))
    out.sort(key=lambda e: (e["bbox"][1], e["bbox"][0]))
    decorate_events(page, out, drawings)
    return out, {im["url"] for im in images}


def convert(source, target, language, source_key="", source_sha256=""):
    source, target = Path(source), Path(target)
    source_key = source_key or source.name
    if not source_sha256:
        with open(source, "rb") as f:
            source_sha256 = hashlib.file_digest(f, "sha256").hexdigest()
    images, blank = set(), []
    table_count = 0
    joined = 0
    with pymupdf.open(str(source)) as pdf:
        if not language:
            language = "cn" if re.search(r"[\u3400-\u9fff]", pdf[0].get_text()) else "en"
        structure = build_structure(pdf, language)
        identity = resolve_identity(
            source_key=source_key,
            cover_lines=structure["cover"],
            pdf_sha256=source_sha256,
            lang_hint=language,
        )
        asset_prefix = identity["assets_dir"]
        asset_dir = target.parent / asset_prefix
        structure["_qt"] = "wkhtml" in (pdf.metadata.get("creator") or "").lower()
        parts = [front_matter(structure, language)]
        section = []
        def flush():
            nonlocal table_count
            if not section:
                return
            for event in section:
                if event["kind"] == "table":
                    table_count += 1
                    for reason in event["issues"]:
                        m = re.match(r"p\.(\d+):\s*(.*)", reason)
                        structure["issues"].append(dict(page=int(m[1]) if m else event["page"], reason=m[2] if m else reason))
            parts.append(render_body(section, language))
            section.clear()
        for num in range(structure["first_body"], len(pdf)+1):
            page = pdf[num-1]
            events, urls = page_events(page, structure, asset_dir, asset_prefix=asset_prefix)
            images.update(urls)
            if not events and num not in structure.get("continued_figures", {}):
                blank.append(num)
            for event in events:
                if event["kind"] == "heading":
                    flush()
                elif section and event["kind"] == "table" and merge_tables(section[-1], event):
                    joined += 1
                    continue
                section.append(event)
            if num % 50 == 0:
                pymupdf.TOOLS.store_shrink(70)
        flush()
        md = "\n\n".join(part.strip("\n") for part in parts if part.strip()) + "\n"
        missing = images - set(ASSET.findall(md))
        if missing:
            raise ValueError(f"{len(missing)} extracted image references missing from Markdown: {sorted(missing)[:2]}")
        if any(not url.startswith(asset_prefix + "/") for url in images):
            raise ValueError(f"Asset URL escaped per-document directory {asset_prefix}")
        anchors = re.findall(r'<a\s+(?:id|name)="([^"]+)"', md)
        expected = [e["anchor"] for e in structure["entries"]]
        if len(anchors) != len(expected) or set(anchors) != set(expected):
            raise ValueError("Contents and body anchor sets differ")
        if not all((target.parent / url).is_file() for url in images):
            raise ValueError("An image is missing from the assets directory")
        if not parts[1:] and structure["first_body"] <= len(pdf):
            raise ValueError("No body was rendered")
        expected_names = {Path(url).name for url in images}
        if asset_dir.is_dir() and asset_dir.name.endswith(".assets"):
            for leftover in list(asset_dir.iterdir()):
                if leftover.is_file() and leftover.name not in expected_names:
                    leftover.unlink()
            if not expected_names and not any(asset_dir.iterdir()):
                asset_dir.rmdir()
        data = md.encode("utf-8")
        atomic_write(target, data)
        return dict(pages=len(pdf), first_body=structure["first_body"], body_pages=len(pdf)-structure["first_body"]+1,
                    blank_pages=blank, continued_figure_pages=sorted(structure.get("continued_figures", {})),
                    headings=len(expected), images=len(images), tables=table_count,
                    table_joins=joined, bytes=len(data), issues=structure["issues"],
                    assets_dir=asset_prefix, assets=sorted(expected_names),
                    document_id=identity["document_id"], language=identity["language"],
                    package_version=identity["package_version"], platform_version=identity["platform_version"],
                    category=identity["category"], product_code=identity["product_code"],
                    product=identity["product"], document_key=identity["document_key"],
                    base_document_key=identity["base_document_key"],
                    document_version=identity["document_version"], title=identity["title"],
                    id_status=identity["id_status"], id_source=identity["id_source"],
                    id_anomalies=identity["id_anomalies"])
