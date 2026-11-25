#!/usr/bin/env python3
# Nostalgic childhood-memory entry writer for the make.fun bounty.
# Emits one sentence (169 characters) to /output/entry.txt, byte-exact.
# The line below must stay identical: the judge scores this exact text.

from pathlib import Path

MEMORY_LINE = (
    "Grandma's kitchen smelled of fresh rice at dusk, and I would sit on the "
    "cold tile floor waiting for her to sneak me the crispy bottom of the pot "
    "before dinner was ready."
)


def write_entry() -> Path:
    target = Path("/output") / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(MEMORY_LINE, encoding="utf-8")
    return target


if __name__ == "__main__":
    write_entry()
