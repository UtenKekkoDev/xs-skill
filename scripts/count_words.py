"""Count letter and number characters in a UTF-8 fiction body, without headings."""

import argparse
import json
import unicodedata
from pathlib import Path


def count_body(text):
    return sum(unicodedata.category(char)[0] in {"L", "N"} for char in text)


def main():
    parser = argparse.ArgumentParser(
        description="Count body-only UTF-8 text: include letters/numbers; exclude punctuation/space."
    )
    parser.add_argument("path", type=Path)
    parser.add_argument("--min", type=int, dest="minimum")
    parser.add_argument("--max", type=int, dest="maximum")
    args = parser.parse_args()
    if args.minimum is not None and args.minimum < 0:
        parser.error("--min must be nonnegative")
    if args.maximum is not None and args.maximum < 0:
        parser.error("--max must be nonnegative")
    if args.minimum is not None and args.maximum is not None and args.minimum > args.maximum:
        parser.error("--min must not exceed --max")
    total = count_body(args.path.read_text(encoding="utf-8-sig"))
    passed = (args.minimum is None or total >= args.minimum) and (
        args.maximum is None or total <= args.maximum
    )
    print(json.dumps({
        "body_characters": total,
        "minimum": args.minimum,
        "maximum": args.maximum,
        "within_range": passed,
        "counting_rule": "Unicode letters and numbers; body-only input; headings must be removed beforehand"
    }, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
