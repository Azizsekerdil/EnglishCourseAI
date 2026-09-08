# Third-Party Notices

*Türkçe not: EnglishCourseAI'nin kendi kaynak kodu MIT lisanslıdır ([LICENSE](LICENSE)). Bu dosya, uygulamada kullanılan ve dağıtılan ikili paketlerin içinde yer alan üçüncü taraf bileşenleri, gerçek lisanslarıyla birlikte listeler.*

EnglishCourseAI itself is distributed under the MIT License (see [LICENSE](LICENSE)).
The built-in vocabulary, learner's dictionary, grammar notes and exercise data under
`eca/` and `grammar/` were written for this project and are covered by that same licence.

This file lists the third-party components that are used by the application or embedded
in the binaries published with a release. Every licence below was read from the installed
package metadata or from the component's own licence file; none of them is guessed.

Versions in the tables are the versions that were actually inspected: pypdf from
`requirements.txt`, and everything else from the packaged **v1.3.0** artifacts
(`dist/EnglishCourseAI.exe`, built on Windows with CPython 3.11.9, and the macOS
`EnglishCourseAI.app` produced by `.github/workflows/build-macos.yml`).

Both artifacts are now frozen from a **clean virtual environment** that contains only
`requirements.txt` plus PyInstaller, so the binaries carry the application, pypdf and
CPython's own runtime - and nothing else. Section 3 records what this changed.

---

## 1. Declared runtime dependency

This is the only third-party package a source checkout installs (`requirements.txt`).

