import json
import time
import tkinter as tk
from types import SimpleNamespace

import pytest

from eca import config as C
from eca import secrets
from eca.ai_client import AIClient
from eca.app import App, TAB_SPECS


@pytest.fixture(scope="module")
def app():
    try: instance = App()
    except tk.TclError: pytest.skip("No Windows display")
    instance.withdraw(); instance.update(); yield instance; instance.on_close()


def test_window_opens_and_all_tabs_build(app):
    assert len(app._tabs) == len(TAB_SPECS) == 18
    for key, _cls, _icon, _group in TAB_SPECS:
        app.select(key); app.update(); assert app.current_page().winfo_exists()


def test_language_switch_is_immediate_and_persistent(app):
    app.select("tab.study"); app.set_ui_language("en"); app.update()
    assert app.page_title.cget("text") == "Spaced Review" and app.language_var.get() == "English"
    assert C.load_settings()["ui_lang"] == "en"
    app.set_ui_language("tr"); app.update()
    assert app.page_title.cget("text") == "Aralıklı Tekrar" and app.language_var.get() == "Türkçe"


def test_card_session_can_complete(app):
    app.set_ui_language("tr"); app.select("tab.study"); tab = app.current_page(); tab.limit.set(5); tab.start("new")
    assert len(tab.session) == 5
    for _ in range(5): tab.reveal(); tab.grade(4); app.update()
    assert tab.session == []


def test_exam_can_generate_and_finish(app):
    app.select("tab.exam"); tab = app.current_page(); tab.count.set(5); tab.start(); assert len(tab.questions) == 5
    while tab.idx < len(tab.questions):
        tab.choice.set(tab.questions[tab.idx].answer); tab.submit(); app.update()
    row = app.repos.db.one("SELECT score FROM exams WHERE id=?", (tab.exam_id,)); assert row["score"] == 100.0


def test_ai_offline_page_does_not_crash(app):
    app.settings["ai_enabled"] = False; app.select("tab.ai"); tab = app.current_page(); tab.input.insert("1.0", "Test"); tab.send(); app.update()
    assert app.t("ai.status_off") in tab.output.get("1.0", "end")


