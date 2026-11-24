"""One-Line Pitches entry: emit one persuasive sentence into entry.txt.

Running this script produces exactly one thing — a fixed sentence saved
to MAKEFUN_OUTPUT_DIR/entry.txt, or to /output/entry.txt when that
variable is not set. The output never changes between runs: the script
reaches no network, draws no random value, reads no clock, and takes no
secret from the environment.
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
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Post-write verification: read the file back and compare byte-for-byte
    # with the pitch; fail loudly if anything differs.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise SystemExit(
            "ERROR: entry.txt does not match PITCH byte-for-byte "
            f"(wrote {len(written)} bytes, expected {len(text.encode('utf-8'))})"
        )


if __name__ == "__main__":
    main()