| Component | Version | Licence | Used for |
|---|---|---|---|
| [pypdf](https://github.com/py-pdf/pypdf) | 6.18.0 (`>=5.0,<7`) | BSD-3-Clause | The PDF Reader tab: opening a local PDF and extracting the text of a page. |

Everything else the application imports comes from the Python standard library
(`tkinter`, `sqlite3`, `urllib`, `ctypes`, `zipfile`, `csv`, ...).

---

## 2. Components embedded in every frozen build (Windows .exe and macOS .app)

Freezing with PyInstaller embeds the CPython interpreter, its standard library and the
native libraries CPython links against. Except where a row says otherwise, these are
present in both the Windows and the macOS artifacts.

### Permissive - Python Software Foundation family

| Component | Version | Licence | Used for |
|---|---|---|---|
| CPython interpreter and standard library | 3.11.9 | PSF-2.0 | Runs the application inside the frozen binary. |

### Permissive - BSD / MIT / Zlib family

| Component | Version | Licence | Used for |
|---|---|---|---|
| Tcl | 8.6 (`tcl86t.dll`, `libtcl8.6.dylib`) | TCL/TK licence (BSD-style) | Required by `tkinter`, which draws the whole user interface. |
| Tk | 8.6 (`tk86t.dll`, `libtk8.6.dylib`) | TCL/TK licence (BSD-style) | The widget toolkit behind every screen. |
| SQLite | 3.45.1 (`sqlite3.dll`) | Public domain (SQLite blessing) | Backs the local learner database through `sqlite3`. |
| libffi | 8 (`libffi-8.dll`; **Windows build only** - the macOS `.app` bundles no libffi and its `_ctypes` module links the system `/usr/lib/libffi.dylib`) | MIT | Required by `ctypes`, used to reach the Windows Credential Manager. |
| Libraries CPython statically links into its own modules, in both artifacts: libexpat 2.6.0 (`pyexpat`), XZ Utils liblzma (`_lzma`), libmpdec 2.5.1 (`_decimal`) | shipped with CPython 3.11.9 | MIT (the Expat licence); public domain for the liblzma core (XZ releases from 5.6 label the same terms 0BSD); BSD-2-Clause | XML parsing, `.xz` decompression and `decimal` arithmetic in the standard library. |
| bzip2 1.0.8 (`_bz2.pyd`) and zlib 1.3.1 (inside `python311.dll`), statically linked - **Windows build only**; the macOS `.app` links the system `/usr/lib/libbz2.1.0.dylib` and `/usr/lib/libz.1.dylib` | shipped with CPython 3.11.9 | bzip2 licence (BSD-style), (c) 1996-2019 Julian R Seward, reproduced in CPython's own `LICENSE.txt`; Zlib | `bz2` and `zlib` compression in the standard library, and the ZIP handling behind `zipfile`. |

*How the last two rows were identified:* CPython's Windows `LICENSE.txt` reproduces the
notices for bzip2 and libffi but is silent about expat, liblzma, libmpdec and zlib.
Those four were located by the strings their compiled modules carry (`expat_2.6.0` in
`pyexpat`, `libmpdec ... 2.5.1` in `_decimal`, `liblzma` in `_lzma`, zlib's `inflate`
error messages in `python311.dll`); the zlib version is the `zlib.ZLIB_VERSION` that
same DLL reports. The licences named above are the terms the upstream projects publish
for exactly those releases.

### Permissive - Apache-2.0

| Component | Version | Licence | Used for |
|---|---|---|---|
| OpenSSL | 3.0.13 (`libcrypto-3.dll`, `libssl-3.dll`, `libcrypto.3.dylib`, `libssl.3.dylib`) | Apache-2.0 | TLS for `urllib` when the optional remote AI endpoint is used, and hashing for `hashlib`. |
| PyInstaller runtime hooks (`pyi_rth_inspect`, `pyi_rth__tkinter`, `pyi_rth_pkgutil`, `pyi_rth_multiprocessing`, and from pyinstaller-hooks-contrib `pyi_rth_cryptography_openssl`) | PyInstaller 6.22.2 / pyinstaller-hooks-contrib 2026.7 | Apache-2.0 | Small startup scripts embedded in the binary that repoint `tkinter`, `pkgutil` and similar machinery at the frozen layout. Both projects licence their `rthooks` directories under Apache-2.0 specifically so they can be shipped this way. |

*Obligation:* Apache-2.0 requires the licence text and attribution to travel with the
binary, and EnglishCourseAI's own MIT licence asks for the same. Both build scripts
therefore embed a copy of this file and of `LICENSE` in the frozen application:
`EnglishCourseAI.spec` adds them to `dist/EnglishCourseAI.exe`, and `build_macos.sh`
adds them to `EnglishCourseAI.app`, where they land in `Contents/Resources/` and are
checked for before the release archive is made. On Windows the release ZIP
(`dist/EnglishCourseAI-Windows.zip`, produced by `build.bat` through
`tools/make_release_zip.py`) additionally carries both files next to the executable, so
they can be read without running it. The v1.2.1 and earlier archives were published
before this was wired up and do not contain them; v1.3.0 is the first release that does.

### Proprietary but freely redistributable

| Component | Licence | Used for |
|---|---|---|
| Microsoft Visual C++ / Universal CRT runtime (`VCRUNTIME140.dll`, `VCRUNTIME140_1.dll`, `ucrtbase.dll`, `api-ms-win-*.dll`) | Microsoft redistributable terms for the Visual C++ Redistributable | The C runtime that CPython and its extension modules on Windows are built against. |

### Copyleft with an explicit distribution exception

| Component | Version | Licence | Used for |
|---|---|---|---|
| PyInstaller bootloader (the embedded native launcher stub) and the Python loader modules it runs (`pyiboot01_bootstrap`, `pyimod01_archive`, `pyimod02_importers`, `pyimod03_ctypes`, `pyimod04_pywin32`) | 6.22.2 | GPL-2.0-or-later **WITH** the PyInstaller bootloader exception | The native stub that unpacks the archive and starts CPython inside the frozen binary, plus the bootstrap and import machinery that stub executes. PyInstaller's `COPYING.txt` lists `./bootloader/` **and** `./PyInstaller/loader` as the "Bootloader and Related Files" the exception covers, and each loader module carries `SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)`. |

*Obligation / why this is fine:* PyInstaller's own licence grants "unlimited permission
to link or embed compiled bootloader and related files into combinations with other
programs, and to distribute those combinations without any restriction coming from the
use of those files". That exception is what allows a frozen application to be published
under a licence of the author's choosing, so no GPL term propagates to EnglishCourseAI.
Only modification and standalone redistribution of the bootloader and its loader modules
stay under the GPL.

**Note on UPX.** `EnglishCourseAI.spec` sets `upx=True`, but UPX was not installed on the
machine that produced the published v1.3.0 executable, so that binary is not UPX-packed
(no UPX signature is present in it). If a future build machine has UPX on `PATH`, UPX is
GPL-2.0-or-later with a special exception that explicitly permits distributing the
compressed executables it produces under any licence.

---

## 3. What the clean build removed (was in the Windows v1.2.1 executable)

pypdf imports Pillow, cryptography and fontTools lazily for optional features (image
extraction, AES-encrypted PDFs, embedded fonts). PyInstaller follows those imports, so
when those packages happen to be installed on the build machine they are collected into
the executable together with their own dependencies. That is what happened for the
published Windows v1.2.1 binary, which was frozen from a developer machine's global
`site-packages`: it also carried Pillow, fontTools, lxml, NumPy with OpenBLAS,
cryptography, beautifulsoup4, PyYAML, pywin32 and their companions - none of which this
application ever calls.

From **v1.3.0** onwards the Windows executable is built exactly the way the macOS `.app`
already was: in a throwaway virtual environment that holds only `requirements.txt`
(pypdf) plus PyInstaller. A run of the build therefore collects only

| Group | What is inside the v1.3.0 executable |
|---|---|
| The application | `eca` (23 modules) and `English_Course_AI.pyw` |
| Declared dependency | `pypdf` 6.18.0 (55 modules), BSD-3-Clause - section 1 |
| Runtime | CPython 3.11.9's own standard library and the native libraries of section 2 (`python311.dll`, `tcl86t.dll`, `tk86t.dll`, `sqlite3.dll`, `libssl-3.dll`, `libcrypto-3.dll`, `libffi-8.dll`, `VCRUNTIME140.dll` and CPython's `.pyd` extension modules) |
| Data | `assets/`, `Resources/`, `grammar/`, `LICENSE`, `THIRD_PARTY_NOTICES.md`, and Tcl/Tk's own data files |

