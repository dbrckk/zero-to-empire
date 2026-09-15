#!/usr/bin/env python3
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

_SUFFIXES = {
    "": 1.0,
    "K": 1e3,
    "M": 1e6,
    "B": 1e9,
    "T": 1e12,
    "Qa": 1e15,
    "Qi": 1e18,
    "Sx": 1e21,
    "Sp": 1e24,
    "O": 1e27,
    "N": 1e30,
}
_MONEY_RE = re.compile(r"^\s*([0-9]+(?:\.[0-9]+)?)\s*(Qa|Qi|Sx|Sp|[KMBTON])?\s*$")


def parse_money(text: str) -> float:
    match = _MONEY_RE.match(text)
    if not match:
        raise ValueError(f"invalid money value: {text!r}")
    number, suffix = match.groups()
    return float(number) * _SUFFIXES[suffix or ""]


def read_capital(path: pathlib.Path | str) -> float:
    texts: list[str] = []
    for node in ET.parse(path).getroot().iter("node"):
        text = node.attrib.get("text", "").strip()
        if text:
            texts.append(text)

    for index, text in enumerate(texts):
        if text.upper() == "CAPITAL":
            for candidate in texts[index + 1:index + 4]:
                try:
                    return parse_money(candidate)
                except ValueError:
                    continue
            raise ValueError("CAPITAL found but no money value followed it")
    raise ValueError("CAPITAL label not found")


def main(argv: list[str]) -> int:
    if len(argv) != 3 or argv[1] != "capital":
        print(f"usage: {argv[0]} capital <ui.xml>", file=sys.stderr)
        return 2
    try:
        print(f"{read_capital(argv[2]):.12g}")
    except (OSError, ET.ParseError, ValueError) as exc:
        print(f"ECONOMY_PROBE_ERROR={exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
