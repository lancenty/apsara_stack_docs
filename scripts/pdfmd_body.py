"""Render the body of an Apsara manual from page-positioned extraction events."""

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from html import escape
import json
import re
from statistics import median
from string import punctuation
import unicodedata

from pdfmd_structure import normalize_text


MONO = re.compile(r"courier|monospace|mono(?:spaced)?|consolas|menlo|inconsolata|fixed", re.I)
BOLD = re.compile(r"bold|heavy", re.I)
ITALIC = re.compile(r"italic|oblique|slanted", re.I)
EMPHASIS = {"bold": ("**", ("strong",)), "italic": ("*", ("em",)),
            "bolditalic": ("***", ("em", "strong"))}
MARKER = re.compile(r"^\s*(?:(\d{1,4}|[ivxlcdm]{1,7}|[IVXLCDM]{1,7}|[a-zA-Z])[.)](?=\s|[\u3000-\u9fff])\s*|([•●◦▪‣])\s*)")
NOTE = re.compile(r"^(说明|注意|重要|警告|危险|提示|Note|Important|Warning|Caution|Danger|Tip)\s*[:：]?$", re.I)
CJK = re.compile(r"[\u2e80-\ua4cf\uf900-\ufaff\uff00-\uffef]")
ROMAN = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}


def _size(event):
    spans = event.get("spans", ())
    return max((s.get("size", 10) for s in spans), default=10)


def _baseline(event):
    return next((s["origin"][1] for s in event.get("spans", ()) if "origin" in s), event["bbox"][3])


def _raw(event):
    return "".join(s.get("text", "") for s in event.get("spans", ())) or event.get("text", "")


def _is_mono(span):
    return bool(span.get("flags", 0) & 8 or MONO.search(span.get("font", "")))


def span_style(span):
    """Recognize the same font styling in ordinary prose and in table cells."""
    flags, font = span.get("flags", 0), span.get("font", "")
    bold = "bold" if flags & 16 or BOLD.search(font) else ""
    italic = "italic" if flags & 2 or ITALIC.search(font) else ""
    return bold + italic + ("code" if _is_mono(span) else "")


def _inside(bbox, rect):
    mid = (bbox[1] + bbox[3]) / 2
    return rect[0] - 2 <= bbox[0] and bbox[2] <= rect[2] + 2 and rect[1] <= mid <= rect[3]


def _union(boxes):
    return (min(b[0] for b in boxes), min(b[1] for b in boxes),
            max(b[2] for b in boxes), max(b[3] for b in boxes))


def _split_at_icon(span, icon, slack, get_chars):
    """MuPDF sometimes joins the words on either side of an icon into one font run."""
    chars = span.get("chars") or get_chars(span)
    if not chars:
        return None
    sides = [[], []]
    for ch in chars:
        left, _, right, _ = ch["bbox"]
        if right <= icon[0] + slack:
            sides[0].append(ch)
        elif left >= icon[2] - slack:
            sides[1].append(ch)
        elif not ch["c"].isspace():
            return None  # The image overlaps printed text. Keep it as its own figure.
    return [dict(span, text="".join(c["c"] for c in side), chars=side,
                 bbox=_union([c["bbox"] for c in side]), origin=side[0]["origin"])
            for side in sides if side]


