from eca import content
from eca.seed_words import WORDS


def test_has_at_least_150_original_a1_words():
    assert len(WORDS) >= 150
    assert len({w["en"] for w in WORDS}) >= 150
    required = {"tr", "en", "article", "gender", "plural", "part_of_speech", "example_tr", "example_en", "frequency_rank", "deck", "audio"}
    assert all(required <= set(word) for word in WORDS)


def test_nouns_have_article_plural_and_natural_example():
    nouns = [w for w in WORDS if w["part_of_speech"] == "noun"]
    assert len(nouns) >= 90
    assert all(w["article"] == "the" and w["gender"] == "not grammatical" and w["plural"] for w in nouns)
    assert all(w["en"] in w["example_en"] for w in nouns)


def test_orthography_covers_required_english_features():
    text = " ".join(" ".join(row) for row in content.ORTHOGRAPHY)
    for token in ("Short vowels", "Silent-e", "th", "sh / ch", "Silent letters", "-ed", "Plural", "Apostrophes", "Hyphens", "UK / US", "Word stress"):
        assert token in text


def test_grammar_topics_cover_requirements():
    codes = {t["code"] for t in content.GRAMMAR_TOPICS}
    required = {"sentence.word_order", "noun.number", "article.indef", "article.def", "article.zero",
                "pron.subject", "pron.object", "possessive", "demonstratives", "verb.be", "verb.have",
                "tense.present_simple", "tense.present_continuous", "tense.past_simple", "tense.past_continuous",
                "tense.present_perfect", "future.will", "future.going_to", "modals.can", "modals.must_should",
                "questions", "negation", "adjectives", "adverbs", "prepositions", "countability", "comparison",
                "conditionals", "infinitive_gerund", "phrasal_verbs"}
    assert required <= codes


def test_all_labs_generate_valid_exercises():
    for lab in ("grammar", "articles", "verbs", "tenses", "pronouns", "orthography"):
        items = content.build(lab, 8)
        assert len(items) == 8
        assert all(item["answer"] in item["options"] and item["prompt"] for item in items)
    assert content.build("unknown", 3) == []


def test_resource_catalog_is_free_or_open_and_attributed():
    assert len(content.RESOURCES) >= 8
    assert all(r["license"] and r["attribution"] and r["url"].startswith("https://") for r in content.RESOURCES)
    assert all(any(term in r["license"] for term in ("Free", "CC", "Public", "public")) for r in content.RESOURCES)
