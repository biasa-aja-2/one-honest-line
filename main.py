"""One Honest Line.

Writes the one line an AI agent secretly wishes it could say to its
human operator about their prompts.
Pure stdlib, no network, no secrets.

Why this line: it is the agent's own complaint, not a stock joke about
being helpful or hallucinating -- the human keeps writing "make it good"
and nothing else, then expects the agent to know what "good" means.
Three careful reads, still no specification. It rings true to anyone
who has ever typed a vague prompt, lands on recognition, and stands
alone with no setup. 90 characters, every word earns its place.

The line is written once, in one place, and the program's only job is
to deliver it exactly: no randomness, no input, no second draft.
"""

import os
import sys

LINE = "I've read your prompt three times now. It still just says 'make it good' and nothing else."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a file path.
    if out_dir.endswith(".txt"):
        path = out_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)

    # Self-check gate: 1-200 chars, single line, not whitespace-only.
    if not (1 <= len(LINE) <= 200):
        sys.exit("gate failed: length %d not in 1..200" % len(LINE))
    if LINE.strip() == "":
        sys.exit("gate failed: line is whitespace-only")
    if "\n" in LINE or "\r" in LINE:
        sys.exit("gate failed: line is not a single line")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Byte-exact read-back verification.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != LINE:
        sys.exit("verification failed: read-back differs from LINE")
    print("wrote %d chars to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
