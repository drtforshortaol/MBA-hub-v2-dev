#!/usr/bin/env python3
"""Fail closed: El Niño V2 preview must contain all original slides."""
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
slides = [root / "images" / f"slide-{i:02d}.jpg" for i in range(1, 4)]
missing = [p.name for p in slides if not p.is_file() or p.stat().st_size < 1024]
if missing:
    print("BLOCKED: original slides missing:", ", ".join(missing), file=sys.stderr)
    sys.exit(1)
print("READY: all three original slide images are present.")