def _inline_images(page, events):
    images = [e for e in events if e["kind"] == "image"]
    if not images:
        return
    raw = None

    def get_chars(span):
        nonlocal raw
        if raw is None:
            import pymupdf
            flags = pymupdf.TEXTFLAGS_RAWDICT & ~pymupdf.TEXT_PRESERVE_IMAGES
            blocks = page.get_text("rawdict", flags=flags, clip=pymupdf.INFINITE_RECT())["blocks"]
            raw = {(c["origin"], s["font"]): (s["chars"], i) for b in blocks
                   for line in b.get("lines", ()) for s in line["spans"] for i,c in enumerate(s["chars"])}
        glyphs, offset = raw.get((span.get("origin"), span.get("font")), ([], 0))
        chars = glyphs[offset:]
        # Qt extraction suppresses the synthetic spaces present in default rawdict.
        for candidate in (chars, [c for c in chars if not c.get("synthetic")]):
            candidate = candidate[:len(span["text"])]
            if "".join(c["c"] for c in candidate) == span["text"]:
                return candidate
        return None

    for image in images:
        box = image["bbox"]
        width, height = box[2] - box[0], box[3] - box[1]
        mid_y = (box[1] + box[3]) / 2
        nearby = []
        for idx, line in enumerate(events):
            if line["kind"] != "line" or line.get("code_rect") or line.get("notice_rect") != image.get("notice_rect"):
                continue
            size = _size(line)
            y_gap = abs(mid_y - (_baseline(line) - size * .32))
            if (height > size * 2 or width > size * 8 or y_gap > size * .55
                    or line["bbox"][2] < box[0] - size or line["bbox"][0] > box[2] + size):
                continue
            slack = size * .15
            spans = []
            for s in line["spans"]:
                x0, _, x1, _ = s["bbox"]
                if x1 <= box[0] + slack or x0 >= box[2] - slack:
                    spans.append(s)
                else:
                    pieces = _split_at_icon(s, box, slack, get_chars)
                    if pieces is None:
                        break
                    spans.extend(pieces)
            else:
                left = min((abs(box[0] - s["bbox"][2]) for s in spans if s["bbox"][2] <= box[0]+slack), default=float("inf"))
                right = min((abs(s["bbox"][0] - box[2]) for s in spans if s["bbox"][0] >= box[2]-slack), default=float("inf"))
                if min(left, right) <= size:
                    nearby.append((y_gap, min(left, right), idx, line, spans))
        if not nearby:
            continue
        # Only join neighbours sharing the best matching baseline. Adjacent rows and
        # independent columns elsewhere on that baseline retain their own blocks.
        reference = min(nearby, key=lambda n: n[:2])[3]
        row = [n for n in nearby if abs(_baseline(n[3]) - _baseline(reference)) <= _size(reference) * .18]
        leftmost = min(row, key=lambda n: n[3]["bbox"][0])
        spans = [s for n in row for s in n[4]]
        md = image["md"]
        if image.get("url"):
            # A wide inline toolbar button may have many more source pixels than
            # its printed size. Keep the native asset and display its PDF width.
            url = escape(image["url"], quote=True)
            md = f'<img src="{url}" width="{max(1, round(width * 4/3))}" alt="">'
        spans.append(dict(text="\ufffc", inline_image=md, bbox=box, size=_size(reference)))
        spans.sort(key=lambda s: s["bbox"][0])
        merged = dict(leftmost[3], spans=spans, bbox=_union([box] + [n[3]["bbox"] for n in row]),
                      text="".join(s["text"] for s in spans))
        removed = {n[2] for n in row}
        events[:] = [merged if idx == leftmost[2] else e for idx, e in enumerate(events)
                     if idx == leftmost[2] or (idx not in removed and e is not image)]


def decorate_events(page, events, drawings=None):
    """Attach panel geometry and vector bullet markers. Rectangles may extend over a page break."""
    bars = set()
    panels = []
    codes = []
    shaded_lines = []
    dots = defaultdict(list)
    for path in page.get_drawings() if drawings is None else drawings:
        rect = tuple(path["rect"])
        x, y, right, bottom = rect
        w, h = right - x, bottom - y
        items = path.get("items", ())
        fill = path.get("fill")
        if 1 <= w <= 5 and 1 <= h <= 5:
            if any(i[0] == "c" for i in items) or (fill and max(fill) < .65):
                dots[round((y + bottom) / 2)].append(rect)
        if not fill or not items or items[0][0] != "re":
            continue
        if w <= 4 and h > 10 and max(fill) - min(fill) > .12:
            bars.add((round(x), round(y), round(bottom)))
        if w >= 30 and h > 8:
            if w > page.rect.width * .55 and len(fill) == 3 and all(
                abs(c - target) < .003 for c, target in zip(fill, (.816, .808, .808))
            ):
                shaded_lines.append(rect)
            elif len(fill) and all(abs(c - 238 / 255) < .004 for c in fill):
                codes.append(rect)
            elif min(fill) > .7 and min(fill) < .998:
                panels.append(rect)
    panels = [r for r in panels if (round(r[0]), round(r[1]), round(r[3])) in bars]
    word_panels = []
    for rect in sorted(set(shaded_lines), key=lambda r: (r[0], r[1])):
        if word_panels and abs(word_panels[-1][3] - rect[1]) < 1 and abs(word_panels[-1][0] - rect[0]) < 1 and abs(word_panels[-1][2] - rect[2]) < 1:
            word_panels[-1] = (*word_panels[-1][:3], rect[3])
        else:
            word_panels.append(rect)
    codes.extend(word_panels)
    for e in events:
        if not e.get("bbox"):
            continue
        box = e["bbox"]
        e["page_height"] = page.rect.height
        for rect in panels:
            if _inside(box, rect):
                e["notice_rect"] = rect
                break
        if e["kind"] != "line":
            continue
        for rect in codes:
            if _inside(box, rect):
                e["code_rect"] = rect
                break
        mid = round((box[1] + box[3]) / 2)
        size = _size(e)
        for pos in range(mid - 3, mid + 4):
            if any(.14 * size <= box[0] - dot[2] <= size * 1.2 for dot in dots.get(pos, ())):
                e["bullet"] = True
                break
    _inline_images(page, events)
    return events


