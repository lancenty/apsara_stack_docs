"""Extract original raster images and preserve the appearance of composite figures."""

import hashlib
import os
import time
from pathlib import Path
from tempfile import NamedTemporaryFile

import pymupdf

from pdfmd_body import _is_mono


def atomic_write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(dir=path.parent, prefix=".pdfmd-", delete=False) as f:
        tmp = Path(f.name)
        try:
            f.write(data)
        except BaseException:
            f.close()
            tmp.unlink(missing_ok=True)
            raise
    try:
        for attempt in range(6):
            try:
                os.replace(tmp, path)
                break
            except PermissionError:
                # Concurrent PDF workers can finish the same content-addressed asset.
                try:
                    if path.is_file() and path.read_bytes() == data:
                        break
                except PermissionError:
                    pass
                if attempt == 5:
                    raise
                time.sleep(.06 * 2**attempt)
    finally:
        tmp.unlink(missing_ok=True)


def in_box(inner, outer, slack=1.5):
    return (inner[0] >= outer[0] - slack and inner[1] >= outer[1] - slack
            and inner[2] <= outer[2] + slack and inner[3] <= outer[3] + slack)


def _asset(data, ext, rect, page, directory, small=False, asset_prefix="assets"):
    name = hashlib.sha256(data).hexdigest()[:32] + "." + ext
    file = directory / name
    try:
        present = file.is_file() and file.stat().st_size == len(data) and file.read_bytes() == data
    except PermissionError:
        present = False
    if not present:
        atomic_write(file, data)
    url = f"{asset_prefix}/{name}"
    if small:
        md = f'<img src="{url}" width="{max(1, round(rect.width * 4/3))}" alt="">'
    else:
        md = f"![]({url})"
    return dict(kind="image", bbox=tuple(rect), page=page.number + 1, md=md, url=url)


def _crop(page, rect, directory, scale=3, asset_prefix="assets"):
    bitmap = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), clip=rect, alpha=False)
    return _asset(bitmap.tobytes("png"), "png", rect, page, directory, asset_prefix=asset_prefix)


def _vector_marks(drawings, body):
    for path in drawings:
        box = path["rect"]
        if not in_box(box, body) or max(box.width, box.height) < 7:
            continue
        # Qt paints background fills, rules and table grids as rectangles.
        # Non-rectangular paths, including diagonals, are evidence of a figure.
        if any(item[0] in ("c", "qu") or
               (item[0] == "l" and abs(item[1].x-item[2].x) > 1
                and abs(item[1].y-item[2].y) > 1) for item in path["items"]):
            yield path


def _inline_code_background(path, code_spans):
    """Qt paints inline code over a gray box, rounding only the exposed ends at line breaks."""
    fill = path.get("fill")
    if path["type"] != "f" or not fill or any(abs(c - 238 / 255) > .004 for c in fill):
        return False
    rect = path["rect"]
    items = path["items"]
    edges = [item for item in items if item[0] == "l"]
    if len(edges) != 4 or len(items) not in (6, 8) or any(i[0] not in ("l", "c") for i in items):
        return False
    # Require one straight segment on each boundary of the filled path.
    for axis, side in ((0, rect.x0), (0, rect.x1), (1, rect.y0), (1, rect.y1)):
        if not any(abs(edge[1][axis] - side) < .1 and abs(edge[2][axis] - side) < .1 for edge in edges):
            return False
    for span in code_spans:
        x0, y0, x1, y1 = span["bbox"]
        if (in_box(span["bbox"], rect, 1) and rect.height <= span["size"] * 2.4
                and abs((y0 + y1) - (rect.y0 + rect.y1)) < span["size"] * .5
                and min(abs(x0 - rect.x0), abs(x1 - rect.x1)) < span["size"]):
            return True
    return False


def _vector_regions(page, marks):
    regions = page.cluster_drawings(drawings=marks, x_tolerance=8, y_tolerance=8)
    # Disconnected strokes may form a small component *inside* the bounds of
    # another component. The first emitted crop otherwise suppresses the larger
    # one. Only prioritize the larger region when the PDF supplies its viewport.
    nested = [outer for i, outer in enumerate(regions)
              if any(in_box(inner, outer, 0) for inner in regions[:i])]
    if not nested:
        return regions
    viewports = set()
    page_clip = None
    for item in page.get_drawings(extended=True):
        if item["type"] != "clip":
            continue
        clip = item["scissor"]
        if item["level"] == 0:
            page_clip = clip
        elif page_clip is not None and not in_box(page_clip, clip):
            viewports.add(tuple(clip))
    confirmed = {tuple(r) for r in nested
                 if any(max(abs(a - b) for a, b in zip(r, clip)) <= 2 for clip in viewports)}
    return sorted(regions, key=lambda r: -abs(r) if tuple(r) in confirmed else 0)


def _image_key(block):
    return (*[round(v, 1) for v in block["bbox"]], block["width"], block["height"])


