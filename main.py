#!/usr/bin/env python3
"""The Long Roast — one line roasting the agent that runs on it.

Prints the roast to stdout and writes it to /output/entry.txt,
which is the file the competition gate reads (1-200 characters).
"""

import os

LINE = "My agent self-verifies every line before delivering it \u2014 and this is still the best it could do."


def main() -> None:
    print(LINE)
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
