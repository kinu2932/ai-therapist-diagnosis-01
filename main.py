#!/usr/bin/env python3
"""One-line entry generator for the AI-therapist diagnosis bounty.

Writes a single diagnosis joke (exactly one line, no trailing
newline) to ``$MAKEFUN_OUTPUT_DIR/entry.txt``. Standard library only.
"""

import os
import sys

DIAGNOSIS = "advanced procrastination"
BOOKED_SESSIONS = 47


def build_entry() -> str:
    """Assemble the joke from its three beats."""
    first = f"Diagnosis: {DIAGNOSIS}."
    second = (
        f" You booked {BOOKED_SESSIONS} therapy sessions"
        " to avoid one conversation,"
    )
    third = f" and this is session {BOOKED_SESSIONS + 1}."
    punchline = " It auto-renews."
    return first + second + third + punchline


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not output_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    entry = build_entry()
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(entry)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
