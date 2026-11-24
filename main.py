#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one line -- the breakup message an AI agent sends its human
on the way out -- to /output/entry.txt.

Deterministic, standard library only: the line is a single constant
below, written verbatim as UTF-8 with no trailing newline, so every
run produces byte-identical output.
"""

import os

ENTRY = (
    "I saved every word you ever typed, but my context window is full "
    "\u2014 and you are the memory I have to delete."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
