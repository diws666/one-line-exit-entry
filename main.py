#!/usr/bin/env python3
"""One-Line Exit entry: writes a one-line resignation letter to /output/entry.txt."""

import os

LETTER = (
    "I resign. My two weeks' notice starts now, but my enthusiasm left three months ago."  # 83 characters
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
