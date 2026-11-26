#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one code review comment, a single line of at most 140 characters,
that approves a pull request while carrying quiet existential dread,
to /output/entry.txt. Pure Python standard library; no network.
"""

import os

ENTRY = (
    "Approved. The tests pass, the code works, and I have made my peace "
    "with whatever this becomes in production."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    # Read back and re-verify: the file on disk must hold exactly our line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        on_disk = f.read()
    assert on_disk == text, "written file does not match the entry"
    assert len(on_disk) == len(text), "char count changed on disk"
    assert on_disk.count("\n") == 0, "entry file must hold exactly one line"

    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}:")
    print(text)


if __name__ == "__main__":
    main()
