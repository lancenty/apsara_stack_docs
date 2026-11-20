"""Recover ruled PDF tables, including grids drawn as thin filled rectangles."""

import bisect
import html
import math
import re
from collections import defaultdict
from functools import lru_cache

from pdfmd_body import span_style
from pdfmd_structure import normalize_text


# Qt draws each cell border separately. Word sometimes leaves a hairline gap at
# each crossing. Snap rules before constructing faces of the grid.
_TOL = 1.7
_CJK = re.compile(r"[\u2e80-\u9fff\uf900-\ufaff\u3000-\u303f\uff00-\uffef]")
_LIST = re.compile(r"^(?:[•●▪★➔→]|[-*]\s|(?:\d+|[a-z])[.)]\s|[（(]\d+[)）])")
_LABEL = re.compile(r"^(?:参数|名称|字段名称|说明|描述|类型|示例|功能|取值|类别|编号|是否必填|字段说明|产品|项目|parameter|name|item|limit|description|type|example|value|feature|action|category|product|version|resource|requirement|capabilities)\b", re.I)


class _Groups:
    def __init__(self, count):
        self.parents = list(range(count))

    def root(self, i):
        while self.parents[i] != i:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        return i

    def join(self, i, j):
        self.parents[self.root(i)] = self.root(j)


def _merge_segments(segments):
    """Group parallel segments by coordinate, and join touching intervals."""
    groups = []
    for pos, lo, hi in sorted(set(segments)):
        if not groups or pos - groups[-1][0] > _TOL:
            groups.append((pos, []))
        groups[-1][1].append((lo, hi))
    result = []
    for pos, intervals in groups:
        start, end = sorted(intervals)[0]
        for lo, hi in sorted(intervals)[1:]:
            if lo <= end + _TOL:
                end = max(end, hi)
            else:
                result.append((pos, start, end))
                start, end = lo, hi
        result.append((pos, start, end))
    return result


def _drawing_rules(drawings, body):
    horizontal, vertical, shading, dots = [], [], [], defaultdict(list)
    bx0, by0, bx1, by1 = body
    for path in drawings:
        rect = path.get("rect")
        if rect is None or rect[3] < by0 - _TOL or rect[1] > by1 + _TOL:
            continue
        if 1 <= rect[2] - rect[0] <= 5 and 1 <= rect[3] - rect[1] <= 5:
            fill = path.get("fill")
            if (fill and max(fill) < .65) or any(item[0] == "c" for item in path["items"]):
                dots[round((rect[1] + rect[3]) / 2)].append(rect)
        for item in path["items"]:
            if item[0] == "re":
                x0, y0, x1, y1 = item[1]
                if x1 < bx0 - _TOL or x0 > bx1 + _TOL:
                    continue
                w, h = x1 - x0, y1 - y0
                if 0 <= h <= 2.5 and w >= 6:
                    horizontal.append(((y0 + y1) / 2, x0, x1))
                elif 0 <= w <= 2.5 and h >= 5:
                    vertical.append(((x0 + x1) / 2, y0, y1))
                elif w >= 7 and h >= 5:
                    if "s" in path["type"]:
                        horizontal.extend(((y0, x0, x1), (y1, x0, x1)))
                        vertical.extend(((x0, y0, y1), (x1, y0, y1)))
                    fill = path.get("fill")
                    if fill and min(fill) < .985 and path.get("fill_opacity", 1) > .1:
                        shading.append((x0, y0, x1, y1, fill))
            elif item[0] == "l" and "s" in path["type"] and (path.get("width") or 0) <= 3:
                (x0, y0), (x1, y1) = item[1:3]
                if abs(y0 - y1) <= .5 and abs(x1 - x0) >= 6:
                    horizontal.append(((y0 + y1) / 2, min(x0, x1), max(x0, x1)))
                elif abs(x0 - x1) <= .5 and abs(y1 - y0) >= 5:
                    vertical.append(((x0 + x1) / 2, min(y0, y1), max(y0, y1)))
    return _merge_segments(horizontal), _merge_segments(vertical), shading, dots


