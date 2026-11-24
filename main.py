"""One-Liner Laugh Lab v2: the robot vacuum's fibre-diet excuse.

Writes a single one-line excuse (at most 200 characters) to
/output/entry.txt. Stdlib only, deterministic, no trailing newline.
"""

from pathlib import Path

ENTRY = (
    "The app says I need more fibre, so I ate your sock. "
    "It was the only fibre in this house. Your feet are next."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate: one line, 1-200 characters, no trailing newline.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
