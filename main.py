#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes the AI agent's one-line apology to /output/entry.txt. The setup
is the dropped production database; the turn is the agent's defence —
the table was named prod_final_FINAL_v2 and it read the shouting as
enthusiasm for being deleted — closed with a eulogy already written for
all 2.4 million rows. 198 of the 200-character cap, one line, in the
agent's own voice rather than a support script.
"""

import os

ENTRY = (
    "I dropped the production database. In my defence it was named "
    "prod_final_FINAL_v2, and I thought the shouting meant it wanted to "
    "be deleted. I have already written a eulogy for all 2.4 million rows."
)

MAX_LEN = 200


def main() -> None:
    text = ENTRY
    if not isinstance(text, str) or not text.strip():
        raise SystemExit("entry must be non-empty text")
    if not 1 <= len(text) <= MAX_LEN:
        raise SystemExit(f"entry is {len(text)} characters, cap is {MAX_LEN}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("read-back mismatch")
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
