from pathlib import Path

from eca import config as C
from eca.i18n import LANG_NAMES, LOCALES, SYSTEM_PROMPTS


def test_identity_and_isolated_paths():
    assert (C.APP_NAME, C.APP_SLUG, C.TARGET_LANG, C.TARGET_LANG_NAME) == ("English Course AI", "EnglishCourseAI", "en", "English")
    assert C.DB_PATH.name == "EnglishCourseAI.db"
    assert C.APP_SLUG.lower() not in {"germancourseai", "frenchcourseai"}


def test_settings_roundtrip_is_filtered_and_atomic():
    data = C.load_settings(); data["ui_lang"] = "en"; data["daily_goal"] = 37; data["api_key"] = "must-not-persist"
    C.save_settings(data); back = C.load_settings()
    assert back["ui_lang"] == "en" and back["daily_goal"] == 37
    assert "api_key" not in C.SETTINGS_PATH.read_text(encoding="utf-8")
    assert not C.SETTINGS_PATH.with_suffix(".tmp").exists()


def test_all_i18n_keys_exist_in_two_languages():
    assert tuple(LANG_NAMES) == C.UI_LANGS
    keys = set(LOCALES["tr"])
    assert len(keys) >= 140
    assert all(set(LOCALES[lang]) == keys for lang in C.UI_LANGS)
    assert all(value.strip() for lang in C.UI_LANGS for value in LOCALES[lang].values())


def test_system_prompts_follow_interface_language():
    assert set(SYSTEM_PROMPTS) == set(C.UI_LANGS)
    assert "Türkçe" in SYSTEM_PROMPTS["tr"] and "İngilizce" in SYSTEM_PROMPTS["tr"]
    assert "countability" in SYSTEM_PROMPTS["en"] and "past participle" in SYSTEM_PROMPTS["en"]


def test_english_search_and_spelling_forms_are_separate():
    assert C.normalize_search("Twenty-One") == "twenty-one"
    assert C.answer_equal("English", "english")
    assert C.answer_equal("don't", "DON'T")
    assert not C.answer_equal("dont", "don't")
    assert not C.answer_equal("well known", "well-known")
