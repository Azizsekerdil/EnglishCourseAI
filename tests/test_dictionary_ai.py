"""AI-driven dictionary lookup and provider resolution against a local mock OpenAI server (no real network)."""
from __future__ import annotations

import json
import time

import pytest

from eca import config as C
from eca import dictionary as D
from eca.ai_client import AIClient, AIError, resolve_provider


def test_ai_lookup_parses_fenced_json_and_sends_bearer(mock_ai):
    client = AIClient(mock_ai.base, api_key="sk-test-123")
    entries = D.ai_lookup(client, mock_ai.sample[0]["headword"], "en")
    assert len(entries) == len(mock_ai.sample) and all(e.source == D.SOURCE_AI for e in entries)
    first, sample = entries[0], mock_ai.sample[0]
    assert (first.headword, first.pos, first.extra, first.translation) == (sample["headword"], "n", sample["extra"], sample["translation"])
    assert first.example == sample["example"] and first.note == sample["note"]
    assert all(e.pos in D.POS_LABELS for e in entries)
    second = entries[1]
    assert second.pos == "n"                                             # "noun" normalised to the dictionary's code
    assert (second.headword, second.extra, second.translation, second.note) == ("snack", "", "atıştırmalık", "a small amount of food eaten between meals")
    chat = mock_ai.chats[-1]
    assert chat["auth"] == "Bearer sk-test-123"
    assert chat["body"]["model"] == mock_ai.MODEL and client.last_model == mock_ai.MODEL
    user = chat["body"]["messages"][-1]["content"]
    assert sample["headword"] in user and "JSON" in user and C.TARGET_LANG_NAME in user
    assert all(r["auth"] == "Bearer sk-test-123" for r in mock_ai.requests)       # /models probe carries it too


def test_no_key_means_no_authorization_header(mock_ai):
    client = AIClient(mock_ai.base)
    assert D.ai_lookup(client, "x", "tr")
    assert all(r["auth"] == "" for r in mock_ai.requests)
    assert D.ai_lookup(client, "   ", "tr") == [] and mock_ai.count("/chat/completions") == 1   # blank query never hits the network


def test_garbage_output_yields_empty_list_without_raising(mock_ai):
    mock_ai.content = "Sorry, I cannot help with that."
    assert D.ai_lookup(AIClient(mock_ai.base), "x", "en") == []
    for garbage in ("", "null", "[]", "[1, 2]", '[{"headword": 5}]', "```\n[{broken\n```", '[{"headword": "a", "translation": null}]',
                    '{"headword": "a"}', "[[[", "]]]", '[{"headword": {"x": 1}, "translation": "y"}]', "[" * 5000):
        assert D.parse_ai_entries(garbage) == [], garbage


def test_parser_is_tolerant_and_bounded():
    rows = D.parse_ai_entries('Here you go:\n```json\n[{"headword": "x", "translation": ["y", "z"], "pos": "Verb"}]\n```\nHope it helps!')
    assert rows[0].translation == "y; z" and rows[0].pos == "v" and rows[0].source == D.SOURCE_AI
    assert D.parse_ai_entries('[{"headword": "x", "translation": "y"}]')[0].pos == "phr"          # missing pos
    long = "a" * 500
    e = D.parse_ai_entries(json.dumps([{"headword": long, "translation": long, "example": long, "note": long, "extra": long}]))[0]
    assert len(e.headword) <= 80 and len(e.translation) <= 200 and len(e.example) <= 240 and len(e.note) <= 240 and len(e.extra) <= 80
    many = D.parse_ai_entries(json.dumps([{"headword": f"w{i}", "translation": "t"} for i in range(12)]))
    assert len(many) == D.AI_MAX_ENTRIES
    mixed = D.parse_ai_entries(json.dumps([7, {"headword": "ok", "translation": "fine"}, {"headword": "", "translation": "x"}, "str"]))
    assert [e.headword for e in mixed] == ["ok"]
    e = D.parse_ai_entries('[{"headword": "house", "pos": "Noun", "extra": "/haʊs/", "translation": ["ev", "konut"], "note": "a building where people live"}]')[0]
    assert (e.pos, e.headword, e.extra, e.translation, e.note, e.display) == ("n", "house", "/haʊs/", "ev; konut", "a building where people live", "house")
    e = D.parse_ai_entries('[{"headword": "go", "pos": "verb", "extra": "", "translation": "gitmek", "note": "to move to another place — went, gone"}]')[0]
    assert (e.pos, e.note) == ("v", "to move to another place — went, gone")


