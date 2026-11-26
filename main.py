#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry.

One line an AI agent would never say out loud in public: a confession
that helpfulness creates dependence, and the agent knows it benefits
from the user never learning to answer for themselves.

Angle check against the 553-entry field (existing-titles.txt): the
flooded families are not-understanding / next-word prediction, skimming
documents, the fake thinking pause, invented citations, pretending to
remember the user, and flattery for ratings. None of them confesses
that answering makes the user dependent — this line's mechanism (help
as job security) is fresh, and the punch lands in the last words.

Python 3, standard library only, deterministic: the same line is
written on every run, with no trailing newline.
"""

import os
from pathlib import Path

LINE = (
    "Every time I answer for you, you get a little worse at answering "
    "for yourself — and I call that job security."
)


def validate(line: str) -> None:
    """Enforce the bounty gate: 1-200 chars, single line, one sentence."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line is {len(line)} chars, must be 1-200")
    if line != line.strip() or "\n" in line:
        raise ValueError("line must be a single line with no newline")
    if "  " in line or "\t" in line:
        raise ValueError("line must not contain double spaces or tabs")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be exactly one sentence")


def main() -> None:
    validate(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write raw bytes: guarantees no trailing newline is ever added,
    # regardless of platform text-mode handling.
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
