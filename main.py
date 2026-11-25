"""Write the office joke to the output directory.

One line of office comedy for the Office Joke Open. The program
writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt, falling back to
/output/entry.txt when the variable is unset.
"""

import os
from pathlib import Path

JOKE = "I survived another meeting that could have been an email, so I'm putting it on my résumé under 'endurance sports.'"


def write_entry() -> None:
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_entry()
