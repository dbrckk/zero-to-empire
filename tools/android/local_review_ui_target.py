#!/usr/bin/env python3
"""Locate actual Android Compose accessibility controls in uiautomator XML.

Only a review helper; never touches production assets or grants approval.
Usage: python tools/android/local_review_ui_target.py hierarchy.xml "ENGINEER"
Prints: "x y" for adb shell input tap, exiting 1 if not visible/clickable.
"""
from __future__ import annotations
import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

BOUNDS = re.compile(r"^\[(\d+),(\d+)\]\[(\d+),(\d+)\]$")


def find(xml_path: Path, label: str, clickable_only: bool = True) -> tuple[int, int] | None:
    root = ET.parse(xml_path).getroot()
    # A label may also appear in a static header. Only target real controls.
    for node in root.iter("node"):
        actual = (node.attrib.get("text") or node.attrib.get("content-desc") or "").strip()
        if actual != label:
            continue
        parents = []
        # uiautomator sometimes puts "clickable" on a parent Button/View.
        direct = node.attrib.get("clickable") == "true"
        if clickable_only and not direct:
            # A bound of a nested label is still actionable only if a parent
            # Compose semantics node encloses it and is clickable.
            for candidate in root.iter("node"):
                if candidate.attrib.get("clickable") != "true":
                    continue
                pb = BOUNDS.fullmatch(candidate.attrib.get("bounds", ""))
                nb = BOUNDS.fullmatch(node.attrib.get("bounds", ""))
                if not (pb and nb):
                    continue
                pl, pt, pr, pd = map(int, pb.groups())
                nl, nt, nr, nd = map(int, nb.groups())
                if pl <= nl and pt <= nt and pr >= nr and pd >= nd:
                    parents.append((pr-pl)*(pd-pt))
            if not parents:
                continue
        match = BOUNDS.fullmatch(node.attrib.get("bounds", ""))
        if match:
            left, top, right, bottom = map(int, match.groups())
            if right > left and bottom > top:
                return (left+right)//2, (top+bottom)//2
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("xml", type=Path)
    parser.add_argument("label")
    parser.add_argument("--allow-static-label", action="store_true")
    args = parser.parse_args()
    try:
        coord = find(args.xml, args.label, not args.allow_static_label)
    except (ET.ParseError, OSError) as err:
        print(str(err), file=sys.stderr)
        return 1
    if not coord:
        return 1
    print(*coord)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
