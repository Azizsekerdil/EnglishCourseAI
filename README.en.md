# English Course AI

English Course AI is an independent Windows desktop study workspace that keeps core learning data local. Turkish and English interfaces provide the same feature set, while the vocabulary, spelling, pronunciation and grammar content is tailored to English.

**User guide:** [docs/USER_GUIDE.md](docs/USER_GUIDE.md) - installation, the 18 screens, the dictionary and direction selector, AI setup, data management and troubleshooting.

Core features include SM-2/Leitner review, 160+ A1 words, a bidirectional English-Turkish learner's dictionary (1,210+ entries with plain-English definitions, a direction selector - `Auto`, `EN → TR`, `TR → EN`, saved with the settings - TTS, CSV import/export, AI lookup with cached results), five study modes, CEFR-aware exams, English spelling and pronunciation labs, 30 grammar topics, local PDF notes, progress reports, Unicode CSV and `.ecapack` transfer, and an optional LM Studio tutor. Prompts and responses are not stored; the token ledger records counts and operational metadata only.

The dictionary can ask LM Studio or an alternative OpenAI-compatible endpoint (NVIDIA NIM by default; any base URL + API key, enabled on the Settings page and selectable as `Auto`, `LM Studio`, `Alternative` or `Off`) for words it does not know; the structured entries (Turkish translation, plain-English definition, example sentence) are cached in the local dictionary and work offline afterwards. The API key is stored in the Windows Credential Manager (`EnglishCourseAI/alt_api_key`; `settings/secrets.json` elsewhere) and never in `settings.json`; the `ENGLISHCOURSEAI_API_KEY` environment variable overrides it. Tests run against a local mock server and never touch the real network or the Credential Manager.

Run from source with Python 3.11+:

```powershell
python -m pip install -r requirements.txt
python .\English_Course_AI.pyw
```

Build the Windows application with `build.bat` from a clean virtual environment that holds only `requirements.txt` plus PyInstaller, pointing `build.bat` at that interpreter with the `PYTHON` environment variable, so nothing from the global `site-packages` is collected into the binary. The outputs are `dist\EnglishCourseAI.exe` and the release archive `dist\EnglishCourseAI-Windows.zip`, which carries the executable together with `LICENSE` and `THIRD_PARTY_NOTICES.md`. User data is stored under `%APPDATA%\EnglishCourseAI`, or under the directory selected with `ECA_HOME`.

The Resource Center links to verified free-access official learning sites and to openly licensed/public-domain collections. It does not bundle third-party course materials, and it preserves access, licence and attribution notes.

## License

English Course AI is released under the MIT License; the full text is in [LICENSE](LICENSE).

The third-party components used by the application and embedded in the packaged builds are listed with their actual licences in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