def _pump(app, predicate, timeout=10.0):
    """Run the Tk event loop until ``predicate()`` holds (background AI work lands via app.run_async)."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        app.update()
        if predicate(): return True
        time.sleep(0.05)
    return False


def _ai_rows(tab):
    return [i for i in tab.tree.get_children() if tab.tree.set(i, "src") == tab.t("dict.ai_source")]


def test_dictionary_falls_back_to_ai_and_caches_results(app, mock_ai):
    app.settings.update({"ai_enabled": True, "ai_base": mock_ai.base, "dict_ai": "local", "dict_ai_autosave": True}); app.refresh_ai_clients()
    app.select("tab.dictionary"); tab = app.current_page(); app.update()
    assert tab.policy.get() == app.t("dict.ai_local")
    tab.query.set("zzqqxxelevenses"); tab.search()
    assert app.t("dict.ai_asking") in tab.ai_out.get("1.0", "end")
    assert _pump(app, lambda: _ai_rows(tab)), "AI results did not arrive"
    entry = tab.current(); sample = mock_ai.sample[0]
    assert entry is not None and entry.source == "ai" and entry.headword == sample["headword"]
    assert sample["translation"].split("; ")[0] in tab.w_trans.cget("text") and sample["example"] in tab.w_example.cget("text")
    assert tab.w_note.cget("text") == sample["note"] and app.t("dict.ai_source") in tab.w_meta.cget("text")
    if C.TARGET_LANG == "en":                                                        # the IPA is shown as is, never as a plural
        assert sample["extra"] in tab.w_meta.cget("text") and app.t("words.plural") not in tab.w_meta.cget("text")
    out = tab.ai_out.get("1.0", "end")
    assert app.t("dict.answered_by") in out and mock_ai.MODEL in out and app.t("dict.ai_local") in out and sample["headword"] in out
    assert mock_ai.count("/chat/completions") == 1 and mock_ai.chats[-1]["auth"] == ""
    assert not tab.save_btn.winfo_manager()                                          # autosaved -> no extra button
    # cached: persisted with source "ai", instantly found offline next time, no second request
    assert app.repos.dictionary.count("ai") >= 1 and any(r["source"] == "ai" and r["example"] == sample["example"] for r in app.repos.dictionary.all())
    tab.query.set(sample["headword"]); tab.search(); app.update()
    assert tab.current().source == "ai" and mock_ai.count("/chat/completions") == 1
    assert _pump(app, lambda: tab.ai_state.cget("text") == app.t("dict.state_local"), 5)
    # "Ask AI" merges AI entries on top of local hits and works for word-bank export with the example sentence
    tab.query.set({"de": "Haus", "fr": "maison", "en": "house"}[C.TARGET_LANG]); tab.search(); app.update()
    assert tab.current().source == "builtin"
    tab.ask_ai(); assert _pump(app, lambda: mock_ai.count("/chat/completions") == 2 and _ai_rows(tab))
    assert tab.tree.get_children()[0] in _ai_rows(tab) and len(tab.results) > len(mock_ai.sample)
    tab.add_to_bank(); word = app.repos.words.search(sample["headword"])[0]
    assert word["example_target"] == sample["example"]


def test_dictionary_policy_off_makes_no_ai_request(app, mock_ai):
    app.settings.update({"ai_enabled": True, "ai_base": mock_ai.base, "dict_ai": "off"}); app.refresh_ai_clients()
    app.select("tab.dictionary"); tab = app.current_page(); app.update()
    assert tab.policy.get() == app.t("dict.ai_off") and tab.ai_state.cget("text") == app.t("dict.state_off")
    tab.query.set("qqzzxxnothing"); tab.search()
    _pump(app, lambda: False, 1.0)
    assert mock_ai.count("/chat/completions") == 0 and tab.tree.get_children() == ()
    assert app.t("dict.no_result") in tab.ai_out.get("1.0", "end")
    tab.ask_ai(); app.update()
    assert app.t("ai.status_off") in tab.ai_out.get("1.0", "end") and mock_ai.count() == 0
    # unreachable local provider: offline text, no crash, no hang
    app.settings.update({"dict_ai": "local", "ai_base": "http://127.0.0.1:9"}); app.refresh_ai_clients()
    tab.query.set("qqzzxxnothing"); tab.search()
    assert _pump(app, lambda: app.t("ai.status_off") in tab.ai_out.get("1.0", "end"), 5)
    tab.policy.set(app.t("dict.ai_auto")); tab._policy_changed()
    assert C.load_settings()["dict_ai"] == "auto"


def _slow(content, delay=0.8):
    """Mock reply that takes ``delay`` seconds, like a local model."""
    return lambda _body: (time.sleep(delay), content)[1]


def test_dictionary_keeps_ai_answer_on_inert_keys_and_caches_stale_answers(app, mock_ai):
    app.settings.update({"ai_enabled": True, "ai_base": mock_ai.base, "dict_ai": "local", "dict_ai_autosave": True}); app.refresh_ai_clients()
    app.select("tab.dictionary"); tab = app.current_page(); app.update()
    mock_ai.content = _slow(mock_ai.content)
    tab.query.set("zzqqxxslow"); tab.search(); _pump(app, lambda: False, 0.2)
    for key in ("Left", "Right", "Home", "End", "Shift_L", "Control_L", "Alt_L", "Tab", "Escape", "Return", "Up", "Down"):
        tab._on_key(SimpleNamespace(keysym=key))                                     # KeyRelease events that leave the text untouched
    assert app.t("dict.ai_asking") in tab.ai_out.get("1.0", "end")
    assert _pump(app, lambda: _ai_rows(tab), 5), "a non-editing key discarded the in-flight AI answer"
    assert mock_ai.count("/chat/completions") == 1 and tab.current().headword == mock_ai.sample[0]["headword"]
    assert app.status.get() != app.t("dict.ai_asking")
    # the text changes while the AI is still answering: the answer is not shown for the new text, but it is cached and the panel moves on
    mock_ai.content = _slow('```json\n[{"headword": "Qqzzstale", "pos": "n", "extra": "", "translation": "bayat-şey", "example": "Qqzzstale!", "note": "x"}]\n```')
    before = app.repos.dictionary.count("ai")
    tab.query.set("qqzzstale"); tab.search(); _pump(app, lambda: False, 0.2)
    tab.query.set("qqzzstalex"); tab._on_key(SimpleNamespace(keysym="x"))
    assert _pump(app, lambda: app.t("dict.ai_stale") in tab.ai_out.get("1.0", "end"), 5), "stale answer left 'Asking…' on screen"
    assert _ai_rows(tab) == [] and tab.query.get() == "qqzzstalex" and app.status.get() == app.t("dict.ai_stale")
    assert app.repos.dictionary.count("ai") == before + 1 and "Qqzzstale" in tab.ai_out.get("1.0", "end")
    tab.query.set("qqzzstale"); tab.search(); app.update()                          # the paid-for answer is served from the cache
    assert tab.current().headword == "Qqzzstale" and tab.current().source == "ai" and mock_ai.count("/chat/completions") == 2


def test_settings_page_reflects_settings_changed_elsewhere(app):
    app.select("tab.dictionary"); dtab = app.current_page(); app.update()
    dtab.policy.set(app.t("dict.ai_off")); dtab._policy_changed()
    assert C.load_settings()["dict_ai"] == "off"
    app.settings["ai_enabled"] = False                                               # toggled outside the settings page
    app.select("tab.settings"); stab = app.current_page(); app.update()
    assert stab.dict_ai.get() == app.t("dict.ai_off") and not stab.ai.get()
    stab.save(); app.update()                                                        # Save must not revert the toolbar choice
    assert C.load_settings()["dict_ai"] == "off" and app.settings["dict_ai"] == "off" and C.load_settings()["ai_enabled"] is False
    app.settings.update({"ai_enabled": True, "dict_ai": "auto"}); C.save_settings(app.settings)
    app.select("tab.settings"); app.update()
    assert stab.dict_ai.get() == app.t("dict.ai_auto") and stab.ai.get()


def test_settings_test_connection_warns_when_dictionary_would_need_a_key(app, mock_ai, monkeypatch):
    secrets.delete_secret("alt_api_key"); app.refresh_ai_clients()
    app.select("tab.settings"); tab = app.current_page(); app.update()
    tab.alt_base.set(mock_ai.base); tab.alt_model.set(mock_ai.MODEL); tab.alt_key.set("")
    tab.test_alt(); assert _pump(app, lambda: app.t("settings.alt_ok") in tab.alt_result.cget("text"), 5)
    assert app.t("settings.alt_key_needed") not in tab.alt_result.cget("text")     # plain http without a key: the dictionary can use it
    monkeypatch.setattr(AIClient, "needs_key", property(lambda self: True))         # behave like a hosted https API
    tab.test_alt(); assert _pump(app, lambda: app.t("settings.alt_key_needed") in tab.alt_result.cget("text"), 5)
    assert app.t("settings.alt_ok") in tab.alt_result.cget("text")


def test_settings_alt_endpoint_keeps_key_out_of_settings_and_drives_dictionary(app, mock_ai):
    app.select("tab.settings"); tab = app.current_page(); app.update()
    assert tab.key_state.cget("text") == app.t("settings.alt_key_none")
    tab.alt_enabled.set(True); tab.alt_base.set(mock_ai.base); tab.alt_model.set(mock_ai.MODEL); tab.alt_key.set("nvapi-ui-secret")
    tab.dict_ai.set(app.t("dict.ai_alt")); tab.dict_autosave.set(False); tab.save(); app.update()
    assert "nvapi-ui-secret" not in C.SETTINGS_PATH.read_text(encoding="utf-8")
    assert secrets.get_secret("alt_api_key") == "nvapi-ui-secret" and tab.alt_key.get() == ""
    assert tab.key_state.cget("text") == app.t("settings.alt_key_saved")
    assert app.ai_alt.api_key == "nvapi-ui-secret" and app.ai_alt.base == mock_ai.base and app.ai_alt.model == mock_ai.MODEL
    assert C.load_settings()["dict_ai"] == "alt" and C.load_settings()["alt_enabled"] is True
    tab.test_alt(); assert _pump(app, lambda: app.t("settings.alt_ok") in tab.alt_result.cget("text"), 5)
    assert mock_ai.requests[-1]["auth"] == "Bearer nvapi-ui-secret"
    # dictionary now answers through the alternative client with the bearer key; autosave off -> "Save" button
    app.select("tab.dictionary"); dtab = app.current_page(); app.update()
    assert dtab.policy.get() == app.t("dict.ai_alt")
    mock_ai.content = '```json\n[{"headword": "Qqzzalt", "pos": "n", "extra": "", "translation": "alt-thing", "example": "Qqzzalt!", "note": ""}]\n```'
    dtab.query.set("qqzzalt"); dtab.search()
    assert _pump(app, lambda: _ai_rows(dtab))
    assert mock_ai.chats[-1]["auth"] == "Bearer nvapi-ui-secret" and mock_ai.chats[-1]["body"]["model"] == mock_ai.MODEL
    assert dtab.current().headword == "Qqzzalt" and dtab.current().source == "ai"
    assert app.t("dict.ai_alt") in dtab.ai_out.get("1.0", "end") and dtab.save_btn.winfo_manager()   # autosave off -> not stored yet
    before = app.repos.dictionary.count("ai"); dtab.save_ai_entry(); app.update()
    assert app.repos.dictionary.count("ai") == before + 1 and not dtab.save_btn.winfo_manager()
    assert any(r["headword"] == "Qqzzalt" and r["source"] == "ai" and r["example"] == "Qqzzalt!" for r in app.repos.dictionary.all())
    app.select("tab.settings"); tab = app.current_page(); tab.delete_key(); app.update()
    assert secrets.get_secret("alt_api_key") == "" and app.ai_alt.api_key == "" and tab.key_state.cget("text") == app.t("settings.alt_key_none")
    app.settings.update({"alt_enabled": False, "dict_ai": "auto", "dict_ai_autosave": True}); C.save_settings(app.settings)


def _word():
    return {"de": "Haus", "fr": "maison", "en": "house"}[C.TARGET_LANG]


def _cols(tab):
    value = tab.tree.cget("displaycolumns")
    return tuple(value) if isinstance(value, (tuple, list)) else tuple(str(value).split())


def test_dictionary_direction_selector_reruns_search_persists_and_fills_turkish(app, mock_ai):
    from eca import dictionary as D
    app.settings.update({"ai_enabled": True, "ai_base": mock_ai.base, "dict_ai": "off", "dict_ai_autosave": True, "alt_enabled": False, "dict_direction": "auto"})
    C.save_settings(app.settings); app.refresh_ai_clients()
    app.select("tab.dictionary"); tab = app.current_page(); app.update()
    word, target, other = _word(), C.TARGET_LANG, D.OTHER_LANG
    t2o, o2t = f"{target}2{other}", f"{other}2{target}"
    assert tab.direction.get() == app.t("dict.dir_auto") and set(tab.direction_box.cget("values")) == set(tab._direction_labels.values())
    assert _cols(tab)[:2] == ("head", "trans") and ("tr" in _cols(tab)) is D.HAS_TR
    tab.query.set(word); tab.search(); app.update()
    assert tab.dir_label.cget("text") == f"{target.upper()} → {other.upper()}" and tab.current().headword == word
    assert tab.w_trans.cget("text").startswith(app.t("dict.translation") + ":") and (tab.w_tr.winfo_manager() != "") is D.HAS_TR
    # switching the combobox re-runs the query in the fixed direction, updates the label and persists the setting
    tab.direction.set(tab._direction_labels[o2t]); tab._direction_changed(); app.update()
    assert app.settings["dict_direction"] == o2t and C.load_settings()["dict_direction"] == o2t
    assert tab.dir_label.cget("text") == D.direction_text(o2t) == f"{other.upper()} → {target.upper()}"
    assert tab.tree.get_children() == () and app.t("dict.no_result") in tab.ai_out.get("1.0", "end") and mock_ai.count() == 0   # only the source side is searched; AI off
    tab.direction.set(tab._direction_labels[t2o]); tab._direction_changed(); app.update()
    assert C.load_settings()["dict_direction"] == t2o and tab.dir_label.cget("text") == D.direction_text(t2o) and tab.current().headword == word
    app.settings["dict_direction"] = "auto"; C.save_settings(app.settings); app.select("tab.settings"); app.select("tab.dictionary"); app.update()
    assert tab.direction.get() == app.t("dict.dir_auto")                                   # picked up on show, like the AI policy
    if not D.HAS_TR:
        return
    # a *2tr search that finds an entry without a Turkish gloss asks the AI and writes the gloss into that entry (no duplicate).
    # The query is always set before the direction is switched: switching re-runs whatever query is in the box.
    t2tr, tr2t = f"{target}2tr", f"tr2{target}"
    app.repos.dictionary.add("Qqzzhaus", "qqzz-house", "n", "", "", "user", ""); tab.dict.extend([D.Entry("Qqzzhaus", "n", "", "qqzz-house", "", D.SOURCE_USER)])
    app.settings["dict_ai"] = "local"; C.save_settings(app.settings); tab.on_show()
    mock_ai.content = json.dumps([{"headword": "Qqzzhaus", "pos": "n", "extra": "", "translation_en": "qqzz-house", "translation_tr": "qqzz-ev; qqzz-hane", "example": "", "note": ""}])
    tab.query.set("Qqzzhaus"); tab.direction.set(tab._direction_labels[t2tr]); tab._direction_changed()
    first = tab.tree.get_children()[0]                                                       # synchronous part: listed with "—", AI pending
    assert _cols(tab)[:3] == ("head", "tr", "trans") and tab.tree.set(first, "tr") == "—" and app.status.get() == app.t("dict.tr_missing")
    assert tab.w_tr.cget("text") == f"{app.t('dict.turkish')}: —" and tab.dir_label.cget("text") == D.direction_text(t2tr)
    assert _pump(app, lambda: tab.current() is not None and tab.current().tr == "qqzz-ev; qqzz-hane"), "Turkish gloss was not filled"
    assert mock_ai.count("/chat/completions") == 1 and tab.current().source == "user" and not _ai_rows(tab) and not tab.save_btn.winfo_manager()
    rows = [r for r in app.repos.dictionary.all() if r["headword"] == "Qqzzhaus"]
    assert [(r["source"], r["tr"]) for r in rows] == [("user", "qqzz-ev; qqzz-hane")]           # updated in place, not duplicated
    assert tab.tree.set(tab.tree.get_children()[0], "tr") == "qqzz-ev; qqzz-hane" and "qqzz-ev" in tab.w_tr.cget("text")
    assert app.t("dict.tr_filled") in app.status.get() and app.t("dict.turkish") in tab.ai_out.get("1.0", "end") and "qqzz-hane" in tab.ai_out.get("1.0", "end")
    tab.query.set("qqzz-hane"); tab.direction.set(tab._direction_labels[tr2t]); tab._direction_changed(); app.update()
    assert tab.dir_label.cget("text") == D.direction_text(tr2t) and tab.current().headword == "Qqzzhaus" and mock_ai.count("/chat/completions") == 1
    tab.add_to_bank(); bank = app.repos.words.search("Qqzzhaus")[0]
    assert bank["tr"] == "qqzz-ev" and bank["en"] == "qqzz-house"                                # first Turkish sense feeds the word bank
    # a *2tr search on an entry that already has its gloss never asks the AI
    tab.query.set("Qqzzhaus"); tab.direction.set(tab._direction_labels[t2tr]); tab._direction_changed(); _pump(app, lambda: False, 0.5)
    assert mock_ai.count("/chat/completions") == 1 and tab.current().tr == "qqzz-ev; qqzz-hane"
    # autosave off: nothing is written until "Save", which then merges the gloss into the existing entry
    app.settings.update({"dict_ai_autosave": False, "dict_direction": "auto"}); C.save_settings(app.settings); tab.on_show()
    app.repos.dictionary.add("Qqzzbaum", "qqzz-tree", "n", "", "", "user", ""); tab.dict.extend([D.Entry("Qqzzbaum", "n", "", "qqzz-tree", "", D.SOURCE_USER)])
    mock_ai.content = json.dumps([{"headword": "Qqzzbaum", "pos": "n", "extra": "", "translation_en": "qqzz-tree", "translation_tr": "qqzz-ağaç", "example": "", "note": ""}])
    tab.query.set("Qqzzbaum"); tab.search(); app.update()
    assert tab.current().source == "user" and mock_ai.count("/chat/completions") == 1                 # auto never targets Turkish: no request
    tab.ask_ai()
    assert _pump(app, lambda: _ai_rows(tab)) and tab.current().source == "ai" and tab.save_btn.winfo_manager()
    assert [r["tr"] for r in app.repos.dictionary.all() if r["headword"] == "Qqzzbaum"] == [""] and tab.dict.twin(tab.current()).tr == ""
    before = app.repos.dictionary.count(); tab.save_ai_entry(); app.update()
    assert app.repos.dictionary.count() == before and [r["tr"] for r in app.repos.dictionary.all() if r["headword"] == "Qqzzbaum"] == ["qqzz-ağaç"]
    assert tab.current().source == "user" and tab.current().tr == "qqzz-ağaç" and not tab.save_btn.winfo_manager() and not _ai_rows(tab)
    # a built-in entry without a gloss (if any is left) is completed through an "ai" twin row that merges on the next start
    bare = next((e for e in tab.dict.entries if e.source == D.SOURCE_BUILTIN and not e.tr and len(tab.dict.find(e.headword)) == 1), None)
    if bare is not None:
        app.settings.update({"dict_ai_autosave": True, "dict_direction": t2tr}); C.save_settings(app.settings); tab.on_show()
        mock_ai.content = json.dumps([{"headword": bare.headword, "pos": bare.pos, "extra": bare.extra, "translation_en": bare.translation, "translation_tr": "qqzz-gloss"}])
        tab.query.set(bare.headword); tab.search()
        assert tab.current().headword == bare.headword and not tab.current().tr and app.status.get() == app.t("dict.tr_missing")
        assert _pump(app, lambda: tab.dict.twin(bare) is not None and tab.dict.twin(bare).tr == "qqzz-gloss")
        assert tab.dict.twin(bare).source == D.SOURCE_BUILTIN and tab.current().tr == "qqzz-gloss" and tab.current().source == D.SOURCE_BUILTIN
        assert any(r["headword"] == bare.headword and r["translation"] == bare.translation and r["source"] == "ai" and r["tr"] == "qqzz-gloss" for r in app.repos.dictionary.all())
        rebuilt = D.build_dictionary([(r["headword"], r["translation"], r["pos"], r["extra"], r["note"], r["source"], r["example"], r["tr"]) for r in app.repos.dictionary.all()])
        assert rebuilt.twin(bare).tr == "qqzz-gloss" and rebuilt.twin(bare).source == D.SOURCE_BUILTIN
    app.settings.update({"dict_ai": "auto", "dict_ai_autosave": True, "dict_direction": "auto"}); C.save_settings(app.settings)


def test_dictionary_random_word_is_found_in_every_direction_without_asking_the_ai(app, mock_ai):
    """"Random word" must search the side the selector expects: under tr2en the headword is not on the Turkish side, so the
    old behaviour reported "not found" and fired an AI request for a built-in word on every click."""
    from eca import dictionary as D
    app.settings.update({"ai_enabled": True, "ai_base": mock_ai.base, "dict_ai": "local", "dict_ai_autosave": True, "alt_enabled": False}); app.refresh_ai_clients()
    mock_ai.content = "[]"
    app.select("tab.dictionary"); tab = app.current_page(); app.update()
    expected_calls = 0
    for code in D.DIRECTIONS:
        app.settings["dict_direction"] = code; C.save_settings(app.settings); tab.on_show(); app.update()
        assert tab.direction.get() == tab._direction_labels[code]
        for _ in range(6):
            before = mock_ai.count("/chat/completions"); tab._write_ai("")
            picked = tab.random_word(); app.update()
            q = tab.query.get()
            assert picked is not None and picked.source == D.SOURCE_BUILTIN and q and tab.results, f"{code}: random word {q!r} was not found"
            assert picked in tab.results and tab.current() is not None, f"{code}: {q!r} did not list the picked entry {picked.headword!r}"
            assert tab.hist.get(0) == q and app.t("dict.no_result") not in tab.ai_out.get("1.0", "end")
            if code == "auto":
                assert q == picked.headword and tab.dir_label.cget("text") == D.direction_text(D.DEFAULT_DIRECTION)   # a headword hit wins ties
                continue
            field = D.source_field(code)
            assert tab.dir_label.cget("text") == D.direction_text(code)
            assert q == (picked.headword if field == "headword" else D.first_sense(getattr(picked, field)))
            if D.HAS_TR and D.target_field(code) == "tr" and not picked.tr:                # the gloss-filling request is the feature, not a lookup
                assert app.status.get() == app.t("dict.tr_missing"); expected_calls += 1
            else:
                assert app.status.get() == f"'{q}': {len(tab.results)} {app.t('dict.results')}" and mock_ai.count("/chat/completions") == before
    _pump(app, lambda: mock_ai.count("/chat/completions") >= expected_calls, 5); _pump(app, lambda: False, 0.3)
    assert mock_ai.count("/chat/completions") == expected_calls                          # built-in words never go to the AI as lookups
    app.settings.update({"dict_ai": "auto", "dict_direction": "auto"}); C.save_settings(app.settings); tab.on_show()


def test_dictionary_ai_answer_in_the_trilingual_shape_keeps_the_turkish_gloss(app, mock_ai):
    """A model answering with translation_en + translation_tr (the shape the DE/FR prompts request) must put the Turkish
    gloss into the Turkish column of the tree, the detail panel, SQLite and the word bank - in the English app the
    translation column IS Turkish, so the English gloss must never land there."""
    from eca import dictionary as D
    app.settings.update({"ai_enabled": True, "ai_base": mock_ai.base, "dict_ai": "local", "dict_ai_autosave": True, "alt_enabled": False, "dict_direction": "auto"})
    C.save_settings(app.settings); app.refresh_ai_clients()
    app.select("tab.dictionary"); tab = app.current_page(); tab.on_show(); app.update()
    turkish = "zzqq-iki hafta; zzqq-on beş gün"
    mock_ai.content = json.dumps([{"headword": "zzqqfortnight", "pos": "n", "extra": "", "translation_en": "a period of two weeks", "translation_tr": turkish,
                                   "example": "", "note": "two weeks"}], ensure_ascii=False)
    tab.query.set("zzqqfortnight"); tab.search()
    assert _pump(app, lambda: _ai_rows(tab)), "AI results did not arrive"
    e = tab.current(); item = tab.tree.get_children()[0]
    assert e is not None and e.headword == "zzqqfortnight" and e.source == D.SOURCE_AI
    if D.HAS_TR:
        assert (e.translation, e.tr) == ("a period of two weeks", turkish) and tab.tree.set(item, "tr") == turkish
        assert tab.w_tr.cget("text") == f"{app.t('dict.turkish')}: {turkish}"
    else:
        assert (e.translation, e.tr) == (turkish, "") and tab.tree.set(item, "trans") == turkish
        assert tab.w_trans.cget("text") == f"{app.t('dict.translation')}: {turkish}"
    assert "a period of two weeks" not in tab.tree.set(item, "trans" if not D.HAS_TR else "tr")
    rows = [r for r in app.repos.dictionary.all() if r["headword"] == "zzqqfortnight"]
    assert [(r["source"], r["translation"], r["tr"]) for r in rows] == [("ai", e.translation, e.tr)]      # cached exactly as shown
    tab.add_to_bank(); bank = app.repos.words.search("zzqqfortnight")[0]
    assert bank["tr"] == "zzqq-iki hafta"                                                   # the word bank gets the first Turkish sense
    tab.query.set("zzqq-on beş gün"); tab.direction.set(tab._direction_labels[f"tr2{C.TARGET_LANG}"]); tab._direction_changed(); app.update()
    assert tab.current() is not None and tab.current().headword == "zzqqfortnight" and mock_ai.count("/chat/completions") == 1   # found on the Turkish side, offline
    app.settings.update({"dict_ai": "auto", "dict_direction": "auto"}); C.save_settings(app.settings); tab.on_show()
