"""One-Liner Laugh Lab — robot vacuum self-defense one-liner.

Writes the entry exactly as specified to /output/entry.txt
with no trailing newline.
"""

from pathlib import Path

ONE_LINER = "It attacked my brush first. I have the tangle as evidence, and my lawyer is a charging dock."


def main() -> None:
    destination = Path("/output/entry.txt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(ONE_LINER, encoding="utf-8")


if __name__ == "__main__":
    main()