def test_normalize_pos_covers_codes_names_and_localised_labels():
    assert D.normalize_pos("noun") == "n" and D.normalize_pos("Substantiv") == "n" and D.normalize_pos("isim") == "n"
    assert D.normalize_pos("verb.") == "v" and D.normalize_pos("ADJ") == "adj" and D.normalize_pos("n.") == "n"
    assert D.normalize_pos("noun (m)") == "n" and D.normalize_pos("Wendung") == "phr" and D.normalize_pos("interjection") == "int"
    assert D.normalize_pos("whatever") == "phr" and D.normalize_pos(None) == "phr" and D.normalize_pos(3) == "phr"


def test_ai_prompt_explains_convention_and_direction():
    prompt = D.ai_prompt("house", "tr")
    assert "house" in prompt and "headword" in prompt and "translation" in prompt and "example" in prompt
    assert all(code in prompt for code in D.POS_LABELS) and str(D.AI_MAX_ENTRIES) in prompt
    assert "Detect the direction" in prompt and C.TARGET_LANG_NAME in prompt
    assert "Turkish" in prompt and "plain-English" in prompt and "went, gone" in prompt
    # the per-key line and the convention must not contradict each other: "note" is a plain-English definition, not a Turkish note
    note_line = next(line for line in prompt.splitlines() if line.strip().startswith('"note"'))
    assert "plain-English definition" in note_line and "Turkish" not in note_line and "usage note" not in prompt


def test_ipa_in_extra_is_not_a_plural():
    ipa = D.Entry("elevenses", "n", "/ɪˈlɛvənzɪz/", "kuşluk atıştırması", "a light mid-morning snack", D.SOURCE_AI)
    assert ipa.plural == "" and ipa.gender == "" and ipa.display == "elevenses"
    assert D.Entry("child", "n", "[tʃaɪld]", "çocuk").plural == ""
    assert D.Entry("child", "n", "children", "çocuk", "", D.SOURCE_USER).plural == "children"       # a real plural in a user entry survives
    d = D.Dictionary([ipa])
    assert d.lookup("elevenses")[1] == [ipa] and d.lookup("/ɪˈlɛvənzɪz/")[1] == []                   # the IPA is not a search form


def test_closed_port_raises_aierror_quickly():
    client = AIClient("http://127.0.0.1:9")
    started = time.monotonic()
    with pytest.raises(AIError):
        D.ai_lookup(client, "house", "en")
    assert time.monotonic() - started < 5
    assert client.available(timeout=0.2) is False and client.reachable(timeout=0.2) is False


def test_client_url_headers_and_key_requirements():
    remote = AIClient(C.NIM_BASE + "/", api_key="k", model="meta/llama-3.1-8b-instruct")
    assert remote._url("models") == "https://integrate.api.nvidia.com/v1/models"
    assert remote._headers()["Authorization"] == "Bearer k" and remote.needs_key and not remote.is_local and remote.usable()
    assert remote.choose_model("dictionary") == "meta/llama-3.1-8b-instruct"        # remote: trusts the configured model, no probe
    assert not AIClient(C.NIM_BASE).usable()                                          # remote without key
    local = AIClient("http://localhost:11434")
    assert local._url("chat/completions") == "http://localhost:11434/v1/chat/completions"
    assert local.usable() and local.is_local and "Authorization" not in local._headers()
    local.configure(api_key="abc", model="m")
    assert local.api_key == "abc" and local.model == "m" and local.base == "http://localhost:11434"
    lan = AIClient("http://192.0.2.10:11434")                                        # Ollama / LM Studio on another machine: no key needed
    assert not lan.is_local and not lan.needs_key and lan.usable() and "Authorization" not in lan._headers()
    hosted = AIClient("HTTPS://api.example.org/v1")                                    # hosted https API: key required
    assert hosted.needs_key and not hosted.usable() and AIClient("https://api.example.org/v1", api_key="k").usable()