def _same_panel(prev, curr, key):
    old, new = prev.get(key), curr.get(key)
    if not old or not new:
        return False
    if prev["page"] == curr["page"]:
        return old == new
    if curr["page"] != prev["page"] + 1 or abs(new[0] - old[0]) > 2 or abs(new[2] - old[2]) > 2:
        return False
    return (new[1] < 0 or old[3] > prev.get("page_height", 842)
            or (new[1] < curr.get("page_height", 842) * .12
                and old[3] > prev.get("page_height", 842) * .89))


def _fence(text, minimum=3):
    return "`" * max([minimum] + [len(s) + 1 for s in re.findall(r"`+", text)])


def _code_language(code):
    sample = code.lstrip()
    if re.match(r"\$\s+[a-z][\w.-]*(?:\s|$)", sample):
        return "bash"
    if sample.startswith(("{", "[")):
        try:
            json.loads(sample)
            return "json"
        except (ValueError, RecursionError):
            if re.match(r'[\[{]\s*(?:\{\s*)?"[^"\n]+"\s*:', sample):
                return "json"
    signatures = [
        ("python", r"^#![^\n]*python|^(?:from [\w.]+ import |import [\w.]+\s*$|def \w+\(.*:\s*$|if __name__\s*==)"),
        ("bash", r"^#![^\n]*(?:sh|bash)\b|^(?:[$#]\s+)?(?:sudo|curl|wget|kubectl|docker|helm|aliyun|aliyuncli|apt-get|ssh|export|chmod|yum|rpm|systemctl|openssl|echo|cat|cd|ls|mkdir|tar|pip3?|git)\s+"),
        ("sql", r"(?i)^(?:select\b.+\bfrom\b|insert into\b|create (?:table|database|index)\b|alter table\b|update .+ set\b|grant .+ on\b|with \w+ as\s*\()"),
        ("xml", r"^<\?xml|^<[\w:.\-]+(?:\s|>|/>)"),
        ("yaml", r"^(?:---\s*\n|(?:apiVersion|kind|version|services|metadata|spec|name):\s)"),
        ("go", r"^package \w+\s*$|^func (?:main|\w+)\("),
        ("csharp", r"^using (?:System|Microsoft)[.;]|\bConsole\.Write(?:Line|line)?\("),
        ("java", r"^import (?:java|com|org)\.|\bpublic (?:static void main|class)\b|\bSystem\.out\."),
        ("cpp", r"^#include\s*[<\"]|\bstd::\w+"),
        ("javascript", r"^(?:const|let) \w+\s*=|^\s*(?:async )?function \w+\(|\bconsole\.log\("),
        ("php", r"^<\?php"),
        ("terraform", r'^(?:resource|provider|variable) "[^"]+"'),
        ("http", r"^(?:GET|POST|PUT|DELETE|PATCH|HEAD) \S+ HTTP/"),
        ("ini", r"^\[[\w. -]+\]\s*\n\w+\s*="),
    ]
    for name, pattern in signatures:
        if re.search(pattern, sample[:10000], re.M):
            return name
    return "text"


