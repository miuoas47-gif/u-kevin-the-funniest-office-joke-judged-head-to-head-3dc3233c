#!/usr/bin/env python3
"""Entry for make.fun's 'The Funniest Office Joke, Judged Head to Head' bounty.

Prints a single original office joke to stdout and, when
MAKEFUN_OUTPUT_DIR is set, writes the same bytes to
$MAKEFUN_OUTPUT_DIR/entry.txt. No arguments, no network, no randomness,
no timestamps: the output is the same on every run.
"""

import os
import sys

LINE = "I told IT my laptop was running slow, and they said it was just matching the pace of our Monday meetings."


def main() -> int:
    data = (LINE + "\n").encode("utf-8")
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
            f.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
