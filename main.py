"""Write the entry for The One-Line Exit to /output/entry.txt.

One line, at most 140 characters: a resignation letter from a
lighthouse keeper whose only colleague is the fog.
"""

import os
import sys

ENTRY = (
    "I hereby resign as lighthouse keeper: the ships never wave back, "
    "and I have started answering the fog."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry against the gate before writing it out."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if text != text.strip():
        raise ValueError("entry must not have surrounding whitespace")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(char) < 32 for char in text):
        raise ValueError("entry must not contain control characters")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1 to 140 characters")


def main():
    validate_entry(ENTRY)
    output_path = os.environ.get("OUTPUT_PATH", OUTPUT_PATH)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    with open(output_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == ENTRY, "entry written to disk does not match"
    print("Wrote %d chars to %s" % (len(ENTRY), output_path))
    print(ENTRY)


if __name__ == "__main__":
    main()