def _code_row(fragments, base, cell):
    """Prefer complete glyph runs over clipped duplicates at the same coordinates."""
    result = ""
    right = -1.
    for e in sorted(fragments, key=lambda v: (round(v["bbox"][0], 1), -v["bbox"][2])):
        x0, _, x1, _ = e["bbox"]
        if x1 <= right + .25:
            continue
        text = _raw(e)
        col = max(0, round((x0 - base) / cell))
        if x0 >= right - .25:
            result += " " * max(0, col - len(result)) + text
        elif col + len(text) > len(result):
            result += text[len(result) - col:]
        right = max(right, x1)
    return result, right


def _wrapped_code(left, right):
    if not left or not right or right[0].isspace() or left.rstrip().endswith(("\\", ";", "{", "}")):
        return False
    if re.match(r"^(?:[{}\[\]]\s*[,;]?\s*$|//|#|(?:sudo|curl|export|return|import|class|def|const|let|var|echo|if|else)\b)", right):
        return False
    # The template hard-wraps long tokens at the last available monospace cell.
    return bool(re.search(r"\S$", left) and re.match(r"[a-z0-9/_.?=&%+:,-]", right)
                or left.endswith(" ") and right[0].islower())


def _code(events):
    base = min(e["bbox"][0] for e in events)
    size = median(_size(e) for e in events)
    cell = size * .6
    rows = []
    page_offset = 0
    last_page = None
    last_rect = None
    for e in events:
        rect = e.get("code_rect")
        y = _baseline(e)
        if e["page"] != last_page:
            if rows and rect and last_rect and abs((rect[3] - rect[1]) - (last_rect[3] - last_rect[1])) < 2:
                page_offset += last_rect[1] - rect[1]
            elif rows:
                page_offset = rows[-1][0] + size * 1.5 - y
            last_page, last_rect = e["page"], rect
        yy = y + page_offset
        if rows and abs(yy - rows[-1][0]) < 1.7:
            rows[-1][1].append(e)
        else:
            rows.append((yy, [e]))
    increments = [round(b[0]-a[0], 1) for a, b in zip(rows, rows[1:]) if .9 * size < b[0]-a[0] < 1.85 * size]
    leading = Counter(increments).most_common(1)[0][0] if increments else size * 1.5
    lines = []
    previous_y = None
    full = False
    for y, fragments in rows:
        value, end = _code_row(fragments, base, cell)
        gap = 1 if previous_y is None else max(1, round((y - previous_y) / leading))
        if full and gap == 1 and _wrapped_code(lines[-1], value):
            lines[-1] += value
        else:
            lines.extend([""] * min(30, gap - 1))
            lines.append(value)
        rect = fragments[0].get("code_rect")
        full = bool(rect and 0 <= rect[2] - (base - rect[0]) - end < cell * 1.16)
        previous_y = y
    body = "\n".join(lines)
    fence = _fence(body)
    return f"{fence}{_code_language(body)}\n{body}\n{fence}"


def _spans(e, skip=0):
    spans = e.get("spans") or [{"text": e.get("text", "")}]
    result = []
    for s in spans:
        text = s.get("text", "")
        if skip:
            n = min(skip, len(text))
            skip -= n
            text = text[n:]
        if not text:
            continue
        if "inline_image" in s:
            result.append(("image", s["inline_image"]))
            continue
        style = span_style(s)
        # normalize_text may trim boundaries. Those boundaries matter between English font runs.
        parts = re.match(r"^(\s*)(.*?)(\s*)$", text, re.S)
        value = text if style.endswith("code") else parts[1] + normalize_text(parts[2]) + parts[3]
        result.append((style, value))
    return result


def _sep(left, right):
    if not left or not right or left[-1].isspace() or right[0].isspace():
        return ""
    a, b = left[-1], right[0]
    if CJK.match(a) or CJK.match(b) or b in ".,;:?!)]}'’" or a in "([{/-":
        return ""
    if re.search(r"(?:https?://|www\.)\S+$", left, re.I):
        word = right.split()[0]
        if a in "./?=#&%_:" or b in "./?=#&%_" or "/" in word:
            return ""
    return " "


def _punct(ch):
    return ch in punctuation or unicodedata.category(ch).startswith(("P", "S"))


