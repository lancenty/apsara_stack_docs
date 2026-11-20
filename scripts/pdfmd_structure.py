"""Recover cover text, numbered sections and body boundaries from the archive PDFs."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import re
import unicodedata


# The Chinese PDF fonts encode many ordinary Han characters as radical symbols.
# NFKC handles the Kangxi block but leaves most simplified radical forms intact.
_HAN_TRANSLATION = {
    cp: unicodedata.normalize("NFKC", chr(cp))
    for start, end in ((0x2E80, 0x2FE0), (0xF900, 0xFB00), (0x2F800, 0x2FA20))
    for cp in range(start, end)
    if unicodedata.normalize("NFKC", chr(cp)) != chr(cp)
}
_HAN_TRANSLATION.update(str.maketrans({
    "⺠": "民", "⻄": "西", "⻅": "见", "⻆": "角", "⻉": "贝", "⻋": "车",
    "⻓": "长", "⻔": "门", "⻘": "青", "⻚": "页", "⻛": "风", "⻜": "飞",
    "⻢": "马", "⻣": "骨", "⻤": "鬼", "⻥": "鱼", "⻦": "鸟", "⻧": "卤",
    "⻨": "麦", "⻩": "黄", "⻬": "齐", "⻮": "齿", "⻰": "龙", "⻳": "龟",
    "\xa0": " ", "\u200b": "", "\ufeff": "", "\xad": "",
}))
_NUMBER = re.compile(r"^(\d+(?:\.\d+)*)")
_PRINTED_PAGE = re.compile(r"\s*(?:\.{2,}|…+)\s*(\d+)\s*$")
_LOOKALIKE = str.maketrans({"’": "'", "‘": "'", "–": "-", "‑": "-", "‐": "-", "—": "-"})


def normalize_text(text: str) -> str:
    """Normalize extraction artefacts without folding ordinary prose punctuation."""
    return text.translate(_HAN_TRANSLATION)


def _key(text):
    return "".join(unicodedata.normalize("NFKC", normalize_text(text)).casefold()
                   .translate(_LOOKALIKE).split())


def _lines(page):
    # PyMuPDF flag 3 keeps ligatures and whitespace and excludes image bytes.
    return [
        {"text": "".join(s["text"] for s in line["spans"]),
         "bbox": line["bbox"], "spans": line["spans"]}
        for block in page.get_text("dict", flags=3)["blocks"]
        for line in block.get("lines", [])
    ]


def _cover(page):
    result, seen = [], set()
    for line in _lines(page):
        text = normalize_text(line["text"]).strip()
        key = _key(text)
        if not key:
            continue
        # Qt paints the entire cover twice at different scales. A second
        # rendering can wrap product names at different positions.
        if result and key == _key(result[0]) and any(
            "文档版本" in value or "documentversion" in _key(value)
            for value in result
        ):
            break
        if key not in seen:
            result.append(text)
            seen.add(key)
    return result


def _word_contents(doc, issues):
    """Read printed contents rows and their internal destinations, including continuations."""
    entries = []
    in_contents = False
    first_body = len(doc) + 1
    for index in range(1, len(doc)):
        if index + 1 >= first_body:
            break
        page = doc[index]
        lines = _lines(page)
        if not in_contents:
            in_contents = any(_key(l["text"]) in {"content", "contents", "tableofcontents", "目录"}
                              for l in lines)
            if not in_contents:
                continue
        for link in sorted(page.get_links(), key=lambda l: (l["from"].y0, l["from"].x0)):
            if link.get("kind") != 1 or link.get("page", -1) <= index:
                continue
            box = link["from"]
            row = sorted((line for line in lines
                          if box.y0 <= (line["bbox"][1] + line["bbox"][3]) / 2 < box.y1
                          and box.x0 - 2 <= line["bbox"][0] < box.x1),
                         key=lambda l: l["bbox"][0])
            text = " ".join(" ".join(l["text"].split()) for l in row).strip()
            leader = _PRINTED_PAGE.search(text)
            number = _NUMBER.match(text)
            if not (number and leader):
                issues.append({"page": index + 1, "reason": "Unrecognized numbered contents row: " + text})
                continue
            title = normalize_text(text[:leader.start()].strip())
            target = link["page"] + 1
            if int(leader.group(1)) != target:
                issues.append({"page": index + 1, "reason": f"Printed page and link differ for {title}"})
            entries.append(_Section(number.group().count(".") + 1, title, target, link["to"].y))
            first_body = min(first_body, target)
    return entries


@dataclass
class _Section:
    level: int
    title: str
    page: int
    y: float
    name: str = ""
    contents_page: int = 0
    printed_number: int = 0
    truncated: bool = False
    body_title: str = ""


def _number(title):
    match = _NUMBER.match(title)
    return match.group() if match else ""


def _destination(doc, dest, page_number):
    point = dest.get("to")
    if point is None or not 1 <= page_number <= len(doc):
        return 79.5
    if dest.get("kind") == 4:
        # wkhtmltopdf's named links expose the raw bottom-up PDF coordinate.
        return doc.page_cropbox(page_number - 1).height - point.y
    return point.y


def _printed_qt(doc, outline):
    """Recognize the actual contents section, including its blank continuation page."""
    result = []
    started = False
    # A bookmark aimed into front matter must not stop the contents search early.
    likely_start = max(12, min((e.page for e in outline if e.page > 0), default=12))
    first_body = None
    for index in range(1, len(doc)):
        if not started and index > likely_start:
            break
        page = doc[index]
        lines = _lines(page)
        body = body_box(page, {})
        title = any(_key(l["text"]) in {"tableofcontents", "目录"}
                    for l in lines if body[1] < l["bbox"][1] < 150)
        if not started and not title:
            continue
        # The Qt table of contents uses Roman footers on both languages and
        # every continuation, while the actual body uses physical Arabic pages.
        roman = any(re.fullmatch(r"[IVXLCDM]+", l["text"].strip())
                    for l in lines if l["bbox"][1] > body[3])
        if started and not (roman or title):
            break
        started = True
        first_body = index + 2
        links = [l for l in page.get_links() if l.get("kind") in {1, 4}]
        bands = []
        for idx, box, _ in _reading_order(lines, body):
            text = lines[idx]["text"].strip()
            if _key(text) in {"目录", "tableofcontents"}:
                continue
            center = (box[1] + box[3]) / 2
            if not bands or abs(center - bands[-1][0]) > 5:
                bands.append((center, []))
            bands[-1][1].append((box, text))
        for center, band in bands:
            numbers = [int(t) for b, t in band if b[0] > page.rect.width * .83 and t.isdecimal()]
            left = [(b, t) for b, t in band if b[0] < page.rect.width * .83]
            if not left:
                continue
            left.sort(key=lambda v: v[0][0])
            raw = normalize_text(" ".join(t for _, t in left)).strip()
            truncated = raw.endswith("…")
            title_text = raw.removesuffix("…").rstrip()
            link = next((l for l in links if l["from"].y0 <= center < l["from"].y1), {})
            if not (link or numbers or _number(title_text)):
                continue
            printed = numbers[0] if numbers else 0
            target = link.get("page", -1) + 1 or printed
            # The Qt template indents exactly 12 pt at each additional level.
            depth = max(1, round((left[0][0][0] - 70) / 12) + 1)
            result.append(_Section(depth, title_text, target, _destination(doc, link, target),
                                   link.get("nameddest", ""), index + 1, printed, truncated))
    return result, first_body


def _body_title(doc, row, titles):
    """Resolve an unusual or abbreviated contents label against its physical heading."""
    lines = _lines(doc[row.page - 1])
    ordered = _reading_order(lines, body_box(doc[row.page - 1], {}))
    for title in titles:
        if title and _match(ordered, {"title": title, "y": row.y}, set()):
            return title
    if not row.truncated:
        return ""
    prefix = _key(row.title)
    starts = [(abs(b[1] - row.y), i) for i, (_, b, key) in enumerate(ordered)
              if (prefix.startswith(key) or key.startswith(prefix)) and abs(b[1] - row.y) < 40]
    if not starts:
        return ""
    _, i = min(starts)
    idx, previous, _ = ordered[i]
    parts = [normalize_text(lines[idx]["text"]).strip()]
    size = max(s["size"] for s in lines[idx]["spans"])
    for idx, b, _ in ordered[i + 1:]:
        text = normalize_text(lines[idx]["text"]).strip()
        if (abs(max(s["size"] for s in lines[idx]["spans"]) - size) > 0.5
                or b[1] - previous[3] > 15 or _NUMBER.match(text)):
            break
        parts.append(text)
        previous = b
    joined = " ".join(parts)
    return joined if _key(joined).startswith(prefix) else ""


def _reconcile_qt(doc, outline, issues):
    printed, first_body = _printed_qt(doc, outline)
    if not printed:
        issues.append({"page": max(1, (first_body or 2) - 1),
                       "reason": "Could not recover the printed table of contents for comparison"})
        return [e for e in outline if (first_body or 1) <= e.page <= len(doc)], first_body
    indexed = {field: defaultdict(list) for field in ("name", "number", "label")}
    for i, e in enumerate(outline):
        for field, key in (("name", e.name), ("number", _number(e.title)), ("label", _key(e.title))):
            if key:
                indexed[field][key].append(i)
    used = set()
    result = []
    for row in printed:
        problems = []
        match = None
        for field, key in (("name", row.name), ("number", _number(row.title)), ("label", _key(row.title))):
            candidates = [i for i in indexed[field].get(key, ()) if i not in used]
            if candidates:
                match = min(candidates, key=lambda i: (abs(outline[i].page - row.page),
                                                       abs(outline[i].y - row.y)))
                break
        book = outline[match] if match is not None else None
        if book:
            used.add(match)
        if not first_body <= row.page <= len(doc):
            row.page = next((p for p in (row.printed_number, book.page if book else 0)
                             if first_body <= p <= len(doc)), 0)
            problems.append("invalid contents link destination")
        if not row.page:
            issues.append({"page": row.contents_page, "reason": f"No body destination for {row.title}"})
            continue
        if row.printed_number and row.printed_number != row.page:
            problems.append(f"printed page {row.printed_number} differs from linked page {row.page}")
            if first_body <= row.printed_number <= len(doc):
                candidate = _Section(row.level, row.title, row.printed_number, row.y, truncated=row.truncated)
                if (_body_title(doc, candidate, [row.title]) and
                        not _body_title(doc, row, [row.title])):
                    row.page = row.printed_number
        if book:
            if book.page != row.page:
                problems.append(f"bookmark page {book.page} differs from contents target {row.page}")
            if row.y == 79.5 and book.page == row.page:
                row.y = book.y
            same = _key(book.title) == _key(row.title)
            shortened = row.truncated and _key(book.title).startswith(_key(row.title))
            if same or shortened:
                row.title = book.title
            else:
                problems.append(f'printed label "{row.title}" differs from bookmark "{book.title}"')
                actual = _body_title(doc, row, [row.title, book.title])
                if not _number(row.title) and _number(book.title) and actual:
                    row.title = actual
                elif actual and row.truncated:
                    row.title = actual
                elif actual and _key(actual) != _key(row.title):
                    row.body_title = actual
            if book.level != row.level:
                problems.append(f"printed level {row.level} differs from bookmark level {book.level}")
        else:
            problems.append("recovered printed section missing from bookmarks")
            if row.truncated:
                row.title = _body_title(doc, row, []) or row.title
        if not _number(row.title):
            problems.append("section number missing in printed contents")
        if problems:
            issues.append({"page": row.contents_page,
                           "reason": f'{row.title} (body page {row.page}): ' + "; ".join(problems)})
        result.append(row)
    extra = [e for i, e in enumerate(outline) if i not in used]
    for e in extra:
        issues.append({"page": max(1, e.page), "reason": f"Bookmark absent from printed contents: {e.title}"})
        if first_body <= e.page <= len(doc):
            result.append(e)
    if extra:
        result.sort(key=lambda e: (e.page, e.y))
    return result, first_body


def build_structure(doc, language):
    """Return one-based physical pages, original numbered titles and unique anchors."""
    issues = []
    outline = doc.get_toc(simple=False)
    first_body = None
    if "wkhtmltopdf" in (doc.metadata.get("creator") or "").lower():
        bookmarks = [_Section(level, normalize_text(raw).strip(), number, _destination(doc, dest, number),
                              dest.get("nameddest", "")) for level, raw, number, dest in outline]
        rows, first_body = _reconcile_qt(doc, bookmarks, issues)
    elif outline:
        rows = [_Section(level, normalize_text(raw).strip(), number, _destination(doc, dest, number))
                for level, raw, number, dest in outline if 1 <= number <= len(doc)]
    else:
        rows = _word_contents(doc, issues)
    entries, by_page, used_anchors = [], defaultdict(list), set()
    for row in rows:
        match = _NUMBER.match(row.title)
        prefix = match.group().replace(".", "-") if match else f"item-{len(entries) + 1}"
        base = "section-" + prefix
        anchor = base
        suffix = 1
        while anchor in used_anchors:
            suffix += 1
            anchor = f"{base}-{suffix}"
        used_anchors.add(anchor)
        entry = dict(level=row.level, title=row.title, anchor=anchor, page=row.page, y=float(row.y))
        if row.body_title:
            entry["body_title"] = row.body_title
        entries.append(entry)
        by_page[row.page].append(entry)
    if not entries:
        issues.append({"page": 1, "reason": "No numbered contents or bookmarks could be recovered"})
    return {"cover": _cover(doc[0]), "entries": entries, "first_body": first_body or min(by_page, default=2),
            "issues": issues, "_by_page": dict(by_page)}


def body_box(page, structure):
    """Archive A4 templates place running headers and footers in the outer 65 points."""
    rect = page.rect
    if structure.get("_qt"):
        return (rect.x0, rect.y0 + 69, rect.x1, rect.y1 - 69)
    return (rect.x0, rect.y0 + 65, rect.x1, rect.y1 - 65)


def _reading_order(lines, box):
    """Group fragments sharing a baseline before sorting each row left to right."""
    fragments = []
    for idx, l in enumerate(lines):
        key = _key(l["text"])
        b = l["bbox"]
        center = (b[1] + b[3]) / 2
        if key and box[1] <= center <= box[3]:
            fragments.append((center, idx, b, key))
    rows = []
    for center, idx, b, key in sorted(fragments, key=lambda t: (t[0], t[2][0])):
        # A single Word heading can mix sizes for number and heading text.
        if not rows or abs(center - rows[-1][0]) > min(5, (b[3] - b[1]) * 0.35):
            rows.append((center, []))
        rows[-1][1].append((idx, b, key))
    return [v for _, row in rows for v in sorted(row, key=lambda v: v[1][0])]


def _match(ordered, entry, used):
    target = _key(entry.get("body_title", entry["title"]))
    starts = [i for i, (idx, _, key) in enumerate(ordered) if idx not in used and target.startswith(key)]
    starts.sort(key=lambda i: abs(ordered[i][1][1] - entry["y"]))
    for start in starts:
        parts, value = [], ""
        for idx, box, key in ordered[start:]:
            if parts and box[1] - parts[-1][1][3] > 45:
                break
            if idx in used or not target.startswith(value + key):
                if parts:
                    # A floating table in the PDF can overlap the heading. Its
                    # small-print rows can lie between two lines of the title.
                    first_box = parts[0][1]
                    if box[3] - box[1] < 0.75 * (first_box[3] - first_box[1]):
                        continue
                break
            parts.append((idx, box))
            value += key
            if value == target:
                return parts
    return []


def heading_events(page, lines, structure):
    """Replace printed heading fragments with one anchored heading per ToC item."""
    number = page.number + 1
    entries = structure["_by_page"].get(number, ())
    events, claimed = [], set()
    if not entries:
        return events, claimed
    box = body_box(page, structure)
    ordered = _reading_order(lines, box)
    for entry in entries:
        matches = _match(ordered, entry, claimed)
        if matches:
            xs0, ys0, xs1, ys1 = zip(*(b for _, b in matches))
            bounds = (min(xs0), min(ys0), max(xs1), max(ys1))
            claimed.update(i for i, _ in matches)
            # Some generators paint headings twice at effectively the same position.
            for idx, b, text in ordered:
                if idx not in claimed and any(text == _key(lines[m]["text"])
                                              and max(abs(a - c) for a, c in zip(b, mb)) < 2
                                              for m, mb in matches):
                    claimed.add(idx)
        else:
            y = max(box[1], min(entry["y"], box[3]))
            bounds = (69.75, y, 70.75, y + 1)
            structure["issues"].append({"page": number, "reason":
                f'Printed heading did not match contents: {entry["title"]}'})
        events.append({"kind": "heading", "bbox": bounds, "page": number,
                       "title": entry.get("body_title", entry["title"]),
                       "anchor": entry["anchor"], "level": entry["level"]})
    return events, claimed
