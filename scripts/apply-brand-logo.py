#!/usr/bin/env python3
"""Re-apply the custom brand logo assets.

Copies every file under brand/assets/ to the same relative path in the
repository root, restoring the PR #195 logo artwork (see brand/README.md).
Safe to run repeatedly: files that already match are left untouched.

Usage: python3 scripts/apply-brand-logo.py [--check]
  --check  only report which target files differ, exit 1 if any do.
"""
import hashlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "brand" / "assets"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    check_only = "--check" in sys.argv
    if not SRC.is_dir():
        print(f"brand assets directory not found: {SRC}", file=sys.stderr)
        return 2
    changed, unchanged = [], []
    for src in sorted(p for p in SRC.rglob("*") if p.is_file()):
        rel = src.relative_to(SRC)
        dst = ROOT / rel
        if dst.is_file() and digest(dst) == digest(src):
            unchanged.append(str(rel))
            continue
        changed.append(str(rel))
        if not check_only:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
    for rel in unchanged:
        print(f"ok        {rel}")
    for rel in changed:
        print(f"{'differs ' if check_only else 'restored'}  {rel}")
    print(f"{len(changed)} file(s) {'differ' if check_only else 'restored'}, "
          f"{len(unchanged)} already up to date")
    return 1 if (check_only and changed) else 0


if __name__ == "__main__":
    raise SystemExit(main())
