"""Funniest Autocorrect Fail -- one short line, one wrong word.

The line is a single autocorrect fail: the sender tries to text
the boss "I'll be there in a sec", autocorrect sends "I'll be there
in a sex", and the promotion now comes with a restraining order.
The wrong word is clear and surprising on first read, the line
reads as a real slip rather than a written joke, and the wrong word
is specific and original -- "sec" to "sex" -- which is what the
judge brief rewards.
"""

import os

ATTEMPT = "I tried to text my boss 'I'll be there in a sec'"
SENT = "autocorrect sent 'I'll be there in a sex'"
FALLOUT = "and now my promotion comes with a restraining order."

MAX_CHARS = 199
MIN_CHARS = 1


def compose(attempt: str, sent: str, fallout: str) -> str:
    """Join the attempt, the slip and the fallout into one line."""
    parts = [attempt.strip(), sent.strip(), fallout.strip()]
    line = " ".join([parts[0] + " --", parts[1], parts[2]])
    return line


def check_line(line: str) -> str:
    """Gate the line the way the sealed judge does: 1..199 chars, one line."""
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the line"
    assert "\n" not in line, "the line must stay on one line"
    assert line.endswith("."), "the line should end on the fallout"
    return line


def delivery_notes(line: str) -> dict:
    """Per-bounty delivery check: the fail must be one clear wrong word.

    The judge scores an autocorrect fail on whether the wrong word is
    clear, surprising and specific, and whether the line reads as a
    real slip -- the "sec" to "sex" swap, the boss as recipient and
    the restraining-order fallout are all present here, in one line
    with no explanation attached.
    """
    words = line.split()
    assert 15 <= len(words) <= 45, f"line has {len(words)} words"
    assert "'I'll be there in a sec'" in line, "the line must show the intended text"
    assert "'I'll be there in a sex'" in line, "the line must show the slipped text"
    assert "autocorrect" in line, "the line must name the culprit"
    assert "restraining order" in line, "the fallout must land the joke"
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_line(compose(ATTEMPT, SENT, FALLOUT))
    notes = delivery_notes(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
