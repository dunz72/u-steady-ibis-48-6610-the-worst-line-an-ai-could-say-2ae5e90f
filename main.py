"""Copy entry.txt to the make.fun output directory.

Stdlib only: the grader's Python image has no third-party libraries.
Validates the line (UTF-8, non-empty, at most 200 characters) and
verifies the copy byte-for-byte with SHA-256.
"""

import hashlib
import os
import shutil
import sys

MAX_CHARS = 200


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    try:
        with open(src, "rb") as f:
            raw = f.read()
    except OSError as exc:
        print(f"error: cannot read entry.txt: {exc}", file=sys.stderr)
        return 1

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        print(f"error: entry.txt is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    line = text.strip()
    if not line:
        print("error: entry.txt is empty", file=sys.stderr)
        return 1
    if "\n" in line:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: entry is {len(line)} characters, over the 200 limit",
            file=sys.stderr,
        )
        return 1

    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, dst)

    def sha256(path: str) -> str:
        digest = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                digest.update(chunk)
        return digest.hexdigest()

    if sha256(src) != sha256(dst):
        print("error: SHA-256 mismatch after copy", file=sys.stderr)
        return 1

    print(f"ok: entry.txt ({len(line)} chars) copied to {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