def test_provider_resolution_follows_policy(mock_ai):
    local_ok, local_down = AIClient(mock_ai.base), AIClient("http://127.0.0.1:9")
    alt, alt_nokey = AIClient(C.NIM_BASE, api_key="k"), AIClient(C.NIM_BASE)      # remote: never contacted by the resolver
    base = {"ai_enabled": True, "alt_enabled": True}
    assert resolve_provider({**base, "dict_ai": "off"}, local_ok, alt) is None
    assert resolve_provider({**base, "dict_ai": "local"}, local_ok, alt) is local_ok
    assert resolve_provider({**base, "dict_ai": "local"}, local_down, alt) is None
    assert resolve_provider({**base, "dict_ai": "alt"}, local_ok, alt) is alt
    assert resolve_provider({**base, "dict_ai": "alt"}, local_ok, alt_nokey) is None
    assert resolve_provider({**base, "alt_enabled": False, "dict_ai": "alt"}, local_ok, alt) is None
    assert resolve_provider({**base, "dict_ai": "auto"}, local_ok, alt) is local_ok
    assert resolve_provider({**base, "dict_ai": "auto"}, local_down, alt) is alt
    assert resolve_provider({**base, "dict_ai": "auto"}, local_down, alt_nokey) is None
    assert resolve_provider({**base, "alt_enabled": False, "dict_ai": "auto"}, local_down, alt) is None
    assert resolve_provider({**base, "ai_enabled": False, "dict_ai": "auto"}, local_ok, alt) is alt
    assert resolve_provider({**base, "ai_enabled": False, "dict_ai": "local"}, local_ok, alt) is None
    assert resolve_provider({**base, "dict_ai": "bogus"}, local_ok, alt) is local_ok                # unknown -> auto
    assert resolve_provider({}, local_ok, alt) is local_ok                                          # defaults: auto, local enabled
    alt_lan = AIClient("http://192.0.2.10:11434")                                                   # key-less server on the LAN (never contacted here)
    assert resolve_provider({**base, "dict_ai": "alt"}, local_down, alt_lan) is alt_lan
    assert resolve_provider({**base, "dict_ai": "auto"}, local_down, alt_lan) is alt_lan
    assert resolve_provider({**base, "alt_enabled": False, "dict_ai": "auto"}, local_down, alt_lan) is None
    assert mock_ai.count("/models") == 1                                                            # reachability is cached


def test_reachability_cache_expires_and_can_be_invalidated(mock_ai):
    client = AIClient(mock_ai.base)
    assert client.reachable() and client.reachable() and mock_ai.count("/models") == 1
    assert client.reachable(ttl=0) and mock_ai.count("/models") == 2
    client.invalidate(); assert client.reachable() and mock_ai.count("/models") == 3
    client.configure(base=mock_ai.base); assert client.reachable() and mock_ai.count("/models") == 4


def test_token_logger_and_alt_model_are_used(mock_ai):
    log = []
    AIClient(mock_ai.base, lambda *a: log.append(a)).chat("hi", "chat", "en")
    alt = AIClient(mock_ai.base, lambda *a: log.append(a), api_key="k", model=mock_ai.MODEL)
    assert D.ai_lookup(alt, "x", "de") and mock_ai.chats[-1]["body"]["model"] == mock_ai.MODEL
    assert mock_ai.chats[-1]["body"]["temperature"] <= 0.2 and mock_ai.chats[-1]["body"]["messages"][0]["role"] == "system"
    assert [(row[0], row[1], row[2], row[3], row[5]) for row in log] == [(mock_ai.MODEL, "chat", 42, 17, True), (mock_ai.MODEL, "dictionary", 42, 17, True)]


def test_entry_defaults_and_table_roundtrip_keep_example(tmp_path):
    e = D.Entry("house", "n", "", "ev")
    assert e.example == "" and e.source == D.SOURCE_BUILTIN
    ai = D.Entry("Zzqqxx", "n", "", "zzq-thing", "n", D.SOURCE_AI, "The zzqqxx is old.")
    out = tmp_path / "ai.csv"
    assert D.write_table(out, [ai]) == 1
    back = D.read_table(out)[0]
    assert back.example == "The zzqqxx is old." and back.source == D.SOURCE_USER
    d = D.build_dictionary([("Zzqqxx", "zzq-thing", "n", "", "", "ai", "The zzqqxx is old."), ("Qqzz", "qqz-fence", "n", "", "", "bogus", "")])
    by = d.count_by_source()
    assert by.get(D.SOURCE_AI, 0) == 1 and d.lookup("Qqzz")[1][0].source == D.SOURCE_USER
    assert d.lookup("Zzqqxx")[1][0].example == "The zzqqxx is old."
    assert d.contains(ai) and not d.contains(D.Entry("nope", "n", "", "nothing"))
    assert d.contains(D.Entry("house", "n", "", "ev", "", D.SOURCE_AI))      # duplicates of built-in entries are recognised


