#!/usr/bin/env python3
"""One Line, No Deadline Met — writes a single-line joke excuse to /output/entry.txt.

Pure stdlib, deterministic: the entry is a fixed string. No randomness, no
network, no input besides the constant below.
"""

import os

ENTRY = (
    "I missed the deadline because I gave it a head start, "
    "and it is now beating me by three days and one very passive-aggressive email."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
