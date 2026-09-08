# Third-Party Notices

*Türkçe not: EnglishCourseAI'nin kendi kaynak kodu MIT lisanslıdır ([LICENSE](LICENSE)). Bu dosya, uygulamada kullanılan ve dağıtılan ikili paketlerin içinde yer alan üçüncü taraf bileşenleri, gerçek lisanslarıyla birlikte listeler.*

EnglishCourseAI itself is distributed under the MIT License (see [LICENSE](LICENSE)).
The built-in vocabulary, learner's dictionary, grammar notes and exercise data under
`eca/` and `grammar/` were written for this project and are covered by that same licence.

This file lists the third-party components that are used by the application or embedded
in the binaries published with a release. Every licence below was read from the installed
package metadata or from the component's own licence file; none of them is guessed.

Versions in the tables are the versions that were actually inspected: pypdf from
`requirements.txt`, and everything else from the packaged **v1.2.1** artifacts
(`dist/EnglishCourseAI.exe`, built on Windows with CPython 3.11.9, and the macOS
`EnglishCourseAI.app` produced by `.github/workflows/build-macos.yml`).

---

## 1. Declared runtime dependency

This is the only third-party package a source checkout installs (`requirements.txt`).

| Component | Version | Licence | Used for |
|---|---|---|---|
| [pypdf](https://github.com/py-pdf/pypdf) | 6.13.2 (`>=5.0,<7`) | BSD-3-Clause | The PDF Reader tab: opening a local PDF and extracting the text of a page. |

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
| PyInstaller runtime hooks (`pyi_rth_inspect`, `pyi_rth__tkinter`, `pyi_rth_pkgutil`, `pyi_rth_multiprocessing`, and from pyinstaller-hooks-contrib `pyi_rth_cryptography_openssl`) | PyInstaller 6.21.0 / pyinstaller-hooks-contrib 2026.6 | Apache-2.0 | Small startup scripts embedded in the binary that repoint `tkinter`, `pkgutil` and similar machinery at the frozen layout. Both projects licence their `rthooks` directories under Apache-2.0 specifically so they can be shipped this way. |

*Obligation:* Apache-2.0 requires the licence text and attribution to travel with the
binary, and EnglishCourseAI's own MIT licence asks for the same. Both build scripts
therefore embed a copy of this file and of `LICENSE` in the frozen application:
`EnglishCourseAI.spec` adds them to `dist/EnglishCourseAI.exe`, and `build_macos.sh`
adds them to `EnglishCourseAI.app`, where they land in `Contents/Resources/` and are
checked for before the release archive is made. On Windows the release ZIP
(`dist/EnglishCourseAI-Windows.zip`, produced by `build.bat`) additionally carries both
files next to the executable, so they can be read without running it. The v1.2.1
archives were published before this was wired up and do not contain them.

### Proprietary but freely redistributable

| Component | Licence | Used for |
|---|---|---|
| Microsoft Visual C++ / Universal CRT runtime (`VCRUNTIME140.dll`, `VCRUNTIME140_1.dll`, `ucrtbase.dll`, `api-ms-win-*.dll`) | Microsoft redistributable terms for the Visual C++ Redistributable | The C runtime that CPython and its extension modules on Windows are built against. |

### Copyleft with an explicit distribution exception

| Component | Version | Licence | Used for |
|---|---|---|---|
| PyInstaller bootloader (the embedded native launcher stub) and the Python loader modules it runs (`pyiboot01_bootstrap`, `pyimod01_archive`, `pyimod02_importers`, `pyimod03_ctypes`, `pyimod04_pywin32`) | 6.21.0 | GPL-2.0-or-later **WITH** the PyInstaller bootloader exception | The native stub that unpacks the archive and starts CPython inside the frozen binary, plus the bootstrap and import machinery that stub executes. PyInstaller's `COPYING.txt` lists `./bootloader/` **and** `./PyInstaller/loader` as the "Bootloader and Related Files" the exception covers, and each loader module carries `SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)`. |

*Obligation / why this is fine:* PyInstaller's own licence grants "unlimited permission
to link or embed compiled bootloader and related files into combinations with other
programs, and to distribute those combinations without any restriction coming from the
use of those files". That exception is what allows a frozen application to be published
under a licence of the author's choosing, so no GPL term propagates to EnglishCourseAI.
Only modification and standalone redistribution of the bootloader and its loader modules
stay under the GPL.

**Note on UPX.** `EnglishCourseAI.spec` sets `upx=True`, but UPX was not installed on the
machine that produced the published v1.2.1 executable, so that binary is not UPX-packed
(no UPX signature is present in it). If a future build machine has UPX on `PATH`, UPX is
GPL-2.0-or-later with a special exception that explicitly permits distributing the
compressed executables it produces under any licence.

---

## 3. Extra libraries inside the published **Windows** v1.2.1 executable

pypdf imports Pillow, cryptography and fontTools lazily for optional features (image
extraction, AES-encrypted PDFs, embedded fonts). PyInstaller follows those imports, so
when those packages happen to be installed on the build machine they are collected into
the executable together with their own dependencies. That is what happened for the
published Windows v1.2.1 binary; the list below is what a byte-level inventory of
`dist/EnglishCourseAI.exe` actually contains.

The macOS workflow installs only `requirements.txt` into a clean runner, so the macOS
`.app` contains **none** of the packages in this section.

### MIT family

| Component | Version | Licence | Used for |
|---|---|---|---|
| Pillow | 12.2.0 | MIT-CMU | pypdf's optional image-extraction path. |
| fontTools | 4.63.0 | MIT | pypdf's optional embedded-font handling. |
| beautifulsoup4 | 4.15.0 | MIT | Pulled in by `lxml.html.soupparser`; never called by this application. |
| soupsieve | 2.8.4 | MIT | CSS selector engine used by beautifulsoup4. |
| charset-normalizer | 3.4.7 | MIT | Encoding detection for beautifulsoup4 (the mypyc-compiled `81d243bd...__mypyc.pyd` belongs to it). |
| PyYAML | 6.0.3 | MIT | Read by `numpy.__config__` when NumPy reports its build configuration. |
| cffi (`_cffi_backend`) | 2.0.0 | MIT | Collected by PyInstaller's `cryptography` hook. cryptography 50 binds OpenSSL through Rust (`cryptography/hazmat/bindings/_rust.pyd`) and imports no cffi, so only the `_cffi_backend` extension is present - the `cffi` Python package is not even in the archive - and nothing calls it. |
| libxml2 / libxslt | statically linked into `lxml/etree.pyd` | MIT | The XML and XSLT engines behind lxml. |
| Little CMS 2 | statically linked into `PIL/_imagingcms.pyd` | MIT | Pillow's colour-management module. |

### BSD family

| Component | Version | Licence | Used for |
|---|---|---|---|
| lxml | 6.1.1 | BSD-3-Clause | Optional XML backend reachable from fontTools. |
| lxml_html_clean | 0.4.5 | BSD-3-Clause | Companion package of `lxml.html`. |
| NumPy | 2.4.6 | BSD-3-Clause (the wheel additionally carries 0BSD, MIT, Zlib and CC0-1.0 for vendored pieces) | Pulled in by Pillow's array interface. |
| OpenBLAS including LAPACK (`numpy.libs/libscipy_openblas64_-*.dll`) | shipped with NumPy 2.4.6 | BSD-3-Clause | NumPy's linear-algebra kernels. |
| pywin32 (`win32/win32pdh.pyd`, `pywin32_system32/pywintypes311.dll`) | 312 | BSD-3-Clause style, (c) 1994-2008 Mark Hammond, per `win32/License.txt`, the licence file that governs the bundled files (the PyPI classifier records it as PSF) | Pulled in by NumPy's optional Windows performance-counter probe. |
| libjpeg-turbo, libtiff, OpenJPEG, libwebp, zlib-ng and XZ/liblzma, statically linked into `PIL/_imaging.pyd` and `PIL/_webp.pyd` | shipped with Pillow 12.2.0 | IJG / BSD-3-Clause, libtiff licence (BSD-style), BSD-2-Clause, BSD-3-Clause, Zlib, 0BSD | Pillow's image codecs. |
| libavif with libaom, dav1d and libyuv, statically linked into `PIL/_avif.pyd` | shipped with Pillow 12.2.0 | BSD-2-Clause, BSD-2-Clause-Patent, and BSD-3-Clause for libyuv, (c) 2011 The LibYuv Project Authors (recorded in Pillow's own `LICENSE`) | Pillow's AVIF codec; libyuv provides its plane scaling. |
| ISO Schematron RELAX NG schema and XSLT skeleton (`lxml/isoschematron/resources/`) | shipped with lxml 6.1.1 | zlib-style permissive licence, (c) Rick Jelliffe and Academia Sinica Computing Center; the schema itself is an ISO/IEC publicly available specification | Data files lxml installs alongside its Schematron support. |

### Python Software Foundation family

| Component | Version | Licence | Used for |
|---|---|---|---|
| defusedxml | 0.7.1 | PSF-2.0 | Hardened XML parsing that Pillow uses when it is available. |
| typing_extensions | 4.15.0 | PSF-2.0 | Typing back-ports imported by several of the packages above. |

### Dual-licensed, permissive either way

| Component | Version | Licence | Used for |
|---|---|---|---|
| cryptography | 50.0.0 | Apache-2.0 **OR** BSD-3-Clause, at the recipient's choice | pypdf's optional support for AES-encrypted PDFs. |

The executable already carries `cryptography-50.0.0.dist-info/licenses/` and that
project's CycloneDX SBOMs, which cover the Rust crates vendored into
`cryptography/hazmat/bindings/_rust.pyd`. NumPy's own `LICENSE.txt`, with all of its
vendored notices, is embedded too.

### Copyleft with an explicit distribution exception

| Component | Licence | Used for |
|---|---|---|
| GCC/gfortran runtime, statically linked into `numpy.libs/libscipy_openblas64_-*.dll` | GPL-3.0-or-later **WITH** GCC-exception-3.1 (GCC Runtime Library Exception) | Fortran runtime support for the OpenBLAS kernels NumPy ships. |

*Obligation / why this is fine:* NumPy's own `LICENSE.txt`, embedded in the executable,
documents this component. The GCC Runtime Library Exception exists specifically to
"allow compilation of non-GPL (including proprietary) programs to use ... the header
files and runtime libraries covered by this Exception", so the GPL does **not** propagate
to EnglishCourseAI and the application may be published under MIT.

### Verified absent

`PIL/_imagingft.pyd` - the Pillow extension that statically links FreeType, Raqm and
**FriBidi (LGPL-2.1-or-later)** - is *not* collected into the executable, because the
application never imports `PIL.ImageFont`. No LGPL-licensed component is present in any
published artifact.

---

## 4. Build and test tooling (not shipped inside the binaries)

| Component | Version | Licence | Used for |
|---|---|---|---|
| PyInstaller | 6.21.0 (`>=6.0,<7`) | GPL-2.0-or-later WITH the bootloader exception | Produces `dist/EnglishCourseAI.exe` and `EnglishCourseAI.app`. Of PyInstaller itself, only the bootloader stub, its `PyInstaller/loader` modules and the Apache-2.0 runtime hooks described in section 2 end up in the binary. |
| pyinstaller-hooks-contrib | 2026.6 | GPL-2.0-or-later for the standard (build-time) hooks; Apache-2.0 for the runtime hooks | Packaging hooks consulted at build time. The GPL-licensed standard hooks run on the build machine and are never embedded; only the Apache-2.0 runtime hook listed in section 2 is shipped. |
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
* Only two GPL-derived projects reach a published binary - PyInstaller, through its
  bootloader stub and the loader modules that stub runs, and the GCC/gfortran runtime
  statically linked inside NumPy's OpenBLAS - and each carries an explicit exception
  written to permit exactly this kind of distribution. Of the other PyInstaller code
  embedded in the binary, the `rthooks` startup scripts are Apache-2.0; the
  GPL-licensed build-time hooks run on the build machine and are never shipped.
* Everything else is BSD, MIT, Zlib, Apache-2.0, PSF-2.0, public domain, or a freely
  redistributable Microsoft runtime.

Corrections are welcome: please open an issue at
<https://github.com/Azizsekerdil/EnglishCourseAI/issues>.
