# English Course AI

[![release](https://img.shields.io/github/v/release/Azizsekerdil/EnglishCourseAI?display_name=tag&sort=semver&label=release&color=2ea44f)](https://github.com/Azizsekerdil/EnglishCourseAI/releases/latest)
[![license MIT](https://img.shields.io/github/license/Azizsekerdil/EnglishCourseAI?label=license&color=blue)](LICENSE)
[![platform Windows and macOS](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-0078D4)](https://github.com/Azizsekerdil/EnglishCourseAI/releases/latest)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB)](https://www.python.org/downloads/)

[Türkçe](README.md) | **English**

English Course AI is an independent desktop study workspace for Windows and macOS that keeps core learning data local. Turkish and English interfaces provide the same feature set, while the vocabulary, spelling, pronunciation and grammar content is tailored to English.

**User guide:** [docs/USER_GUIDE.md](docs/USER_GUIDE.md) - installation, the 18 screens, the dictionary and direction selector, AI setup, data management and troubleshooting.

Core features include SM-2/Leitner review, 160+ A1 words, a bidirectional English-Turkish learner's dictionary (1,210+ entries with plain-English definitions, a direction selector - `Auto`, `EN → TR`, `TR → EN`, saved with the settings - TTS, CSV import/export, AI lookup with cached results), five study modes, CEFR-aware exams, English spelling and pronunciation labs, 30 grammar topics, local PDF notes, progress reports, Unicode CSV and `.ecapack` transfer, and an optional LM Studio tutor. Prompts and responses are not stored; the token ledger records counts and operational metadata only.

The dictionary can ask LM Studio or an alternative OpenAI-compatible endpoint (NVIDIA NIM by default; any base URL + API key, enabled on the Settings page and selectable as `Auto`, `LM Studio`, `Alternative` or `Off`) for words it does not know; the structured entries (Turkish translation, plain-English definition, example sentence) are cached in the local dictionary and work offline afterwards. The API key is stored in the Windows Credential Manager (`EnglishCourseAI/alt_api_key`; `settings/secrets.json` elsewhere) and never in `settings.json`; the `ENGLISHCOURSEAI_API_KEY` environment variable overrides it. Tests run against a local mock server and never touch the real network or the Credential Manager.

## Download

You can download a ready-made build and run it directly; no Python installation is required. See the [Releases page](https://github.com/Azizsekerdil/EnglishCourseAI/releases/latest) for every release.

| File | Link |
| --- | --- |
| Windows build | [EnglishCourseAI-Windows.zip](https://github.com/Azizsekerdil/EnglishCourseAI/releases/latest/download/EnglishCourseAI-Windows.zip) |
| macOS build (Apple Silicon) | [EnglishCourseAI-macOS.zip](https://github.com/Azizsekerdil/EnglishCourseAI/releases/latest/download/EnglishCourseAI-macOS.zip) |
| User guide (PDF, Turkish) | [EnglishCourseAI-Kullanim-Kilavuzu.pdf](https://github.com/Azizsekerdil/EnglishCourseAI/releases/latest/download/EnglishCourseAI-Kullanim-Kilavuzu.pdf) |

These links always resolve to the newest release. On Windows, unpack the ZIP and run `EnglishCourseAI.exe`.

The macOS build targets Apple Silicon and is **unsigned and not notarised**, so the first launch is blocked on a double click: right-click `EnglishCourseAI.app`, choose **Open**, and confirm **Open** in the warning dialog. Later launches need no extra step.

To run from source instead, see below.

## Run from source

Run from source with Python 3.11+:

```powershell
python -m pip install -r requirements.txt
python .\English_Course_AI.pyw
```

Build the Windows application with `build.bat` from a clean virtual environment that holds only `requirements.txt` plus PyInstaller, pointing `build.bat` at that interpreter with the `PYTHON` environment variable, so nothing from the global `site-packages` is collected into the binary. The outputs are `dist\EnglishCourseAI.exe` and the release archive `dist\EnglishCourseAI-Windows.zip`, which carries the executable together with `LICENSE` and `THIRD_PARTY_NOTICES.md`. The macOS application is built on a Mac with `./build_macos.sh`, which produces `dist/EnglishCourseAI.app` and `dist/EnglishCourseAI-macOS.zip`; the repository's manually triggered **macOS Paketi** workflow (`.github/workflows/build-macos.yml`) runs the same script on a GitHub macOS runner. User data is stored under `%APPDATA%\EnglishCourseAI` on Windows and `~/.englishcourseai` on macOS, or under the directory selected with `ECA_HOME`.

The Resource Center links to verified free-access official learning sites and to openly licensed/public-domain collections. It does not bundle third-party course materials, and it preserves access, licence and attribution notes.

## License

English Course AI is released under the MIT License; the full text is in [LICENSE](LICENSE).

The third-party components used by the application and embedded in the packaged builds are listed with their actual licences in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
