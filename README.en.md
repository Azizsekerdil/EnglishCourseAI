# English Course AI

English Course AI is an independent Windows desktop study workspace that keeps core learning data local. Turkish and English interfaces provide the same feature set, while the vocabulary, spelling, pronunciation and grammar content is tailored to English.

Core features include SM-2/Leitner review, 160+ A1 words, five study modes, CEFR-aware exams, English spelling and pronunciation labs, 30 grammar topics, local PDF notes, progress reports, Unicode CSV and `.ecapack` transfer, and an optional LM Studio tutor. Prompts and responses are not stored; the token ledger records counts and operational metadata only.

Run from source with Python 3.11+:

```powershell
python -m pip install -r requirements.txt
python .\English_Course_AI.pyw
```

Build the Windows application with `build.bat`; the output is `dist\EnglishCourseAI.exe`. User data is stored under `%APPDATA%\EnglishCourseAI`, or under the directory selected with `ECA_HOME`.

The Resource Center links to verified free-access official learning sites and to openly licensed/public-domain collections. It does not bundle third-party course materials, and it preserves access, licence and attribution notes.
