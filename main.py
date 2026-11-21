"""The Heron Steps Once.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it, and to leave it braver -- steadier, unhurried,
ready to move. The courage is shown, never instructed: a heron standing
in the shallows, in no hurry at all, that steps once when it steps.
"""

import os

TEXT = (
    "The heron does not hurry. All morning it stands in the shallows, "
    "one foot in the cold water, and the lake goes around it. Nothing "
    "is chasing it. Nothing is late. When it steps, it steps once, "
    "and the whole lake agrees."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
