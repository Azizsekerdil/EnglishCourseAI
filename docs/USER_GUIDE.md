# English Course AI - User Guide

Version 1.3.0 · Windows and macOS desktop application · Interface languages: Turkish and English

- [1. About this guide](#1-about-this-guide)
- [2. Installation](#2-installation)
- [3. First launch](#3-first-launch)
- [4. Screens](#4-screens)
- [5. The dictionary in detail](#5-the-dictionary-in-detail)
- [6. Artificial intelligence](#6-artificial-intelligence)
- [7. Data management](#7-data-management)
- [8. Shortcuts and tips](#8-shortcuts-and-tips)
- [9. Troubleshooting](#9-troubleshooting)
- [10. Release notes summary](#10-release-notes-summary)
- [11. Frequently asked questions](#11-frequently-asked-questions)
- [12. Licence](#12-licence)

---

## 1. About this guide

This guide covers **English Course AI** version **1.3.0**. The application is a self-contained English study workspace built for learners whose first language is Turkish, and it keeps your data on your own computer. Review, the dictionary, the labs, exams, PDF notes and progress all work without an internet connection; the AI features are optional.

You do not have to read it end to end: if you are just starting, sections [2](#2-installation), [3](#3-first-launch) and [4](#4-screens) are enough; section [5](#5-the-dictionary-in-detail) is for heavy dictionary use, section [6](#6-artificial-intelligence) for connecting an AI provider, and section [9](#9-troubleshooting) for when something does not behave as expected. Button and field names are given as the English interface shows them, with the Turkish label in parentheses where that helps.

## 2. Installation

### Windows (zip)

1. Download `EnglishCourseAI-Windows.zip`.
2. Extract the zip into a folder (do not run it from inside the archive).
3. Double-click `EnglishCourseAI.exe`.

There is no setup wizard, no administrator right and no registry change; the application is a single file and its first start may take a few seconds. Next to `EnglishCourseAI.exe` the zip also carries the project's `LICENSE` (MIT) and `THIRD_PARTY_NOTICES.md`; the same two files are embedded inside the executable.

### macOS (zip, Apple Silicon)

1. Download and expand `EnglishCourseAI-macOS.zip`, then move `EnglishCourseAI.app` into your `Applications` folder.
2. The application is **not notarized**: on the first launch, **right-click** the icon (or Control-click it), choose **Open**, and press **Open** again in the warning dialog.
3. You grant this permission once; afterwards a double-click is enough.

The package targets Apple Silicon and its bundle identifier is `com.englishcourseai.desktop`. `LICENSE` and `THIRD_PARTY_NOTICES.md` live inside the bundle, in `EnglishCourseAI.app/Contents/Resources/`.

### Running from source

Requirement: Python 3.11 or newer. Running from source has a single external dependency, `pypdf` (BSD-3-Clause), used by the PDF Reader. The packaged `.exe` and `.app` builds additionally embed the Python interpreter, Tcl/Tk and PyInstaller's launcher stub; all of them are itemised in [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md).

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python .\English_Course_AI.pyw
```

On macOS and Linux you activate the environment with `source .venv/bin/activate` and use `python English_Course_AI.pyw`.

### Where your data is kept

Learner data is not stored next to the program but in a separate user folder: `%APPDATA%\EnglishCourseAI` on Windows, `~/Library/Application Support/EnglishCourseAI` on macOS, `~/.englishcourseai` on other systems.

| Sub-folder | Content |
| --- | --- |
| `data` | `EnglishCourseAI.db` (all SQLite data) |
| `settings` | `settings.json` and, if needed, `secrets.json` |
| `exports` | The folder suggested for dictionary CSV exports |
| `downloads` | A working folder the application reserves |

For portable use, set the `ECA_HOME` environment variable and the application keeps everything in that folder:

```powershell
$env:ECA_HOME = "E:\EnglishCourseAI-data"
.\EnglishCourseAI.exe
```

## 3. First launch

The window opens at 1360 × 860 (minimum 1080 × 700) and the title bar reads `English Course AI 1.3.0`. There is a grouped page list on the left, a toolbar at the top and a status bar at the bottom. The top bar holds the page title, the `🌐` icon with the **interface language** box (`Türkçe` / `English`), the **+** button that creates a profile, the **profile** box, and at the far right the `AI: Available` / `AI: Unavailable` badge.

On the first launch the application asks you for nothing: it creates the data folder and the `EnglishCourseAI.db` database, creates a default profile named `Alex`, loads the built-in 162-word A1-level starter set into the Word Bank (the words are spread over 20 topical decks such as Temel, Fiiller and Yiyecek), and prepares the 1,210-entry built-in dictionary (no download needed).

You change the **interface language** from the top bar; pages are redrawn immediately and the choice is saved (default: Turkish). To change the **theme**, pick `dark` or `light` in **Settings → Theme** and press **Save** (default: `dark`). The **Daily goal** (default 20) and **Text to speech** (on by default) are also on the Settings page.

**Tip:** To get acquainted, run a short 10-card round on the **Spaced Review** page with the `new` queue, then look up a few words on the **Dictionary EN-TR** page.

## 4. Screens

The left menu lists 18 pages in five groups; the order below is exactly the order in the menu.

| Group | Pages |
| --- | --- |
| LEARN | Spaced Review · Word Bank · Dictionary EN-TR · Exam |
| LABS | Spelling & Sound · Pronunciation · Grammar |
| READ & EXPLORE | Resource Center · PDF Reader · Course Library |
| PRACTICE | AI Tutor · Speaking · Writing & Handwriting |
| PROGRESS & SYSTEM | Progress · Packs · Token Ledger · Offline Guide · Settings |

### LEARN

#### Spaced Review (Aralıklı Tekrar)

**What it does.** Runs your daily review plan with the SM-2 algorithm and Leitner boxes.

**How to use it.** The four cards at the top show the **Due today**, **New**, **Mistakes** and **Favorites** counts. Choose `new`, `due`, `wrong` or `favorites` in the queue box; choose **Cards**, **Multiple choice**, **Typing**, **Listening** or **Matching** in the next box; set the card count (5-50, default 10) and press **Start**. The card shows the word with its plural and part of speech; after **Show answer** you rate yourself with **Again**, **Hard**, **Good** or **Easy**. The card face is the same in every mode; with **Listening** selected the word is also read aloud. When the queue is empty, **Session complete** appears.

**Tip:** A word you mark **Again** returns tomorrow, one you mark **Easy** moves to steadily longer intervals; honest grading keeps the plan accurate.

#### Word Bank (Kelime Bankası)

**What it does.** It is the list of all your study words; review and exams draw from it.

**How to use it.** Type in the box and press **Search** (or Enter); the search covers the English word, the Turkish meaning and the clue field. The table has the columns **English**, **Turkish**, **English clue**, **Article**, **Plural** and **Deck**; selecting a row shows the example sentences below. **★ Favorite** adds or removes the selected word from your favorites. **↑ Export** writes a UTF-8 CSV and **↓ Import** reads a file in the same layout back in.

**Tip:** A word you send here with **★ Add to word bank** in the dictionary lands in the `Dictionary EN-TR` deck and joins your review queue.

#### Dictionary EN-TR (Sözlük EN-TR)

**What it does.** A bidirectional English ↔ Turkish learner's dictionary: 1,210 built-in entries work offline, and words it does not know can be asked of the AI, whose answer is cached locally.

**How to use it.** See section [5](#5-the-dictionary-in-detail) for the full description.

**Tip:** Press **🎲 Random word** to meet a new word; an entry from the built-in deck comes up straight away.

#### Exam (Sınav)

**What it does.** Generates and scores a multiple-choice exam from your word bank.

**How to use it.** Set the **Question count** spinner (5-50, default 10) and press **Start**. Each question shows an English word; tick one of four Turkish options and press **Check**. After the last question, **Exam complete** and **Score: …%** appear and the result is written to your progress log. The CEFR level stored with the exam is read from the `cefr` field of the settings file (default `A1`); this version has no level selector in the interface.

**Tip:** The `wrong` queue is built from the words you graded **Again** or **Hard** in Spaced Review; exam results are stored separately and do not change that queue.

### LABS

#### Spelling & Sound (Yazım ve Ses)

**What it does.** Shows the English spelling-to-sound relationship through 15 rules and offers a short dictation exercise.

**How to use it.** Select a row in the table on the left (an unlabelled symbol column, then the **Spelling and sound rules** and **Examples** columns); the explanation appears in the right panel. In the **Dictation exercise** area, press **▶ Speak** to hear the word, type it into the box and press **Check**: a `✓` for a correct answer, otherwise the correct spelling. The dictation word is fixed in this version and cannot be changed from the interface; it is currently the German `Straße` - a leftover from the sibling German application that will be corrected in the English build.

**Tip:** The spelling check ignores capitalization but treats apostrophes and hyphens as meaningful: `dont` is not the same answer as `don't`.

#### Pronunciation (Telaffuz)

**What it does.** Reads a word out with the computer voice and lists the difficult English sounds side by side.

**How to use it.** Type the word into the box at the top and press **▶ Speak**; in this version the box opens with the German `Mädchen` (the same leftover), so type your own word over it. Below, under **Pronunciation tip**, a 10-row sound table gives the sound name, its IPA spelling and example words (`th` `/θ/ /ð/` → *think, this*). **◉ Compare with microphone** is not active in this version; pressing it shows **Unavailable**, and the application never records audio.

**Tip:** Look the same word up in the dictionary and read its plain-English definition; entries found by the AI also carry an IPA spelling in the **Extra** column.

#### Grammar (Dilbilgisi)

**What it does.** Works through 30 grammar topics with a rule, an example and an exercise.

**How to use it.** Pick a topic in the list on the left (Basic word order, Indefinite articles, Present perfect, Phrasal verbs…); the title, rule and example appear on the right. In the **Exercise** area, tick an option and press **Check**: a `✓` for a correct answer, otherwise the correct answer with an explanation. **Next** draws a new exercise. Exercises are picked at random from a pool of 28 and are not filtered by the selected topic; your results are recorded per topic.

**Tip:** After reading a rule, press **Next** a few times to see different question types instead of getting stuck on one item.

### READ & EXPLORE

#### Resource Center (Kaynak Merkezi)

**What it does.** Links to free-access, public-domain and Creative Commons English resources; it copies no third-party content.

**How to use it.** Each of the eight cards shows the resource name, its level, the **License** and the **Attribution** note (British Council LearnEnglish, BBC Learning English, VOA Learning English, Tatoeba, LibriVox, Project Gutenberg and more). **Open ↗** opens the link in your default browser; the notice at the top of the page, `ⓘ Opening links uses the internet.`, is there as a reminder.

**Tip:** Public-domain status varies by country; check your local situation before sharing anything you download.

#### PDF Reader (PDF Okuyucu)

**What it does.** Reads the text of your own PDF course file page by page and lets you keep a note on every page.

**How to use it.** Press **Choose PDF** and pick the file; its path appears next to the button and is remembered for the next launch. Move around with the **Page** spinner while the left panel shows that page's text (read-only). Type into the **Page note** box on the right and press **Save**; the note is stored per profile, file and page. Text comes from the PDF's text layer, so for scanned PDFs the panel stays empty.

**Tip:** To read a scanned page, take a screenshot of it and hand it to the **Image / OCR** task on the **AI Tutor** page.

#### Course Library (Ders Kitaplığı)

**What it does.** Lists your own files from the `Resources` folder next to the program.

**How to use it.** **Open course folder** opens it in File Explorer (Windows). Copy your PDF, audio or text files in and press **Refresh**; the list shows the file name, type and size in MB. Double-clicking a row opens the file in the system's default application (Windows).

**Tip:** Sub-folders are scanned too, so organising lessons unit by unit does not break the list.

### PRACTICE

#### AI Tutor (AI Öğretmen)

**What it does.** Gives explanation, translation, correction and image/OCR tasks to the local model running in LM Studio.

**How to use it.** Pick **Explain**, **Translate**, **Correct** or **Image / OCR** in the **Task** box, type your text into the upper box and press **Send**; the answer appears in the read-only panel below. For images, use the **Image / OCR** button on the right to choose a `.png`, `.jpg`, `.jpeg` or `.webp` file - the task switches by itself. If local AI is off or LM Studio cannot be reached, the panel reads `AI is disabled or LM Studio cannot be reached.` This page only ever uses LM Studio.

**Tip:** The note at the bottom, `🔒 Prompt and response text is never saved; only token counts are logged.`, is this page's privacy promise.

#### Speaking (Konuşma)

**What it does.** Lets you practise conversation by writing with the local AI in a scenario you choose.

**How to use it.** Pick a scenario in the **Scenario** box (`At a café`, `At the station`, `At a hotel`, `In a shop`, `At the doctor's`) and press **Start conversation**; the other person asks a short question. Type your English reply in the box below and press **Send**. The panel always shows the latest answer, while the previous text is sent to the model as context.

**Tip:** The role-play is written for A1 level, so short, complete sentences give the best results.

#### Writing & Handwriting (Yazma & El Yazısı)

**What it does.** Has the AI correct your free writing and gives you a blank area for handwriting practice.

**How to use it.** Read the prompt on the left (`Write in English about what you did today.`), type your text into the box and press **Correct with AI**; the panel below shows the corrected version, the name of the rule and a short explanation. You can write with the mouse in the **Handwriting area** on the right and empty it with **Clear**. The handwriting area is not saved.

**Tip:** After reading the correction, write the same text once more without looking at it; that second attempt is what makes it stick.

### PROGRESS & SYSTEM

#### Progress (İlerleme)

**What it does.** Shows your daily goal, your streak and how much you studied over the last seven days.

**How to use it.** Open the page: the **Daily goal**, **Day streak**, **Studied** and **Learned** metrics sit at the top, with the **Last 7 days** bar chart and the **Weekly report** line (`Correct`, `Wrong` and `Score` as a percentage) below them.

**Tip:** The streak counts consecutive days studied; short but regular sessions are the easiest way to keep it alive.

#### Packs (Paketler)

**What it does.** Bundles your words (and optionally your progress) into one file you can carry to another computer.

**How to use it.** Tick **Include progress** if you want the progress data too, press **↑ Export** and give the file an `.ecapack` name (the `Pack created` message shows the path). On the other computer, choose the same file with **↓ Import**; the `Pack imported` message tells you how many words arrived. The pack is a zip containing `manifest.json` and `data.json`; a pack made by another language's application is rejected.

**Tip:** Imported words keep the deck names they had on the source computer; only rows with no deck at all fall into `Paket`. The Word Bank cannot filter by deck and its search box covers only the English word, the Turkish meaning and the English clue, so read the deck from the **Deck** column.

#### Token Ledger (Token Defteri)

**What it does.** Keeps a numeric summary of AI calls and contains no text.

**How to use it.** At the top are the **Calls** and **Total tokens** metrics; below is a table of the last 500 calls: timestamp, model, task, prompt tokens, completion tokens, total, milliseconds and success flag.

**Tip:** If your alternative endpoint is paid, watch your spending here; the **Task** column takes the values `dictionary`, `grammar`, `translate`, `correct`, `dialogue` and `vision`.

#### Offline Guide (Çevrimdışı Kılavuz)

**What it does.** The short in-app help text: which features are fully local, how the dictionary directions work, and what the CSV columns are.

**How to use it.** Open the page and read it; at the very bottom, below the separator line, is the **full path of your data folder**. Use that path when making backups.

**Tip:** In an offline setting this is the fastest reference you have.

#### Settings (Ayarlar)

**What it does.** Collects the theme, goal, speech, local AI and alternative endpoint options.

**How to use it.** Edit the fields and press **Save**; `Settings saved` appears. If you changed the theme, the window is redrawn.

| Field | Meaning | Default |
| --- | --- | --- |
| **Theme** | `dark` / `light` | `dark` |
| **Daily goal** | Daily card target (5-200) | 20 |
| **Text to speech** | Speech on/off | on |
| **Local AI** | LM Studio use on/off | on |
| **LM Studio address** | Address of the local server | `http://127.0.0.1:1234` |
| **Default model** | Preferred model name for tasks | `qwen2.5-7b-instruct` |
| **Dictionary AI provider** | `Auto` / `LM Studio` / `Alternative` / `Off` | `Auto` |
| **Save AI dictionary results into the dictionary** | Caches AI entries | on |
| **Use the alternative endpoint** | Enables the second provider | off |
| **Base URL** | OpenAI-compatible address | `https://integrate.api.nvidia.com/v1` |
| **Model** | Model name at the alternative endpoint | `meta/llama-3.1-8b-instruct` |
| **API key** | Moved into secure storage when typed | empty |

**Tip:** The **Default model** box lists the built-in profiles but also accepts free text; type the exact name of the model loaded in LM Studio.

## 5. The dictionary in detail

The **Dictionary EN-TR** page merges three layers: the **1,210 built-in entries** inside the program, the entries you add yourself, and the entries the AI finds and caches. Every entry has an English headword, Turkish meaning(s), a part of speech and a plain-English definition; irregular verb and plural forms are appended to the definition after a ` — ` mark (the `tooth` entry ends with `— plural: teeth`). The **Extra** (IPA) and **Example sentence** fields are empty in the built-in entries; they are filled in the entries the AI finds and the ones you add yourself.

### The direction selector

The **Direction:** box on the second toolbar row offers three options.

| Option | Side searched | When to choose it |
| --- | --- | --- |
| **Auto** | The English headword/definition and the Turkish meaning together; the highest-scoring side wins and the headword wins a tie | Everyday use, when you do not want to think about which language you are typing |
| **EN → TR** | The English headword and the English definition only | When you want the Turkish meaning of an English word |
| **TR → EN** | The Turkish meaning only | When you want the English word for a Turkish one |

A fixed direction searches only its own source side, which is why typing `house` while `TR → EN` is selected returns nothing. That is not a fault but what the direction means. Your choice is saved with the settings and survives a restart; changing the direction repeats the query in the box in the new direction. The small label to the right of the search box shows the effective direction after a search (`EN → TR` or `TR → EN`); in **Auto** mode that is the direction the application detected for you.

### The Turkish column and the detail panel

The table on the left has five columns.

| Column | Content |
| --- | --- |
| **English** | The headword |
| **Turkish** | The meaning(s); several are separated by `;` |
| **Part of speech** | `noun`, `verb`, `adjective`, `adverb`, `pronoun`, `preposition`, `conjunction`, `numeral`, `article`, `interjection`, `particle`, `phrase` |
| **Extra** | The IPA spelling (like `/brɪdʒ/`); empty in the built-in entries |
| **Source** | `built-in`, `user` or `AI` |

Selecting a row opens the panel on the right: the headword in large type, a line with the part of speech and the extra field, the **Turkish:** meaning, the example sentence in quotation marks, the plain-English definition and, when the word is already in your word bank, a `★ Word Bank: … (deck)` line. The buttons are **🔊 Speak**, **✦ Ask AI**, **Copy**, **★ Add to word bank** and, only while an unsaved AI entry is selected, **💾 Save to dictionary**. Below them sit the **Recent lookups** list, which holds your last 12 queries, and the **AI answer** panel; at the very bottom a counter reads `1210 entries · built-in 1210 · user 0 · AI 0`.

### Search rules

- The list filters live **from the second character** you type; this live search sends no request to the AI.
- **Enter** or **Search** runs the full search: the query is added to your history and, if there is no result, the AI may be asked.
- Ranking: **exact match** > exact match after stripping `to`/`the`/`a`/`an` > **prefix** > **word start** > **substring** (at least three characters) > a match found only in the definition.
- Search ignores case and diacritics; Turkish letters fold to their plain equivalents (`ç/c`, `ğ/g`, `ş/s`, `ö/o`, `ü/u`) and `İ`, `I` and `ı` all search as `i`. `IŞIK`, `ışık` and `isik` return the same result.
- **Irregular forms** are found because they live inside the definition: `teeth` finds `tooth`, and `went` also finds `go`.
- A single search returns at most 200 results.

### Source labels

| Label | Meaning |
| --- | --- |
| **built-in** | One of the 1,210 entries shipped with the program; it cannot be deleted and is identical in every installation |
| **user** | An entry you added with **+ Add entry** or imported from CSV |
| **AI** | An entry the AI found, cached into the local dictionary |

The part-of-speech line in the detail panel also ends with `· AI` for AI entries.

### Filling a missing meaning with AI

When you look up a word the dictionary does not have and the **AI:** policy is not `Off`:

1. The status bar reads `Not found in the dictionary. Ask the AI or add it yourself.` and the AI is asked in the background (`Asking the AI…`).
2. The answer comes back as structured JSON: headword, part of speech, IPA, Turkish meaning, example sentence and plain-English definition; at most 5 entries per query.
3. If **Save AI dictionary results into the dictionary** is on (the default), the entries are written into the local dictionary and the next lookup of the same word is found offline.
4. The entries appear at the top of the list with the `AI` source and are printed in the **AI answer** panel, ending with an `— Answered by: LM Studio · …` line.
5. If the AI finds nothing, the panel reads `The AI returned no entry for this query.`

**✦ Ask AI** asks even when the dictionary did find something and puts the returned entries above the local results. With auto-saving off the entries are temporary; to keep one, select it and press **💾 Save to dictionary**. If you change the query before the answer arrives, the stale answer is not printed (`The query changed, so the previous AI answer is not shown.`) but the entries that were produced are still saved **when auto-saving is on**; with it off they are discarded.

### Adding to the word bank

Press **★ Add to word bank** on the selected entry. The word is written into the Word Bank under the `Dictionary EN-TR` deck, carrying the first meaning into the Turkish field along with the example sentence and the definition. The status bar shows `Added to word bank: …`, the detail panel gains the `★ Word Bank: …` line, and the word is now part of the Spaced Review and Exam pool.

### CSV import and export

**↑ Export CSV** writes the result list on screen, or the whole dictionary when there is none; the dialog suggests the `exports` folder and the name `dictionary_en.csv`.

| # | Column | Content |
| --- | --- | --- |
| 1 | `headword` | The English headword |
| 2 | `translation` | The Turkish meaning(s), separated by `;` |
| 3 | `pos` | The part-of-speech code (`n`, `v`, `adj`, `adv`, `pron`, `prep`, `conj`, `num`, `art`, `int`, `part`, `phr`) |
| 4 | `extra` | The IPA spelling, or empty |
| 5 | `note` | The plain-English definition |
| 6 | `source` | `builtin`, `user` or `ai` |
| 7 | `example` | The example sentence |

```csv
headword,translation,pos,extra,note,source,example
house,ev,n,,a building where people live,builtin,
tooth,diş,n,,one of the hard white things in your mouth — plural: teeth,builtin,
bridge,köprü,n,/brɪdʒ/,a structure built over a river or road,user,We walked across the old bridge.
```

**↓ Import CSV/TSV** reads `.csv`, `.tsv` and `.txt` files and detects the delimiter itself. A header row is recognised and the **columns may come in any order**: `word`, `target`, `en` and `english` mean the headword; `meaning`, `tr`, `turkish` and `türkçe` mean the translation; `definition` means the note column. Without a header row the order above applies. Rows with an empty headword or translation are skipped, entries are stored with the `user` source, and the same (headword, translation) pair is never added twice. When it finishes, the status bar reads `N entries imported`.

### Adding an entry

**+ Add entry** opens a small window; text in the search box is pre-filled into the matching field according to the detected direction.

| Field | Required | Description |
| --- | --- | --- |
| **English** | yes | The headword (dictionary form) |
| **Turkish** | yes | The meaning; separate several with `;` |
| **Part of speech (n/v/adj/…)** | no | The part-of-speech code |
| **Extra** | no | The IPA spelling |
| **Note / definition** | no | A plain-English definition |
| **Example sentence** | no | A short example |

**Save** (or Enter) adds the entry with the `user` source and searches for it straight away; if either required field is empty you get `English and Turkish fields are required.` **Esc** closes the window.

## 6. Artificial intelligence

### Installing LM Studio and its local server

1. Install LM Studio and download a chat model.
2. Start the OpenAI-compatible **Local Server**.
3. The default address is `http://127.0.0.1:1234`; if you use another port, type it into **Settings → LM Studio address** and press **Save**.

The application talks to the server through `GET /v1/models` and `POST /v1/chat/completions`. With LM Studio closed the application keeps working; only the AI features are disabled.

### Choosing a model

If the **Default model** from Settings is installed it is used directly; otherwise a per-task profile list is tried, and failing that the installed models are ranked and the most suitable one is picked.

| Task | Preference order |
| --- | --- |
| `chat`, `dialogue`, `dictionary` | `qwen2.5-7b-instruct`, `llama-3.1-8b-instruct` |
| `grammar`, `correct` | `qwen2.5-7b-instruct`, `qwen2.5-14b-instruct` |
| `translate` | `qwen2.5-7b-instruct`, `gemma-2-9b-it` |
| `vision` | `qwen2-vl-7b-instruct`, `llava-v1.6-mistral-7b` |

**Why specialist models are skipped.** Embedding (`embed`), reranking (`rerank`), maths (`math`), code (`coder`, `code-`), vision (`vision`, `-vl`, `llava`, `moondream`, `clip`), medical (`bio`, `medic`), audio (`whisper`, `tts`, `audio`) and image-generation (`sd-`, `stable-diffusion`) models are useless for dictionary and chat work; a model whose name carries one of these traces is pushed to the end and used only when nothing else exists. On a tie, general models of 4-16 billion parameters with `instruct`, `chat` or `-it` in the name are preferred, because that size fits an ordinary laptop.

**Thinking models.** Some models spend the whole budget on reasoning and return an empty answer. The application sends `reasoning_effort: "none"` to local servers; if the server rejects the field the request is retried without it. When the answer is empty and truncated, it is tried once more with three times the budget.

### The alternative endpoint

Instead of, or alongside, LM Studio the dictionary can use any OpenAI-compatible service: NVIDIA NIM, OpenRouter, Groq, an Ollama server on your network, and so on.

1. Find the **Alternative endpoint** group on the **Settings** page and tick **Use the alternative endpoint**.
2. Type the address into **Base URL** (default `https://integrate.api.nvidia.com/v1`) and the model name into **Model** (default `meta/llama-3.1-8b-instruct`).
3. Paste your key into **API key**; the field is masked with bullet characters (•).
4. Press **Save**: the field clears and `••••• stored` appears beside it.
5. Try it with **Test connection**; you should see `Connection OK · N models`. If the model is not listed, `selected model not listed` is appended; if the key is missing, `the dictionary will not use this endpoint until a key is stored` warns you.

Remote addresses starting with `https://` require a key; loopback addresses such as `127.0.0.1` and `localhost`, and plain `http://` servers on your network, are accepted without one.

**Where your key is stored.** On Windows the key lives in the **Windows Credential Manager** as a generic credential named `EnglishCourseAI/alt_api_key`; on other systems, or if that API fails, it falls back to `settings/secrets.json` (with 0600 permissions where the platform supports it). The key is **never** written into `settings.json`. If `ENGLISHCOURSEAI_API_KEY` is set, it overrides the stored key. The **Delete key** button removes the record (`Key deleted`).

### The AI policy

**Dictionary AI provider** appears both on the Settings page and in the **AI:** box on the dictionary toolbar; both show the same setting.

| Policy | Behaviour |
| --- | --- |
| **Auto** | Uses LM Studio when reachable; otherwise the alternative endpoint if it is enabled; otherwise no AI is used |
| **LM Studio** | The local server only; **Local AI** must be on and the server reachable |
| **Alternative** | The alternative endpoint only; it must be enabled and, where required, have a stored key |
| **Off** | The dictionary sends no AI request; AI Tutor, Speaking and Writing & Handwriting are unaffected |

The toolbar label shows what the selected policy amounts to right now: `LM Studio: connected`, `Alternative: ready`, `AI unreachable` or `AI off`. The reachability answer is cached for 30 seconds, so the label may lag if you have just started LM Studio. Only the **Dictionary** page uses the alternative endpoint; **AI Tutor**, **Speaking** and **Writing & Handwriting** always go through LM Studio.

### The token ledger and privacy

Every call adds one row to the **Token Ledger**: timestamp, model, task, prompt tokens, completion tokens, total, elapsed milliseconds and success flag. **Prompt and response text are stored nowhere** - neither in the database nor in log files. Dictionary questions go to the model with a temperature of 0.1, a budget of at most 1,200 tokens and a 90-second timeout.

## 7. Data management

**Profiles.** The box in the top bar switches profiles and the **+** button creates one (it asks for a name). Kept per profile: the review schedule and progress, the study log, exams, PDF page notes and grammar statistics. Shared: the Word Bank, the dictionary entries, the token ledger and the settings. There is no profile deletion in the interface.

**Backups.**

| Method | Covers | How |
| --- | --- | --- |
| Database copy | Everything | Copy `…\EnglishCourseAI\data\EnglishCourseAI.db` while the application is closed |
| Word CSV | The Word Bank | **Word Bank → ↑ Export** |
| Dictionary CSV | Dictionary entries | **Dictionary EN-TR → ↑ Export CSV** |
| Pack file | Words (+ progress, optionally) | **Packs → ↑ Export** (`.ecapack`) |

**The data folder and resetting.** You will find the full path at the bottom of the **Offline Guide** page. Close the application; to reset everything, delete or rename the data folder (a fresh installation is created on the next launch); to reset only the settings, delete `settings/settings.json`; to experiment, point `ECA_HOME` at a temporary folder. The API key is not in the data folder but in the operating system's secure store, so deleting the folder does not delete it - use **Settings → Delete key** for that.

## 8. Shortcuts and tips

The application has no menu accelerators; the following are the real shortcuts defined in the code.

| Shortcut | Where | What it does |
| --- | --- | --- |
| **Enter** | Dictionary search box | Runs the full search (asking the AI when needed) |
| Typing two or more characters | Dictionary search box | Filters instantly, sends no AI request |
| **Double-click** | Dictionary result list | Speaks the selected entry |
| **Enter** | Word Bank search box | Runs the search |
| **Enter** | Add entry window | Saves the entry |
| **Esc** | Add entry window | Closes the window |
| **Double-click** | Course Library list | Opens the file in the default application (Windows) |

- **Fix the direction:** when mining vocabulary from a long Turkish text, `TR → EN` removes accidental matches completely.
- **🎲 Random word** draws a built-in entry whose relevant side is known for the selected direction, so it always finds a result even in a fixed direction and never triggers a needless AI request.
- Clicking a line in **Recent lookups** repeats that lookup.
- **Copy** puts the entry on the clipboard as `word — meaning`.
- The Settings page re-reads the current values every time it opens, so an AI policy changed on the dictionary toolbar is reflected there too.

## 9. Troubleshooting

**LM Studio cannot be reached (`AI: Unavailable`, `AI unreachable`).** Usually the local server has not been started: open LM Studio and start the Local Server. Then check that the **LM Studio address** in Settings matches the address and port LM Studio reports, and press **Save**; saving refreshes the clients. Make sure the **Local AI** box is ticked. Because the reachability answer is cached for 30 seconds the label may not change immediately; once those 30 seconds have passed, leaving the dictionary page and coming back re-measures it. The `AI:` badge in the top bar is measured only at startup and is not refreshed afterwards.

**The AI returns an empty answer (`The AI returned no entry for this query.`).** The most common cause is a "thinking" model spending the budget on reasoning; the application retries once with three times the budget. If it is still empty, load a non-thinking `instruct` model of 4-16 billion parameters in LM Studio and type its name into **Default model**. A model too large for your memory makes answers very slow or truncated, and if the only installed model is a maths, embedding or vision model the dictionary cannot produce a meaningful answer.

**A word has no Turkish meaning / nothing is found.** Check the direction first: `TR → EN` searches Turkish meanings only and `EN → TR` the English side only; switch to **Auto** if in doubt. If the word is not in the built-in dictionary and the AI policy is `Off` or the provider is unreachable, the message `Not found in the dictionary…` stays on screen. Then either connect a provider, add the word yourself with **+ Add entry**, or import a ready-made CSV list.

**macOS says the application "cannot be opened".** The package is not notarized: right-click (or Control-click) the icon, choose **Open**, and press **Open** again in the warning. Once allowed, a double-click works. If the warning keeps coming back, use the **Open Anyway** button at the bottom of **System Settings → Privacy & Security**.

**There is no sound.** Speech calls the Windows `System.Speech` component through PowerShell and picks the first installed `en-*` voice. With no English voice package you hear the default voice or nothing at all; add an English voice from the Windows settings and verify that **Settings → Text to speech** is ticked. On macOS and Linux this component does not exist, so speech silently does nothing.

**The exe will not start.** Do not run it from inside the zip; extract it first. If SmartScreen warns you, choose **More info → Run anyway**. Some antivirus products quarantine PyInstaller-packaged files; check the quarantine list and add the folder to the exclusions if necessary. If `%APPDATA%` is write-protected the application cannot create its data folder; point `ECA_HOME` at a writable folder.

**Where is my data?** The full path is printed at the bottom of the **Offline Guide** page: `%APPDATA%\EnglishCourseAI` on Windows, `~/Library/Application Support/EnglishCourseAI` on macOS, `~/.englishcourseai` on other systems. If `ECA_HOME` is set, that folder wins.

## 10. Release notes summary

| Version | Highlights |
| --- | --- |
| **v1.0.0** | First release: 17 pages, SM-2/Leitner review, the 162-word A1-level starter set, exams, spelling/pronunciation/grammar labs, PDF notes, the Resource Center, packs, the LM Studio AI Tutor, Turkish and English interfaces |
| **v1.1.0** | The **Dictionary EN-TR** tab (1,210 built-in entries, bidirectional lookup, speech, CSV import/export) and the dictionary's **AI connection**: LM Studio or an OpenAI-compatible alternative endpoint, the key kept in the Credential Manager, results cached into the local dictionary |
| **v1.1.1** | Fix for empty answers from thinking models (`reasoning_effort`) and model selection that filters out specialist models |
| **v1.1.2** | Dictionary AI polish: cleanup of the extra field, a direction label after an AI answer, the toolbar moved onto its own row, repeated senses removed |
| **v1.2.0** | The **direction selector**: `Auto`, `EN → TR`, `TR → EN`; a fixed direction searches only its source side and the choice is saved with the settings. Turkish is handled as a full third language in the dictionary engine, and CSV import recognises the header row and accepts the columns in any order |
| **v1.2.1** | **ASCII and capital-letter support in Turkish lookup**: `sinav` = `SINAV` = `sınav`, `cok` = `çok`, `ogrenci` = `öğrenci`. The Turkish column is folded to ASCII for comparison, the displayed spelling never changes, and a folded match is ranked below a direct one, so someone who types `ask` still gets the English word. This **user guide** (Turkish and English) was also added to the repository; the PDF version is published with the release assets |
| **v1.3.0** | The project is published under the **MIT License**; `LICENSE` and `THIRD_PARTY_NOTICES.md` were added at the repository root and now travel inside the distributed packages as well (the Windows `.zip` and `.exe`, the macOS `.app`). The packages are built in a **clean virtual environment**: only the libraries listed in `requirements.txt` are collected, the file size drops, and the third-party notice ships with the package |

## 11. Frequently asked questions

**1. Do I need an internet connection?** No. Review, the Word Bank, the dictionary (1,210 built-in entries), exams, the labs, PDF notes, packs and progress are fully local. The internet is used only for Resource Center links and the alternative remote endpoint.

**2. Is the application useful without AI?** Yes. Set the AI policy to `Off` and **the dictionary** sends no request and keeps working from its built-in entries; the AI Tutor, Speaking and **Correct with AI** features are unaffected - to switch those off too, untick **Settings → Local AI**.

**3. How many entries does the dictionary have?** 1,210 ship with the program, plus your own entries and the ones cached by the AI. The counter at the bottom of the dictionary page shows the current total broken down by source.

**4. Which direction option should I use?** **Auto** is enough for everyday work; if you work in one direction only, the matching fixed direction removes accidental matches completely. Your choice is saved.

**5. Why do I get no result for an English word while `TR → EN` is selected?** Fixed directions search only their own source side, and `TR → EN` looks at Turkish meanings only. Switch to **Auto** or set the direction to `EN → TR`.

**6. Is my API key safe?** On Windows it is kept in the Credential Manager, on other systems only in a local secrets file. It is never written into the settings file and never appears in exports or packs; remove it at any time with **Delete key**.

**7. Is what I send to the AI stored?** No. Neither the prompt nor the response text is saved; the Token Ledger keeps only the model, the task, the token counts, the elapsed time and the success flag.

**8. How do I move my data to another computer?** The easiest way is to export an `.ecapack` file from the **Packs** page and import it on the other machine; to move everything exactly, copy `EnglishCourseAI.db` from the data folder.

**9. How do I add my own words?** Add them to the dictionary one by one with **+ Add entry** or in bulk with **↓ Import CSV/TSV**; use **★ Add to word bank** to put an entry into your study list. The Word Bank also has its own CSV import.

**10. Can I change the exam level?** This version has no CEFR selector in the interface; the `cefr` value from the settings file (`A1` by default) is written into the exam record. You can set the number of questions with the **Question count** spinner.

**11. Why can I not compare my pronunciation with the microphone?** **◉ Compare with microphone** is not active in this version and shows **Unavailable**; the application does not record audio. Use the Pronunciation page for listening and IPA comparison.

**12. Can two people use the same computer?** Yes. Create a second profile with the **+** button; the review schedule, exams, PDF notes and statistics are kept per profile, while the word list, the dictionary and the settings are shared.

## 12. Licence

English Course AI is released under the MIT License; the full text is in [`LICENSE`](../LICENSE) at the root of the repository. The vocabulary, dictionary, grammar and exercise content that ships with the application was written for this project and is covered by the same licence.

Every third-party component the application uses, and everything embedded in the packaged builds (the Windows `.exe` and the macOS `.app`), is listed with its actual licence in [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md). The external sites in the Resource Center are not copied into the application; anything you download from them stays under its own licence.
