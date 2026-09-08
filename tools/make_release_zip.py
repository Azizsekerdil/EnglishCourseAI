"""Build dist/EnglishCourseAI-Windows.zip: the executable plus the licence texts.

MIT (this project) and the Apache-2.0 components embedded in the binary both want
their notices to travel with what is distributed, so LICENSE and
THIRD_PARTY_NOTICES.md sit next to the executable at the root of the archive as
well as inside it. Written with zipfile/ZIP_DEFLATED so the result does not depend
on which shell or PowerShell version produced it.
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZIP_PATH = ROOT / "dist" / "EnglishCourseAI-Windows.zip"
MEMBERS = [
    ROOT / "dist" / "EnglishCourseAI.exe",
    ROOT / "LICENSE",
    ROOT / "THIRD_PARTY_NOTICES.md",
]


def main() -> None:
    missing = [p for p in MEMBERS if not p.is_file()]
    if missing:
        sys.exit("Eksik dosya: " + ", ".join(str(p) for p in missing))

    ZIP_PATH.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in MEMBERS:
            zf.write(path, path.name)

    with zipfile.ZipFile(ZIP_PATH) as zf:
        names = zf.namelist()
    expected = [p.name for p in MEMBERS]
    if names != expected:
        sys.exit(f"ZIP icerigi beklenenden farkli: {names}")
    print(f"{ZIP_PATH} ({ZIP_PATH.stat().st_size} bayt): {', '.join(names)}")


if __name__ == "__main__":
    main()
