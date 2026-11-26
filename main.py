"""Write one 129-character apology line to /output/entry.txt.
Use $MAKEFUN_OUTPUT_DIR instead when set and nonempty.
Python standard library only; deterministic; exit 0.
"""

import os
import shutil
from pathlib import Path


APOLOGY = (
    "Sorry, I heard 'book a table for two' as 'book a stable for two.' "
    "I mentioned your anniversary. They've brought out the good hay."
)


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    for stale_path in output_dir.iterdir():
        if stale_path.is_symlink() or not stale_path.is_dir():
            stale_path.unlink()
        else:
            shutil.rmtree(stale_path)

    (output_dir / "entry.txt").write_bytes(APOLOGY.encode("utf-8"))


if __name__ == "__main__":
    main()
