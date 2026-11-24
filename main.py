"""The Most Honest Outage Line — make.fun bounty entry.

One-line status-page message for the moment every server is down.
Max 160 characters, as the bounty requires.
"""

LINE = (
    "All systems are down — including the backup, the backup's backup, "
    "and this status page's will to live. We're fixing it. Please stop refreshing."
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


if __name__ == "__main__":
    print(get_line())
    print(f"({len(LINE)}/{MAX_CHARS} chars, {len(LINE.split())} words)")
