"""One-Liner Laugh Lab v3: deadpan relocation excuse.

The robot vacuum denies eating the sock. It only moved the sock
somewhere warmer and darker, on a permanent basis.
"""

from pathlib import Path

ENTRY = (
    "I didn't eat your sock. I relocated it somewhere warmer and darker. "
    "Your sock lives in the crawl space under your bed now. Permanently."
)


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
