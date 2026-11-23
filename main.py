#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke is a fixed, deterministic string: no randomness, no network,
pure standard library. The program writes it to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).
"""

JOKE = (
    "My coding agent fixed the demo crash by opening a pull request "
    "against itself \u2014 it's still waiting for its own approval."
)

import os
import sys


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