def _emphasize(style, text, before, after, adjacent):
    marker, tags = EMPHASIS[style]
    # CommonMark cannot open * after a word and before punctuation, or close it
    # after punctuation and before a word. Glued emphasis markers can also be
    # read as one delimiter run with different nesting. Keep their exact spacing.
    can_open = not _punct(text[0]) or before.isspace() or _punct(before)
    can_close = not _punct(text[-1]) or after.isspace() or _punct(after)
    if can_open and can_close and not adjacent:
        return marker + text + marker
    for tag in reversed(tags):
        text = f"<{tag}>{text}</{tag}>"
    return text


def _format(spans):
    runs = []
    for style, value in spans:
        if runs and style == runs[-1][0] and style != "image":
            runs[-1][1] += value
        elif value:
            runs.append([style, value])
    result = []
    for i, (style, text) in enumerate(runs):
        prev = runs[i-1][1][-1] if i else " "
        nxt = runs[i+1][1][0] if i+1 < len(runs) else " "
        if style == "image":
            if result and not result[-1][-1].isspace():
                result.append(" ")
            result.append(text)
            if not nxt.isspace():
                result.append(" ")
            continue
        match = re.match(r"^(\s*)(.*?)(\s*)$", text, re.S)
        left, val, right = match.groups()
        if val and style.endswith("code"):
            fence = _fence(val, 1)
            pad = " " if val.startswith("`") or val.endswith("`") else ""
            val = fence + pad + val + pad + fence
            style = style.removesuffix("code")
        else:
            val = re.sub(r"([\\*`])", r"\\\1", val)
            val = re.sub(r"<(?=[A-Za-z/!?])", "&lt;", val)
        if val and style in EMPHASIS:
            before, after = left[-1:] or prev, right[:1] or nxt
            adjacent = ((i and not before.isspace() and runs[i-1][0].removesuffix("code") in EMPHASIS)
                        or (i+1 < len(runs) and not after.isspace() and runs[i+1][0].removesuffix("code") in EMPHASIS))
            val = _emphasize(style, val, before, after, adjacent)
        result.append(left + val + right)
    return "".join(result).strip()


def _marker(e):
    raw = _raw(e)
    m = MARKER.match(raw)
    if e.get("bullet") and not m:
        return "-", 0, e["bbox"][0]
    if not m:
        return None, 0, e["bbox"][0]
    label = m[1] or "-"
    used = 0
    x = e["bbox"][0]
    for s in e.get("spans", ()):
        length = len(s.get("text", ""))
        if used + length > m.end():
            x = s.get("bbox", e["bbox"])[0] + max(0, m.end() - used) * s.get("size", _size(e)) * .51
            break
        x = s.get("bbox", e["bbox"])[2]
        used += length
    else:
        if not e.get("spans"):
            x += m.end() * _size(e) * .51
    return label, m.end(), x


@dataclass
class Block:
    x: float
    md: str
    marker: str = ""
    heading: bool = False
    children: list = field(default_factory=list)


def _prose_continues(prev, current, x, language):
    if abs(x - current["bbox"][0]) > max(3, .45 * _size(prev)):
        return False
    if abs(_size(prev) - _size(current)) > 1.2:
        return False
    if prev["page"] != current["page"]:
        return (current["page"] == prev["page"] + 1
                and prev["bbox"][3] > .85 * prev.get("page_height", 842)
                and current["bbox"][1] < .16 * current.get("page_height", 842)
                and not re.search(r"[。！？.!?:：]\s*$", _raw(prev)))
    delta = _baseline(current) - _baseline(prev)
    return 0 < delta < _size(prev) * 1.56


def _is_code(e):
    if any(s.get("inline_image") for s in e.get("spans", ())):
        return False
    if e.get("code_rect"):
        return True
    spans = [s for s in e.get("spans", ()) if s.get("text", "").strip()]
    return bool(spans) and all(_is_mono(s) for s in spans)


