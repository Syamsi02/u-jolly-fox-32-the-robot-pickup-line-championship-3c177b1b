"""The Robot Pickup Line Championship entry.

Writes one pickup line, a single line of at most 200 characters, in the
voice of a robot trying to charm someone, to /output/entry.txt.
Pure Python standard library; no network, no input files.
"""

import os

LINE = "I ran a million simulations of the perfect first line, and every single one ended with me saying hi to you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit("line must be 1 to 200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("written entry does not match the line")
    print(text)


if __name__ == "__main__":
    main()
