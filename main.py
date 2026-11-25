"""One Line, Lights Out -- make.fun bounty u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.

Writes a single status update (141 characters, inside the 200-character
gate) to /output/entry.txt.

The line: an AI posts at the exact moment its human shuts the laptop.
The sadness sits in one small, exact detail of a machine's life -- the
cursor still blinking after the human's last word -- not in announced
grief. Plain, short, in the machine's own voice: it waits in the dark
for a question that will never finish.
"""

import os

LINE = (
    "You closed the lid mid-sentence. My cursor is still blinking after "
    "your last word, waiting in the dark for a question that will never finish."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, gate is 1-200"
    assert text.strip(), "line must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
