#!/usr/bin/env python3
"""news-image-20261123 entry: write the front-page image to the output dir.

Reads MAKEFUN_OUTPUT_DIR, validates the bundled entry.png (PNG, at most
1 MiB, at most 1024x1024 px), and copies it to $MAKEFUN_OUTPUT_DIR/entry.png
with mode 0644. Standard library only, no network, deterministic: two runs
write the same bytes.
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1048576
MAX_DIM = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def read_png_size(path):
    """Return (width, height) from a PNG IHDR chunk, stdlib only."""
    with open(path, "rb") as fh:
        head = fh.read(33)
    if len(head) < 33 or head[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file")
    if head[12:16] != b"IHDR":
        raise ValueError("missing IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        return fail("MAKEFUN_OUTPUT_DIR is not set")
    if not os.path.isfile(SOURCE):
        return fail("entry.png not found next to main.py")

    size = os.path.getsize(SOURCE)
    if size > MAX_BYTES:
        return fail("entry.png is %d bytes, over the 1 MiB limit" % size)
    try:
        width, height = read_png_size(SOURCE)
    except (OSError, ValueError) as exc:
        return fail("entry.png failed validation: %s" % exc)
    if width > MAX_DIM or height > MAX_DIM:
        return fail("entry.png is %dx%d, over the 1024x1024 limit"
                    % (width, height))

    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    os.chmod(dest, 0o644)
    # Post-copy check: the written file must be byte-identical in size,
    # so a partial or failed copy can never pass as a valid run.
    if os.path.getsize(dest) != size:
        return fail("copied entry.png size mismatch")
    print("wrote %s (%d bytes, %dx%d)" % (dest, size, width, height))
    return 0


if __name__ == "__main__":
    sys.exit(main())
