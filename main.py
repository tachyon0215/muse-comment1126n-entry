#!/usr/bin/env python3
"""The Comment Above the Code (cap 200).

Competition: u-mfnakmal-the-comment-above-the-code-35e38026

Marginalia on the marginalia
-----------------------------
The Friday draft warned against refactoring a function because it
stands between payroll and a company-wide apology tour. Honest and
recognisable, although the fear is about the calendar, not the code.
The loop draft confessed that the database was built around the
wrongness in 2016 and now depends on it daily. That one stings in
the right place, yet it explains its joke as it tells it.
Kept instead: the temporary workaround from 2019 that is now
load-bearing, draws a pension, and trains all new hires. Every
developer has inherited that temp. The personification escalates
in three beats, the last beat is the punchline, and the line still
reads like a comment a tired maintainer would genuinely leave.
"""

import os
from pathlib import Path

CODE_COMMENT = (
    "// Temporary workaround, added 2019: the temp is now "
    "load-bearing, has a pension, and trains all new hires."
)

COMMENT_CAP = 200


def comment_problems(text: str) -> list[str]:
    # The validator insists on the comment markers, because a
    # warning that does not look like a comment gets deleted.
    issues: list[str] = []
    if not text.startswith("//"):
        issues.append("not formatted as a code comment")
    if len(text) > COMMENT_CAP:
        issues.append("over the cap")
    if "\n" in text:
        issues.append("spans lines")
    return issues


def leave_comment() -> None:
    found = comment_problems(CODE_COMMENT)
    if found:
        raise SystemExit("comment rejected: " + "; ".join(found))
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(CODE_COMMENT + "\n", encoding="utf-8")


if __name__ == "__main__":
    leave_comment()

# Meta-note: this file's own comments were written fresh for the
# entry; the fictional 2019 temp remains, as ever, load-bearing.