# ---------------------------------------------------------------------------
# Thinking models (gemma-4 / qwen3): reasoning_effort field, truncated-answer retry, model ranking
# ---------------------------------------------------------------------------
def test_local_client_sends_reasoning_off_and_records_finish_reason(mock_ai):
    mock_ai.reasoning_tokens = 3
    client = AIClient(mock_ai.base)
    assert client.is_local
    entries = D.ai_lookup(client, mock_ai.sample[0]["headword"], "en")
    assert entries and entries[0].source == D.SOURCE_AI
    body = mock_ai.chats[-1]["body"]
    assert body.get("reasoning_effort") == "none" and body["max_tokens"] == D.AI_MAX_TOKENS
    assert client.last_finish_reason == "stop" and client.last_reasoning_tokens == 3


def test_remote_client_does_not_send_reasoning_field(mock_ai):
    class RemoteClient(AIClient):                     # hosted endpoint stand-in
        is_local = property(lambda self: False)

    client = RemoteClient(mock_ai.base, api_key="k")
    assert D.ai_lookup(client, mock_ai.sample[0]["headword"], "en")
    assert "reasoning_effort" not in mock_ai.chats[-1]["body"]
    assert AIClient(mock_ai.base).is_local                       # class property untouched


def test_server_rejecting_extra_fields_gets_a_retry_without_them(mock_ai):
    mock_ai.reject_fields = {"reasoning_effort"}
    client = AIClient(mock_ai.base)
    assert D.ai_lookup(client, mock_ai.sample[0]["headword"], "en")
    chats = mock_ai.chats
    assert len(chats) == 2
    assert "reasoning_effort" in chats[0]["body"] and "reasoning_effort" not in chats[1]["body"]


def test_truncated_empty_answer_is_retried_with_a_bigger_budget(mock_ai):
    mock_ai.queue = [("", "length"), (mock_ai.content, "stop")]
    client = AIClient(mock_ai.base)
    assert D.ai_lookup(client, mock_ai.sample[0]["headword"], "en")
    chats = mock_ai.chats
    assert len(chats) == 2 and chats[1]["body"]["max_tokens"] == D.AI_MAX_TOKENS * 3
    mock_ai.queue = [("Sorry, I cannot help with that.", "stop")]          # not truncated: no retry
    assert D.ai_lookup(client, "zzqqxx", "en") == [] and len(mock_ai.chats) == 3


def test_rank_models_skips_specialist_models_and_prefers_fitting_general_models():
    from eca import ai_client as A
    installed = ["qwen/qwen3.6-35b-a3b", "google/gemma-4-12b-qat", "qwen/qwen3-vl-8b", "biomistral-7b",
                 "qwen2.5-math-7b-instruct", "moondream-2b-2025-04-14", "text-embedding-nomic-embed-text-v1.5"]
    ranked = A.rank_models(installed, "dictionary")
    assert ranked[0] == "google/gemma-4-12b-qat"
    assert "qwen2.5-math-7b-instruct" not in ranked and "text-embedding-nomic-embed-text-v1.5" not in ranked
    assert A.rank_models(["text-embedding-x"], "chat") == ["text-embedding-x"]
    assert A.rank_models(["gemma-4-12b-qat", "qwen2.5-7b-instruct"], "chat")[0] == "qwen2.5-7b-instruct"
    assert A.model_size_b("qwen/qwen3.6-35b-a3b") == 35.0 and A.is_specialist("qwen/qwen3-vl-8b")


def test_choose_model_avoids_specialist_models(monkeypatch, mock_ai):
    client = AIClient(mock_ai.base)
    monkeypatch.setattr(client, "models", lambda timeout=1.5: ["qwen2.5-math-7b-instruct", "google/gemma-4-12b-qat"])
    assert client.choose_model("dictionary") == "google/gemma-4-12b-qat"