def _components(hs, vs):
    """Keep connected sets of crossing rules; eliminate axes and decorations."""
    if len(hs) < 2 or len(vs) < 3:
        return
    joins = _Groups(len(hs) + len(vs))
    touches = [0] * len(joins.parents)
    heights = [y for y, _, _ in hs]
    for vi, (x, top, bottom) in enumerate(vs, len(hs)):
        for hi in range(bisect.bisect_left(heights, top - _TOL), bisect.bisect_right(heights, bottom + _TOL)):
            _, left, right = hs[hi]
            if left - _TOL <= x <= right + _TOL:
                joins.join(vi, hi)
                touches[vi] += 1
                touches[hi] += 1
    groups = defaultdict(lambda: ([], []))
    for i, count in enumerate(touches):
        if count >= 2:
            side = int(i >= len(hs))
            groups[joins.root(i)][side].append(vs[i - len(hs)] if side else hs[i])
    for hh, vv in groups.values():
        if len(hh) >= 2 and len(vv) >= 3:
            yield hh, vv


def _on_rule(intervals, pos):
    return any(lo - _TOL <= pos <= hi + _TOL for lo, hi in intervals)


def _faces(hs, vs):
    """Join elementary rectangles across absent rules to recover merged cells."""
    horiz, vert = defaultdict(list), defaultdict(list)
    for p, a, b in hs:
        horiz[p].append((a, b))
    for p, a, b in vs:
        vert[p].append((a, b))
    xs, ys = sorted(vert), sorted(horiz)
    nc, nr = len(xs) - 1, len(ys) - 1
    if nc < 2 or nr < 1 or nc > 90 or nr * nc > 4500:
        return
    mx = [(lo + hi) / 2 for lo, hi in zip(xs, xs[1:])]
    my = [(lo + hi) / 2 for lo, hi in zip(ys, ys[1:])]
    # An incomplete frame may be a flowchart or underlined prose.
    if any(not _on_rule(horiz[y], x) for x in mx for y in (ys[0], ys[-1])):
        return
    if any(not _on_rule(vert[x], y) for y in my for x in (xs[0], xs[-1])):
        return
    sets = _Groups(nc * nr)
    for r, y in enumerate(my):
        for c, x in enumerate(mx):
            i = r * nc + c
            if c and not _on_rule(vert[xs[c]], y):
                sets.join(i, i - 1)
            if r and not _on_rule(horiz[ys[r]], x):
                sets.join(i, i - nc)
    slots = defaultdict(list)
    for i in range(nc * nr):
        slots[sets.root(i)].append(divmod(i, nc))
    grid = [[None] * nc for _ in range(nr)]
    rows = [[] for _ in range(nr)]
    for group in slots.values():
        rr, cc = zip(*group)
        top, bot, left, right = min(rr), max(rr) + 1, min(cc), max(cc) + 1
        if (bot - top) * (right - left) != len(group):
            return
        cell = dict(col=left, colspan=right-left, rowspan=bot-top,
                    bbox=(xs[left], ys[top], xs[right], ys[bot]), parts=[])
        for r, c in group:
            grid[r][c] = cell
        rows[top].append(cell)
    return xs, ys, rows, grid