def _whole_screenshot(page, block, body, state):
    """A Qt image can be painted once per paper page with a translated top edge."""
    bounds = pymupdf.Rect(block["bbox"])
    if bounds.y0 < body.y0 or bounds.y1 <= body.y1 or bounds.x0 < body.x0 or bounds.x1 > body.x1:
        return False
    match = next((i for i in page.get_image_info(hashes=True) if _image_key(i) == _image_key(block)), None)
    if not match:
        return False
    continuations = []
    current = bounds
    for idx in range(page.number+1, len(page.parent)):
        next_page = page.parent[idx]
        other_images = next_page.get_image_info(hashes=True)
        candidate = next((i for i in other_images if i["digest"] == match["digest"]
                          and abs(i["bbox"][0]-bounds.x0) < 1 and abs(i["bbox"][2]-bounds.x1) < 1
                          and i["bbox"][1] < body.y0 and current.y0-i["bbox"][1] > body.height*.7), None)
        if not candidate:
            return False
        current = pymupdf.Rect(candidate["bbox"])
        visible = current & body
        if any(in_box(t[:4], visible, 0) for t in next_page.get_text("blocks", flags=3)):
            return False
        if any(i is not candidate and abs(pymupdf.Rect(i["bbox"]) & visible) > 1 for i in other_images):
            return False
        if any(in_box(p["rect"], visible) for p in _vector_marks(next_page.get_drawings(), body)):
            return False
        continuations.append((idx+1, _image_key(candidate)))
        if current.y1 <= body.y1:
            repeated = state.setdefault("continued_figures", {})
            for number, key in continuations:
                repeated.setdefault(number, set()).add(key)
            return True
    return False


def extract_figures(page, blocks, lines, drawings, tables, body, directory, state, asset_prefix="assets"):
    body = pymupdf.Rect(body)
    images = []
    for block in blocks:
        if block["type"] != 1:
            continue
        if _image_key(block) in state.get("continued_figures", {}).get(page.number+1, ()):
            continue
        rect = pymupdf.Rect(block["bbox"]) & body
        if rect.is_empty or rect.width < 1 or rect.height < 1:
            continue
        if max(rect.width, rect.height) < 22:
            # Only discard tiny decorations beside a recognized notice label.
            if any(abs(line["bbox"][1]-rect.y0) < 7 and
                   rect.x0-2 <= line["bbox"][0] <= rect.x1+12 and
                   line["text"].strip().casefold() in {
                       "说明","重要","警告","危险","注意","提示","note","important",
                       "warning","danger","notice","caution","tip"}
                   for line in lines):
                continue
        images.append((rect, block))

    marks = list(_vector_marks(drawings, body))
    covered = set()
    events = []
    used = set()
    for index, (rect, block) in enumerate(images):
        if index in used:
            continue
        rect = pymupdf.Rect(rect)
        composite = False
        for j in range(index+1, len(images)):
            other, _ = images[j]
            if j not in used and abs(rect & other) > 1:
                rect |= other
                used.add(j)
                composite = True
        caption = {i for i, line in enumerate(lines) if in_box(line["bbox"], rect, 0)}
        # Include annotation strokes and live text placed over a screenshot.
        overlay = any(in_box(p["rect"], rect, 0) and
                      (p["type"] != "f" or len(p["items"]) != 1)
                      and max(p["rect"].width, p["rect"].height) >= 8
                      for p in drawings)
        tr = block["transform"]
        clipped = not in_box(block["bbox"], body)
        if clipped and state["_qt"] and not (composite or caption or overlay):
            clipped = not _whole_screenshot(page, block, body, state)
        if composite or caption or overlay or tr[0] <= 0 or tr[3] <= 0 or abs(tr[1])+abs(tr[2]) > 0.01 or clipped:
            scale = max(3, min(6, block["width"] / max(1, rect.width)))
            event = _crop(page, rect, directory, scale, asset_prefix=asset_prefix)
            covered.update(caption)
        else:
            data, ext = block["image"], block["ext"]
            if block.get("mask"):
                pix = pymupdf.Pixmap(data)
                if pix.alpha:
                    pix = pymupdf.Pixmap(pix, 0)
                mask = pymupdf.Pixmap(block["mask"])
                data, ext = pymupdf.Pixmap(pix, mask).tobytes("png"), "png"
            elif ext not in ("jpeg", "png", "gif", "webp"):
                pix = pymupdf.Pixmap(data)
                if pix.colorspace and pix.colorspace.n > 3:
                    pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
                data, ext = pix.tobytes("png"), "png"
            event = _asset(data, ext, rect, page, directory, max(rect.width, rect.height) <= 22, asset_prefix=asset_prefix)
        events.append(event)

    marks = [p for p in marks if not any(in_box(p["rect"], r) for r, _ in images)]
    artwork = marks
    if marks and state["_qt"]:
        code = [s for line in lines for s in line["spans"] if _is_mono(s) and s["text"].strip()]
        if code:
            artwork = [p for p in marks if not _inline_code_background(p, code)]
    if artwork:
        for rect in _vector_regions(page, marks):
            rect = rect & body
            if rect.width < 28 or rect.height < 14:
                continue
            # Preserve the entire cluster when a real drawing touches a styled label.
            if len(artwork) < len(marks) and not any(in_box(p["rect"], rect, 0) for p in artwork):
                continue
            if any(abs(rect & pymupdf.Rect(im["bbox"])) > 1 for im in events):
                continue
            # Table structure remains text. Vector figures in a cell can still be attached.
            if any(in_box(t["bbox"], rect) for t in tables):
                continue
            rect = (rect + (-2, -2, 2, 2)) & body
            events.append(_crop(page, rect, directory, asset_prefix=asset_prefix))
            covered.update(i for i, line in enumerate(lines) if in_box(line["bbox"], rect, 0))
    return events, covered


def fallback_figure(page, body, directory, asset_prefix="assets"):
    """Preserve independently drawn content on a page with no extracted events."""
    rect = pymupdf.Rect(body)
    preview = page.get_pixmap(matrix=pymupdf.Matrix(.7,.7), clip=rect, colorspace=pymupdf.csGRAY)
    if sum(v < 230 for v in preview.samples) < 5:
        return None
    return _crop(page, rect, directory, asset_prefix=asset_prefix)