`build/EnglishCourseAI/Analysis-00.toc` for the v1.3.0 build lists no third-party
top-level package other than `pypdf`, and a byte scan of `dist/EnglishCourseAI.exe`
finds no `numpy`, `pandas`, `lxml`, `PIL`, `fontTools`, `cryptography`,
`charset_normalizer`, `bs4`, `yaml` or `defusedxml`. The executable shrank from
42,521,596 to 14,920,000 bytes.

The licence obligations of the removed packages therefore no longer apply to any
published v1.3.0 artifact. Two of them are worth naming explicitly, because they were
the only copyleft-derived components outside PyInstaller in the older Windows binary:
the GCC/gfortran runtime statically linked into NumPy's OpenBLAS
(GPL-3.0-or-later WITH GCC-exception-3.1) is gone with NumPy, and `PIL/_imagingft.pyd`
- the Pillow extension that links FriBidi (LGPL-2.1-or-later) - was never collected in
the first place, because the application does not import `PIL.ImageFont`. **No LGPL- or
AGPL-licensed component is present in any published artifact.**

---

## 4. Build and test tooling (not shipped inside the binaries)

| Component | Version | Licence | Used for |
|---|---|---|---|
| PyInstaller | 6.22.2 (`>=6.0,<7`) | GPL-2.0-or-later WITH the bootloader exception | Produces `dist/EnglishCourseAI.exe` and `EnglishCourseAI.app`. Of PyInstaller itself, only the bootloader stub, its `PyInstaller/loader` modules and the Apache-2.0 runtime hooks described in section 2 end up in the binary. |
| pyinstaller-hooks-contrib | 2026.7 | GPL-2.0-or-later for the standard (build-time) hooks; Apache-2.0 for the runtime hooks | Packaging hooks consulted at build time. The GPL-licensed standard hooks run on the build machine and are never embedded; only the Apache-2.0 runtime hook listed in section 2 is shipped. |
| pytest | 9.1.1 (`>=8.0,<10`) | MIT | Runs the test suite. Never shipped. |
| Python-Markdown | 3.10.3 (`>=3.5,<4`) | BSD-3-Clause | Renders `docs/*.md` into the HTML that `tools/build_guides.py` prints to the guide PDFs. Never shipped. |

