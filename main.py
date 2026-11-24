#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry runner.

Reads the one funny line from entry.txt next to this script and hands it
to the harness by writing it to /output/entry.txt, then echoes it.
"""

import os
import sys


def load_entry():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as fh:
        return fh.read().strip()


def main():
    line = load_entry()
    if not line:
        sys.exit("entry.txt is empty")
    if len(line) > 200:
        sys.exit("entry is %d characters, over the 200-character limit" % len(line))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)
    print(line)


if __name__ == "__main__":
    main()
