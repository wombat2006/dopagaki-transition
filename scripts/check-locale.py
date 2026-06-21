#!/usr/bin/env python3
"""Validate repository text against meta/locale-policy.json."""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "meta" / "locale-policy.json"

# Appended when allow.emoji == "all"
EMOJI_RANGES: list[tuple[str, str, str]] = [
    ("emoji-misc-technical", "0x2300", "0x23FF"),
    ("emoji-misc-symbols", "0x2600", "0x27BF"),
    ("emoji-misc-arrows", "0x2B00", "0x2BFF"),
    ("emoji-variation-selectors", "0xFE00", "0xFE0F"),
    ("emoji-smp", "0x1F000", "0x1FFFF"),
    ("emoji-zwj", "0x200D", "0x200D"),
    ("emoji-keycap", "0x20E3", "0x20E3"),
    ("emoji-tags", "0xE0020", "0xE007F"),
]


def parse_hex(value: str) -> int:
    return int(value, 16)


def load_policy(path: pathlib.Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def build_allowed_ranges(policy: dict) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []

    for cp in policy.get("allow", {}).get("codepoints", []):
        value = parse_hex(cp)
        ranges.append((value, value))

    for item in policy.get("allow", {}).get("ranges", []):
        ranges.append((parse_hex(item["start"]), parse_hex(item["end"])))

    if policy.get("allow", {}).get("emoji") == "all":
        for _, start, end in EMOJI_RANGES:
            ranges.append((parse_hex(start), parse_hex(end)))

    return ranges


def build_deny(policy: dict) -> tuple[set[str], tuple[str, ...], list[tuple[int, int]]]:
    deny = policy.get("deny", {})
    chars = set(deny.get("characters", []))
    phrases = tuple(deny.get("phrases", []))
    ranges = [
        (parse_hex(item["start"]), parse_hex(item["end"]))
        for item in deny.get("ranges", [])
    ]
    return chars, phrases, ranges


def allowed(cp: int, allowed_ranges: list[tuple[int, int]]) -> bool:
    return any(lo <= cp <= hi for lo, hi in allowed_ranges)


def denied_codepoint(
    cp: int,
    deny_ranges: list[tuple[int, int]],
) -> bool:
    return any(lo <= cp <= hi for lo, hi in deny_ranges)


def iter_text_files(root: pathlib.Path, policy: dict) -> list[pathlib.Path]:
    targets = policy["targets"]
    extensions = {ext.lower() for ext in targets["extensions"]}
    exclude = set(targets.get("exclude_paths", []))
    exclude_files = set(targets.get("exclude_files", []))
    files: list[pathlib.Path] = []

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = str(path.relative_to(root))
        if rel in exclude_files:
            continue
        if any(part in exclude for part in path.parts):
            continue
        if path.suffix.lower() in extensions:
            files.append(path)
    return files


def check_file(
    path: pathlib.Path,
    allowed_ranges: list[tuple[int, int]],
    deny_chars: set[str],
    deny_phrases: tuple[str, ...],
    deny_ranges: list[tuple[int, int]],
    default_action: str,
) -> tuple[list[str], list[str]]:
    rel = str(path.relative_to(ROOT))
    text = path.read_text(encoding="utf-8")
    range_errors: list[str] = []
    deny_errors: list[str] = []

    for lineno, line in enumerate(text.splitlines(), 1):
        for col, ch in enumerate(line, 1):
            cp = ord(ch)
            is_allowed = allowed(cp, allowed_ranges)
            if default_action == "deny" and not is_allowed:
                range_errors.append(f"{rel}:{lineno}:{col} U+{cp:04X} {ch!r}")
                continue
            if is_allowed and ch in deny_chars:
                deny_errors.append(f"{rel}:{lineno}:{col} U+{cp:04X} {ch!r}")
            if is_allowed and denied_codepoint(cp, deny_ranges):
                deny_errors.append(f"{rel}:{lineno}:{col} U+{cp:04X} {ch!r}")

        for phrase in deny_phrases:
            start = 0
            while True:
                idx = line.find(phrase, start)
                if idx == -1:
                    break
                deny_errors.append(f"{rel}:{lineno}:{idx + 1} phrase {phrase!r}")
                start = idx + 1

    return range_errors, deny_errors


def main() -> int:
    policy = load_policy(POLICY_PATH)
    allowed_ranges = build_allowed_ranges(policy)
    deny_chars, deny_phrases, deny_ranges = build_deny(policy)
    default_action = policy.get("default", "deny")

    range_errors: list[str] = []
    deny_errors: list[str] = []

    for path in iter_text_files(ROOT, policy):
        re_errs, de_errs = check_file(
            path,
            allowed_ranges,
            deny_chars,
            deny_phrases,
            deny_ranges,
            default_action,
        )
        range_errors.extend(re_errs)
        deny_errors.extend(de_errs)

    if range_errors:
        print("Disallowed code points:")
        for err in range_errors:
            print(f"  {err}")
    else:
        print("Code point check: OK")

    if deny_errors:
        print("Denylist hits:")
        for err in deny_errors:
            print(f"  {err}")
    else:
        print("Denylist check: OK")

    return 1 if range_errors or deny_errors else 0


if __name__ == "__main__":
    sys.exit(main())
