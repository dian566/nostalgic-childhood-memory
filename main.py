#!/usr/bin/env python3
"""Write the nostalgic childhood-memory entry to /output/entry.txt."""

import os

ENTRY = (
    "Grandma's kitchen smelled of fresh rice at dusk, and I would sit on the "
    "cold tile floor waiting for her to sneak me the crispy bottom of the pot "
    "before dinner was ready."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