*Obligation:* PyInstaller and its community hook collection are used as unmodified build
tools, so their GPL terms apply to those projects and not to the application they
package. Both projects deliberately licence the parts that do get embedded under terms
that permit it: the bootloader exception for the launcher stub and its loader modules,
and Apache-2.0 for the runtime hooks (see section 2).

---

## 5. External services and operating-system features (not bundled)

| Component | Licence / terms | Used for |
|---|---|---|
| Windows `System.Speech` speech synthesis, driven through PowerShell | Part of Windows; no code is bundled or redistributed | The listen buttons in the dictionary and pronunciation screens. |
| LM Studio, NVIDIA NIM, or any other OpenAI-compatible endpoint the user configures | Supplied and licensed by whoever operates the endpoint | Optional AI dictionary lookups and tutor features. Disabled by default; nothing is bundled and no API key ships with the application. |

---

## 6. Learning resources: linked, never bundled or downloaded

The Resource Center (`eca/content.py`, `eca/tabs/reading.py`) is a catalogue of links.
Choosing **Open** hands the URL to the user's default browser. The application performs
**no download of its own**, and no third-party course material is copied into this
repository or into the released binaries. Anything a user chooses to fetch from these
sites afterwards keeps that site's own licence, which the catalogue shows on each card:

| Resource | Licence / access terms shown in the app |
|---|---|
| British Council LearnEnglish | Free access; external copyright applies |
| BBC Learning English | Free access; BBC copyright applies |
| Cambridge English free activities | Free access; Cambridge copyright applies |
| VOA Learning English | Free access; check item-specific reuse terms |
| English as an Additional Language - Wikibooks | CC BY-SA 4.0 |
| Tatoeba English sentences | CC BY 2.0 FR / selected CC0; sentence-level attribution must be preserved |
| LibriVox English audiobooks | Public domain in the USA; local status may differ |
| Project Gutenberg English books | Project Gutenberg public-domain terms; check each item and local status |

*Obligation:* material reused from Wikibooks stays under CC BY-SA 4.0 and material from
Tatoeba under CC BY 2.0 FR, with attribution, if a user redistributes it. Because nothing
is bundled, that obligation falls on the user's own reuse and never on this repository.

The `Resources/` folder ships with a single placeholder text file. Files a learner drops
into it are their own and are never redistributed by this project.

---

## 7. Summary

* No GPL-, LGPL- or AGPL-licensed library is imported by the source tree, listed in
  `requirements.txt`, or linked into a published artifact under terms that would affect
  EnglishCourseAI.
* Only one GPL-derived project reaches a published v1.3.0 binary: PyInstaller, through
  its bootloader stub and the loader modules that stub runs, and it carries an explicit
  exception written to permit exactly this kind of distribution. Of the other PyInstaller
  code embedded in the binary, the `rthooks` startup scripts are Apache-2.0; the
  GPL-licensed build-time hooks run on the build machine and are never shipped. (The
  second such component in the old Windows binary, the GCC/gfortran runtime inside
  NumPy's OpenBLAS, left with NumPy when the build moved to a clean environment.)
* Everything else is BSD, MIT, Zlib, Apache-2.0, PSF-2.0, public domain, or a freely
  redistributable Microsoft runtime.

Corrections are welcome: please open an issue at
<https://github.com/Azizsekerdil/EnglishCourseAI/issues>.