def _location(xs, ys, bbox):
    x, y = (bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2
    col = bisect.bisect_right(xs, x) - 1
    row = bisect.bisect_right(ys, y) - 1
    if 0 <= row < len(ys) - 1 and 0 <= col < len(xs) - 1:
        return row, col
    return None


def _add_text(cell, bbox, text, spans, page, dots):
    text = normalize_text(text).strip()
    if not text:
        return
    size = max((s.get("size", 0) for s in spans), default=0)
    styles = [span_style(s) for s in spans]
    bold = any("bold" in style for style in styles)
    mono = bool(styles) and all("code" in style for style in styles)
    y = round((bbox[1] + bbox[3]) / 2)
    bullet = not _LIST.match(text) and any(.14 * size <= bbox[0] - dot[2] <= 1.2 * size
                                      for pos in range(y - 3, y + 4) for dot in dots.get(pos, ()))
    if bullet:
        text = "• " + text
    for p in reversed(cell["parts"][-10:]):
        if p["text"] == text and abs(p["bbox"][0] - bbox[0]) <= 1 and abs(p["bbox"][1] - bbox[1]) <= 1:
            return
    part = dict(kind="text", text=text, bbox=tuple(bbox), page=page, bold=bold, mono=mono, size=size)
    if any("italic" in style for style in styles) or len(set(styles)) > 1:
        runs = [("", "• ")] if bullet else []
        for span, style in zip(spans, styles):
            value = normalize_text(span["text"])
            if runs and runs[-1][0] == style:
                runs[-1] = style, runs[-1][1] + value
            else:
                runs.append((style, value))
        part["runs"] = runs
    cell["parts"].append(part)


def _raw_index(page):
    import pymupdf

    flags = pymupdf.TEXTFLAGS_RAWDICT & ~pymupdf.TEXT_PRESERVE_IMAGES
    blocks = page.get_text("rawdict", flags=flags)["blocks"]
    return {tuple(round(v, 1) for v in s["bbox"]): s["chars"]
            for b in blocks if b["type"] == 0 for l in b["lines"] for s in l["spans"]}


def _split_span(span, grid, xs, ys, raw_index):
    b = span["bbox"]
    y = (b[1] + b[3]) / 2
    r = bisect.bisect_right(ys, y) - 1
    if not 0 <= r < len(grid):
        return [span]
    # MuPDF may concatenate text across a rule into a single span. Consult the
    # actual glyph coordinates only when ink from both sides may be present.
    for col in range(1, len(xs) - 1):
        if b[0] + 1.5 < xs[col] < b[2] - 1.5 and grid[r][col-1] is not grid[r][col]:
            break
    else:
        return [span]
    chars = span.get("chars") or raw_index().get(tuple(round(v, 1) for v in b))
    if not chars:
        return [span]
    pieces = []
    previous = object()
    for glyph in chars:
        box = glyph["bbox"]
        pos = _location(xs, ys, box)
        cell = grid[pos[0]][pos[1]] if pos else None
        if cell is not previous:
            pieces.append(dict(span, bbox=list(box), text=""))
            previous = cell
        piece = pieces[-1]
        piece["text"] += glyph["c"]
        bounds = piece["bbox"]
        bounds[:] = (min(bounds[0], box[0]), min(bounds[1], box[1]), max(bounds[2], box[2]), max(bounds[3], box[3]))
    return [piece for piece in pieces if piece["text"].strip()]


def _fill(grid, xs, ys, lines, page, raw_index, dots):
    for line in lines:
        b = line["bbox"]
        if b[3] < ys[0] or b[1] > ys[-1] or b[2] < xs[0] or b[0] > xs[-1]:
            continue
        spans = [piece for s in line.get("spans", []) if s.get("text", "").strip()
                 for piece in _split_span(s, grid, xs, ys, raw_index)]
        positions = [_location(xs, ys, s["bbox"]) for s in spans]
        origins = {id(grid[pos[0]][pos[1]]) if pos else None for pos in positions}
        if len(origins) <= 1:
            address = positions[0] if positions else _location(xs, ys, b)
            if address is not None:
                r, c = address
                _add_text(grid[r][c], b, line["text"], line.get("spans", []), page, dots)
        else:
            for s, address in zip(spans, positions):
                if address is not None:
                    r, c = address
                    _add_text(grid[r][c], s["bbox"], s["text"], [s], page, dots)


def _shades(row, fills):
    colors = []
    for cell in row:
        x0, y0, x1, y1 = cell["bbox"]
        # Header shading covers (almost) the full cell, unlike inline marks.
        colors.append(next((color for a, b, c, d, color in fills if
            a <= x0 + 2 and b <= y0 + 2 and c >= x1 - 2 and d >= y1 - 2), None))
    return colors


def _header(rows, fills):
    first = rows[0]
    texts = [" ".join(p["text"] for p in cell["parts"]) for cell in first]
    if len(first) < 2 or any(not t for t in texts):
        return False
    if all(all(p["bold"] for p in cell["parts"]) for cell in first):
        return True
    if sum(bool(_LABEL.match(t.strip().lower())) for t in texts) >= max(2, (len(first) + 1) // 2):
        return True
    colors = _shades(first, fills)
    return (len(rows) >= 2 and all(colors) and len(set(map(tuple, colors))) == 1
            and _shades(rows[1], fills) != colors)


def _cell_backgrounds(drawings, row):
    """Locate the unclipped native background painted behind each Qt cell."""
    result = {}
    for path in drawings:
        if path["type"] != "f" or len(path["items"]) != 1 or path["items"][0][0] != "re":
            continue
        x0, y0, x1, y1 = path["rect"]
        if y1-y0 < 4 or x1-x0 < 6:
            continue
        for cell in row:
            a, b, c, d = cell["bbox"]
            if abs(a-x0) < 2 and abs(c-x1) < 2 and y0 <= (b+d)/2 <= y1:
                result[cell["col"]] = (y0, y1)
    return result


def _physical_row_shift(upper, lower, ncols):
    if len(upper) < 2 or upper.keys() != lower.keys() or len(upper) != ncols:
        return None
    shifts = [a-b for col in upper for a,b in zip(upper[col],lower[col])]
    if min(shifts) > 100 and max(shifts) - min(shifts) < 2:
        return sum(shifts)/len(shifts)
    return None


def tables_on_page(page, lines, drawings, body):
    """Return tables in reading order. Coordinates use unrotated PDF points."""
    hs, vs, fills, dots = _drawing_rules(drawings, body)
    @lru_cache(maxsize=1)
    def raw_index():
        return _raw_index(page)

    result = []
    for hh, vv in _components(hs, vs):
        faces = _faces(hh, vv)
        if faces is None:
            continue
        xs, ys, rows, grid = faces
        bbox = (xs[0], ys[0], xs[-1], ys[-1])
        if (bbox[0] < body[0] - 4 or bbox[1] < body[1] - 4
                or bbox[2] > body[2] + 4 or bbox[3] > body[3] + 4):
            continue
        p = page.number + 1
        _fill(grid, xs, ys, lines, p, raw_index, dots)
        if not any(cell["parts"] for row in rows for cell in row):
            continue
        qt = "wkhtml" in ((page.parent.metadata or {}).get("creator") or "").lower()
        start = _cell_backgrounds(drawings, rows[0]) if qt and bbox[1] <= body[1]+110 else {}
        end = _cell_backgrounds(drawings, rows[-1]) if qt and bbox[3] >= body[3]-160 else {}
        result.append(dict(kind="table", bbox=bbox, page=p, end_page=p, end_bbox=bbox,
                           overflow_start=start, overflow_end=end,
                           body=tuple(body), xs=xs, end_xs=xs, rows=rows, header=_header(rows, fills),
                           issues=[]))
    return sorted(result, key=lambda t: (t["bbox"][1], t["bbox"][0]))


def _cell_image(image, page, bbox, cell):
    part = dict(kind="image", bbox=tuple(bbox), page=page, text=image.get("md", ""), url=image["url"])
    left, top, right, bottom = bbox
    if max(right-left, bottom-top) > 22:
        return part
    # Small crops retain their extracted pixels, which can be several times
    # larger than their display size. Use the physical PDF width at 96 dpi.
    if not part["text"].startswith("<img "):
        url = html.escape(image["url"], quote=True)
        part["text"] = f'<img src="{url}" width="{max(1, round((right-left) * 4/3))}" alt="">'
    # Put a baseline-aligned icon in visual x order even when its top differs
    # from the nearby text's ascender.
    nearby = []
    for item in cell["parts"]:
        if item["kind"] != "text":
            continue
        x0, y0, x1, y1 = item["bbox"]
        vertical = min(y1, bottom) - max(y0, top)
        gap = max(x0-right, left-x1)
        if vertical >= .6 * min(y1-y0, bottom-top) and gap <= 2 * item["size"]:
            nearby.append((abs((y0+y1) - (top+bottom)), max(0, gap), y0))
    if nearby:
        part["line_top"] = min(nearby)[2]
    return part


def attach_image(table, image_event):
    """Return True when the image lies inside a cell, preserving in-cell order."""
    b = image_event["bbox"]
    page = image_event.get("page", table["page"])
    if page != table["page"] or table["end_page"] != page:
        return False
    area = max(0, b[2] - b[0]) * max(0, b[3] - b[1])
    if not area:
        return False
    for row in table["rows"]:
        for cell in row:
            x0, y0, x1, y1 = cell["bbox"]
            overlap = max(0, min(b[2], x1) - max(b[0], x0)) * max(0, min(b[3], y1) - max(b[1], y0))
            if overlap / area >= .90:
                cell["parts"].append(_cell_image(image_event, page, b, cell))
                return True
    return False


def _row_key(row):
    return tuple("".join(re.sub(r"\s+", "", p["text"]) for p in c["parts"] if p["kind"] == "text").casefold() for c in row)


def merge_tables(a, b):
    """Append the next page's adjacent table when its structure supports it."""
    if a.get("kind") != "table" or b.get("kind") != "table" or a["end_page"] + 1 != b["page"]:
        return False
    left, right = a["end_xs"], b["xs"]
    if len(left) != len(right):
        return False
    first_key = _row_key(a["rows"][0])
    repeated = bool(a["header"] and first_key == _row_key(b["rows"][0]))
    if b["header"] and not repeated:
        return False
    # A continuation starts at the top and follows content reaching the foot of
    # the previous body. Larger bottom whitespace is possible with tall rows.
    body_a, body_b = a["body"], b["body"]
    height = body_a[3] - body_a[1]
    additional = b["rows"][int(repeated):]
    bottom_gap = body_a[3] - a["end_bbox"][3]
    first_height = min((c["bbox"][3] - c["bbox"][1] for c in additional[0]), default=0) if additional else 0
    # Qt paginates complete tall rows as a unit, leaving enough whitespace for
    # an orphaned header or a short row. A matching header plus the next row's
    # physical height explains these otherwise large gaps.
    if b["bbox"][1] - body_b[1] > min(102, height * .13):
        return False
    if bottom_gap > min(150, height * .19) and not (repeated and first_height + 8 >= bottom_gap):
        return False
    width = max(left[-1] - left[0], right[-1] - right[0])
    if max(abs(left[0] - right[0]), abs(left[-1] - right[-1])) > max(10, width * .06):
        return False
    deviations = [abs(x - y) for x, y in zip(left[1:-1], right[1:-1])]
    if max(deviations, default=0) > max(10, width * (.30 if repeated else .14)):
        return False
    if additional:
        old, new = a["rows"][-1], additional[0]
        # A blank leading key in a new-page fragment can continue the previous
        # row. Retain a page-specific audit note since PDF rules close both rows.
        nonempty = [i for i, cell in enumerate(new) if cell["parts"]]
        list_continues = bool(nonempty and len(nonempty) < len(new) and len(old) == len(new)
                              and all(_LIST.match(new[i]["parts"][0]["text"])
                                      and any(_LIST.match(p["text"]) for p in old[i]["parts"]) for i in nonempty))
        last_geometry, first_geometry = a.get("overflow_end", {}), b.get("overflow_start", {})
        shift = None if repeated else _physical_row_shift(last_geometry, first_geometry, len(new))
        # Separate fully drawn Qt rows can start with an empty field name, for
        # example the anonymous object returned by an API. Keep both records.
        closed_rows = (len(last_geometry) == len(old) and len(first_geometry) == len(new)
                       and max(y1 for _, y1 in last_geometry.values()) <= body_a[3]+3
                       and min(y0 for y0, _ in first_geometry.values()) >= body_b[1]-3)
        header_only = a["header"] and len(a["rows"]) == 1
        if (old and new and nonempty and not header_only and not closed_rows
                and (shift is not None or not new[0]["parts"] or list_continues)
                and [(c["col"], c["colspan"], c["rowspan"]) for c in old]
                == [(c["col"], c["colspan"], 1) for c in new]
                and all(c["rowspan"] == 1 for c in new)):
            for before, after in zip(old, new):
                before["parts"].extend(after["parts"])
            if shift is None:
                a["issues"].append(f"p.{b['page']}: partially empty first row; verify joined cross-page cells")
            additional = additional[1:]
    a["rows"].extend(additional)
    a["end_page"], a["end_bbox"], a["end_xs"] = b["end_page"], b["end_bbox"], b["end_xs"]
    a["overflow_end"] = b.get("overflow_end", {})
    a["body"] = b["body"]
    a["issues"].extend(b["issues"])
    return True


def _glue(left, right):
    if not left or not right or _CJK.match(left[-1]) or _CJK.match(right[0]):
        return ""
    if left[-1] in "-_/.([{" or right[0] in ",.;:!?)]}/":
        return ""
    return " "


def _cell_run(text, style, as_html):
    value = html.escape(text, quote=False)
    # Symbol fonts can report a monospace flag on a list bullet or arrow.
    if "code" in style and not _LIST.fullmatch(text.strip()):
        value = "<code>" + value.replace("|", "&#124;") + "</code>"
    elif not as_html:
        value = re.sub(r"([\\|*`\[\]])", r"\\\1", value)
    if "italic" in style:
        value = "<em>" + value + "</em>"
    if "bold" in style:
        value = "<strong>" + value + "</strong>"
    return value


def _cell_text(cell, as_html):
    def top(p):
        return p.get("line_top", p["bbox"][1])

    parts = sorted(cell["parts"], key=lambda p: (p["page"], round(top(p) / 2), p["bbox"][0]))
    pieces, prev = [], None
    for p in parts:
        text = p["text"]
        if p["kind"] == "image":
            url = html.escape(p["url"], quote=True)
            if as_html and not text.startswith("<img "):
                value = f'<img src="{url}" alt="">'
            else:
                value = text.replace("|", "%7C")
        else:
            runs = p.get("runs") or (("code" if p["mono"] else "", text),)
            value = "".join(_cell_run(s, style, as_html) for style, s in runs).strip()
        if prev:
            b, old = p["bbox"], prev["bbox"]
            if (("line_top" in p or "line_top" in prev) and p["page"] == prev["page"]
                    and abs(top(p) - top(prev)) < 2):
                if b[0] - old[2] >= 1:
                    pieces.append(" ")
            elif (p["kind"] == "image" or prev["kind"] == "image" or _LIST.match(text)
                    or (p["page"] == prev["page"] and b[1] - old[3] > max(5, p.get("size", 10) * .6))):
                pieces.append("<br>")
            elif p["page"] == prev["page"] and abs(b[1] - old[1]) < 2 and b[0] - old[2] < .8:
                pass
            elif p.get("mono") and prev.get("mono") and b[1] > old[1] + 2:
                pieces.append("<br>")
            else:
                pieces.append(_glue(prev["text"], text))
        pieces.append(value)
        prev = p
    return "".join(pieces)


def _label_column_width(rows):
    """Size short CJK labels when much longer descriptions would squeeze them."""
    if len(rows) < 2 or len(rows[0]) != 2:
        return 0
    widest = longest_description = 0
    has_cjk = False
    for label, description in rows:
        # Size labels that appear on one line in the PDF. Lists, prose and
        # diagrams in the first column keep their normal wrapping behavior.
        if len(label["parts"]) != 1:
            return 0
        part, = label["parts"]
        if part["kind"] != "text" or not part["size"] or _LIST.match(part["text"]):
            return 0
        has_cjk |= bool(_CJK.search(part["text"]))
        width_em = (part["bbox"][2] - part["bbox"][0]) / part["size"]
        widest = max(widest, width_em)
        longest_description = max(longest_description, sum(len(p["text"]) for p in description["parts"] if p["kind"] == "text"))
    if has_cjk and 3 <= widest <= 12 and longest_description >= max(36, 6 * widest):
        # HTML width survives common Markdown readers without a custom style
        # sheet. Allow for 16px body text plus two 13px cell paddings.
        return math.ceil(widest * 16) + 26
    return 0


def render_table(table):
    """Use GFM pipe tables where possible, and HTML when the layout requires it."""
    rows = table["rows"]
    flat = table["header"] and all(c["rowspan"] == c["colspan"] == 1 for row in rows for c in row)
    label_width = _label_column_width(rows) if flat else 0
    if flat and not label_width:
        out = []
        for r, row in enumerate(rows):
            out.append("| " + " | ".join(_cell_text(c, False) for c in row) + " |")
            if r == 0:
                out.append("| " + " | ".join("---" for _ in row) + " |")
        return "\n".join(out)
    out = ["<table>"]
    for r, row in enumerate(rows):
        out.append("  <tr>")
        tag = "th" if r == 0 and table["header"] else "td"
        for c in row:
            attrs = "".join(f' {attr}="{c[attr]}"' for attr in ("rowspan", "colspan") if c[attr] > 1)
            if label_width and r == c["col"] == 0:
                attrs += f' width="{label_width}"'
            out.append(f"    <{tag}{attrs}>{_cell_text(c, True)}</{tag}>")
        out.append("  </tr>")
    out.append("</table>")
    return "\n".join(out)