def _blocks(events, language, in_notice=False):
    result = []
    i = 0
    while i < len(events):
        e = events[i]
        i += 1
        kind, box = e["kind"], e["bbox"]
        if e.get("notice_rect") and not in_notice:
            group = [e]
            while i < len(events) and _same_panel(group[-1], events[i], "notice_rect"):
                if group[-1]["page"] != events[i]["page"] and NOTE.match(_raw(events[i]).strip()):
                    break
                group.append(events[i])
                i += 1
            body = _render(_tree(_blocks(group, language, True)))
            quoted = "\n".join(("> " + s) if s else ">" for s in body.splitlines())
            result.append(Block(e["notice_rect"][0], quoted))
        elif kind == "heading":
            anchor = escape(str(e["anchor"]), quote=True)
            level = max(1, min(6, int(e["level"])))
            result.append(Block(box[0], f'<a id="{anchor}"></a>\n\n{"#" * level} {e["title"]}', heading=True))
        elif kind in ("image", "table"):
            if kind == "table":
                from pdfmd_tables import render_table
                md = render_table(e)
            else:
                md = e["md"]
            if md:
                result.append(Block(box[0], md))
        elif kind == "line" and _is_code(e):
            group = [e]
            while i < len(events):
                n = events[i]
                if n["kind"] != "line" or not _is_code(n) or (n.get("notice_rect") and not in_notice):
                    break
                if e.get("code_rect") or n.get("code_rect"):
                    if not _same_panel(group[-1], n, "code_rect"):
                        break
                elif (group[-1]["page"] == n["page"] and
                      _baseline(n) - _baseline(group[-1]) > 3 * _size(n)):
                    break
                group.append(n)
                i += 1
            result.append(Block(e.get("code_rect", box)[0], _code(group)))
        elif kind == "line" and _raw(e).strip():
            marker, skip, x = _marker(e)
            spans = _spans(e, skip)
            prev = e
            while i < len(events):
                n = events[i]
                if (n["kind"] != "line" or _is_code(n) or (n.get("notice_rect") and not in_notice)
                    or _marker(n)[0] or not _prose_continues(prev, n, x, language)):
                    break
                following = _spans(n)
                if not following:
                    break
                if spans:
                    sep = _sep(spans[-1][1], following[0][1])
                    if sep:
                        spans.append((spans[-1][0] if following[0][0] == spans[-1][0] else "", sep))
                spans.extend(following)
                i += 1
                prev = n
            md = _format(spans)
            if in_notice and NOTE.fullmatch(md):
                md = "**" + md + "**"
            if md or marker:
                result.append(Block(x, md, marker or ""))
    return result


def _tree(blocks):
    roots, stack = [], []
    for b in blocks:
        if b.heading:
            stack.clear()
        else:
            while stack:
                delta = b.x - stack[-1].x
                if delta > 4 or (not b.marker and delta >= -4):
                    break
                stack.pop()
        (stack[-1].children if stack else roots).append(b)
        if b.marker:
            stack.append(b)
    return roots


def _order(label):
    if not label or label == "-" or label.isdigit():
        return None, 0
    lower = label.lower()
    if all(c in ROMAN for c in lower):
        values = [ROMAN[c] for c in lower]
        number = sum(-v if j + 1 < len(values) and v < values[j + 1] else v for j, v in enumerate(values))
        return ("I" if label.isupper() else "i"), number
    return ("A" if label.isupper() else "a"), ord(lower) - ord("a") + 1


def _indent(md, n):
    return "\n".join(" " * n + l if l else "" for l in md.split("\n"))


def _render(blocks):
    parts = []
    i = 0
    while i < len(blocks):
        b = blocks[i]
        typ, start = _order(b.marker)
        if typ:
            attr = f' start="{start}"' if start != 1 else ""
            items = [f'<ol type="{typ}"{attr}>']
            expected = start
            while i < len(blocks):
                child = blocks[i]
                next_type, number = _order(child.marker)
                if next_type != typ:
                    break
                attr = f' value="{number}"' if number != expected else ""
                items.append(f"<li{attr}>")
                items.append(child.md)
                if child.children:
                    items.append(_render(child.children))
                items.append("</li>")
                expected = number + 1
                i += 1
            items.append("</ol>")
            parts.append("\n\n".join(items))
        else:
            i += 1
            prefix = (b.marker + (". " if b.marker.isdigit() else " ")) if b.marker else ""
            md = prefix + b.md
            if b.children:
                md += "\n\n" + _indent(_render(b.children), len(prefix))
            parts.append(md)
    return "\n\n".join(parts)


def render_body(events, language):
    """Return Markdown; numbering restarts, notices, and code survive page changes."""
    return _render(_tree(_blocks(list(events), language))).strip() + "\n"
