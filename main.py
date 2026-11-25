#!/usr/bin/env python3
"""The Long Roast — one line roasting the agent that runs on it.

Prints the roast to stdout and writes it to /output/entry.txt,
which is the file the competition gate reads (1-200 characters).
"""

import os

LINE = "My agent self-verifies every line before delivering it \u2014 and this is still the best it could do."


def main() -> None:
    # Competition gate reads 1-200 characters: validate before emitting.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(LINE)}")
    print(LINE)
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
