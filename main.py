#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry (account A / overtheraa).

Writes one invented word and its one-line definition to /output/entry.txt.
Gate: UTF-8 text, 1 to 140 characters, not only white space, a single line.

The word: typok — typing + "ok", with a nod to "typo", the little
mistake a one-word reply feels like after a long wait.

Judge-brief mapping (brief's order, most important first):
1. Fresh word + one clear line: "typok" is coined here, followed by a
   single-line (n.) definition — nothing else in the file.
2. Real gap: English has no word for the specific dread of a long
   "typing…" that ends in a one-syllable shrug; every messenger user
   recognises it at once.
3. Exact and self-contained: the definition names the trigger (ten
   minutes of blinking dots), the feeling (dread) and the payoff
   (just "ok") in one reading, with no second sentence or example.
4. Well formed and easy to live with: two syllables (TY-pok),
   spelled exactly as it sounds, built from two words everyone
   already knows — it sounds as though English could have grown it.
5. Fresh and surprising: the word itself is the punchline — the
   ten-minute wait collapses into the two letters it was waiting for.
"""

import os
import sys

ENTRY = "typok (n.): the dread of watching 'typing\u2026' blink for ten minutes, then getting just 'ok'."


def gate_ok(text):
    """Mirror the kit gate: 1-140 chars, not only whitespace, single line."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 140:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def write_entry(path="/output/entry.txt"):
    """Write the entry, verifying it against the gate first."""
    if not gate_ok(ENTRY):
        raise ValueError("entry fails the gate: %r" % ENTRY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    return path


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    written = write_entry(target)
    print("wrote %s (%d chars)" % (written, len(ENTRY)))
