#!/usr/bin/env python3
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

_BOUNDS_RE = re.compile(r"^\[(\d+),(\d+)\]\[(\d+),(\d+)\]$")


def _bounds(node):
    match = _BOUNDS_RE.match(node.attrib.get("bounds", ""))
    if not match:
        return None
    x1, y1, x2, y2 = map(int, match.groups())
    if x2 <= x1 or y2 <= y1:
        return None
    return x1, y1, x2, y2


def _text(node) -> str:
    return (node.attrib.get("text", "") + " " + node.attrib.get("content-desc", "")).strip()


def _center(rect):
    x1, y1, x2, y2 = rect
    return (x1 + x2) // 2, (y1 + y2) // 2


def _area(rect) -> int:
    x1, y1, x2, y2 = rect
    return (x2 - x1) * (y2 - y1)


def _overlaps(a, b) -> bool:
    return min(a[2], b[2]) > max(a[0], b[0]) and min(a[3], b[3]) > max(a[1], b[1])


def _contains(rect, point) -> bool:
    x1, y1, x2, y2 = rect
    x, y = point
    return x1 <= x <= x2 and y1 <= y <= y2


def _safe_point(clickable, overlays):
    x1, y1, x2, y2 = clickable
    width, height = x2 - x1, y2 - y1
    fractions = (0.5, 0.05, 0.95, 0.15, 0.85)
    points = [
        (int(x1 + width * fx), int(y1 + height * fy))
        for fy in fractions
        for fx in fractions
    ]
    cx, cy = _center(clickable)
    points.sort(key=lambda point: (point[0] - cx) ** 2 + (point[1] - cy) ** 2)
    for point in points:
        if not any(_contains(overlay, point) for overlay in overlays):
            return point
    raise ValueError("matching clickable is fully covered by the label")


def find_click_target(path: pathlib.Path | str, needle: str) -> tuple[int, int]:
    root = ET.parse(path).getroot()
    needle_l = needle.lower()
    nodes = list(root.iter("node"))
    matches = [
        (node, _bounds(node))
        for node in nodes
        if needle_l in _text(node).lower() and _bounds(node)
    ]
    if not matches:
        raise ValueError(f"node not found: {needle}")

    direct = [(node, rect) for node, rect in matches if node.attrib.get("clickable") == "true"]
    if direct:
        _, rect = min(direct, key=lambda item: _area(item[1]))
        return _center(rect)

    overlays = [rect for _, rect in matches]
    nearby = []
    for node in nodes:
        rect = _bounds(node)
        if node.attrib.get("clickable") != "true" or rect is None:
            continue
        if any(_overlaps(rect, overlay) for overlay in overlays):
            nearby.append((node, rect))
    if not nearby:
        raise ValueError(f"no clickable target overlaps: {needle}")

    _, clickable = min(nearby, key=lambda item: _area(item[1]))
    return _safe_point(clickable, overlays)


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(f"usage: {argv[0]} <ui.xml> <label>", file=sys.stderr)
        return 2
    try:
        x, y = find_click_target(argv[1], argv[2])
    except (OSError, ET.ParseError, ValueError) as exc:
        print(f"CLICK_TARGET_ERROR={exc}", file=sys.stderr)
        return 1
    print(x, y)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
