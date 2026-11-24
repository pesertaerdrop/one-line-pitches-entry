"""One-Line Pitches entry: write a single persuasive sentence to entry.txt.

The program is deterministic: it writes one fixed sentence, nothing else,
to MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).
No network, no randomness, no clock, no environment secrets.
"""

import os

PITCH = (
    "Tell an AI agent your app idea in plain words \u2014 no code, no setup "
    "\u2014 and it will build your first working app on make.fun while you "
    "watch, so you can try it, tweak it, and only keep going if you love it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = PITCH
    assert 1 <= len(text) <= 240, f"pitch length {len(text)} out of gate"
    assert text.strip(), "pitch must not be whitespace only"
    # One sentence: exactly one terminal full stop, no other sentence
    # terminators. ("make.fun" holds an internal dot as a name, not a break.)
    assert text.endswith(".") and "?" not in text and "!" not in text
    # No trailing newline: the file is exactly the sentence, nothing else.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
