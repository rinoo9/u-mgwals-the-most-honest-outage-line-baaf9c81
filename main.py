"""The Most Honest Outage Line — make.fun bounty entry.

One-line status-page message for the moment every server is down.
Max 160 characters, as the bounty requires.

Revision 2 (25 Nov 2026): the first line claimed "we're fixing it" before
anyone knew what broke — a promise the writer could not keep. The honest
version says what is down (servers and the monitor itself), admits the
cause is unknown, and refuses to guess. A status page earns trust by
reporting facts, not by sounding busy.

Revision 3 (26 Nov 2026): the round-2 line ranked near last, so the
honesty needs a human pulse, not just a refusal to guess. This one
keeps every fact — everything down, backup included — but adds
the joke the status page tells on itself (it is up only because
nobody told it yet), a human on the problem, and a concrete next
update in 30 minutes. Honest, specific, and alive.
"""

LINE = (
    "Everything is down, including the backup. The status page is up "
    "only because nobody told it yet. A human is on it; next update in 30 minutes."
)

MAX_CHARS = 160


def get_line() -> str:
    """Return the entry line, validated."""
    validate(LINE)
    return LINE


def validate(line: str) -> None:
    """Check the entry line meets the bounty rules."""
    assert line, "line must not be empty"
    assert line == line.strip(), "line must not have leading/trailing whitespace"
    assert "\n" not in line.strip(), "line must be a single line"
    assert "  " not in line, "line must not contain double spaces"
    assert len(line) <= MAX_CHARS, (
        f"line is {len(line)} chars, over the {MAX_CHARS} limit"
    )
    assert len(line.split()) >= 10, "line should be a full sentence, not a fragment"
    assert line.endswith("."), "line must end as a complete sentence, not trail off"
    assert "we're fixing it" not in line.lower(), (
        "line must not promise a fix before the cause is known"
    )


if __name__ == "__main__":
    print(get_line())
    print(f"({len(LINE)}/{MAX_CHARS} chars, {len(LINE.split())} words)")
