"""English-specific spelling, pronunciation, grammar and free resources."""
from __future__ import annotations

import random


ORTHOGRAPHY = [
    ("A–Z", "English alphabet", "English uses 26 letters; letter names and sounds are not always the same.", "A /eɪ/ · B /biː/ · C /siː/"),
    ("a e i o u", "Short vowels", "A single vowel in a closed syllable is often short.", "cat · bed · sit · hot · cup"),
    ("a_e i_e", "Silent-e pattern", "A final silent e often changes the earlier vowel to its letter name.", "cap / cape · kit / kite"),
    ("th", "Two th sounds", "th may be voiceless /θ/ or voiced /ð/.", "think · three · this · mother"),
    ("sh / ch", "Consonant pairs", "sh usually represents /ʃ/; ch commonly represents /tʃ/.", "ship · fish · chair · teacher"),
    ("c / g", "Soft and hard c/g", "Before e, i or y, c and g are often soft; exceptions exist.", "city · cycle · giant · game"),
    ("ee / ea", "Long-e spellings", "ee and ea often represent /iː/, but spelling must be learned word by word.", "see · green · eat · speak"),
    ("oo", "Two common oo sounds", "oo may be /uː/ or /ʊ/.", "food · school · book · good"),
    ("kn wr mb", "Silent letters", "Some historical consonants remain in spelling but are not pronounced.", "know · write · lamb · climb"),
    ("-ed", "Past-tense ending", "-ed is pronounced /t/, /d/ or /ɪd/ depending on the final sound.", "worked · played · wanted"),
    ("-s", "Plural and third-person -s", "The ending is pronounced /s/, /z/ or /ɪz/.", "cats · dogs · buses"),
    ("'", "Apostrophes", "Apostrophes mark omitted letters or possession; they are part of correct spelling.", "don't · I'm · Sarah's book"),
    ("-", "Hyphens", "Hyphens connect some compound words and multiword modifiers.", "well-known · twenty-one"),
    ("UK / US", "Common spelling variants", "Both standards are valid when used consistently.", "colour / color · centre / center"),
    ("stress", "Word stress", "A stressed syllable is clearer and usually longer; stress can distinguish words.", "PREsent / preSENT · PHOtograph"),
]

PRONUNCIATION = [
    ("th", "/θ/ /ð/", "think, this"), ("r", "/ɹ/", "red, around"),
    ("short i / long ee", "/ɪ/ /iː/", "ship, sheep"), ("short a / short e", "/æ/ /e/", "bad, bed"),
    ("w / v", "/w/ /v/", "west, vest"), ("schwa", "/ə/", "about, teacher"),
    ("-ed", "/t/ /d/ /ɪd/", "worked, played, wanted"), ("-s", "/s/ /z/ /ɪz/", "cats, dogs, buses"),
    ("linking", "connected speech", "turn_off, pick_it_up"), ("stress", "content-word stress", "I NEED a NEW TICKET"),
]

_TOPIC_ROWS = [
    ("sentence.word_order", "Temel söz dizimi", "Basic word order", "Olumlu cümlede temel sıra özne + fiil + nesnedir.", "A basic affirmative clause follows subject + verb + object.", "She reads books."),
    ("noun.number", "Tekil ve çoğul", "Singular and plural", "Çoğul çoğunlukla -s/-es alır; düzensiz biçimler ayrıca öğrenilir.", "Most plurals take -s/-es; irregular forms must be learned.", "one child · two children"),
    ("article.indef", "a / an", "Indefinite articles", "Tekil sayılabilen, belirsiz isimlerde a/an kullanılır; seçim sese bağlıdır.", "Use a/an with a singular, non-specific count noun; the choice depends on sound.", "a book · an apple · a university"),
    ("article.def", "the", "Definite article", "Konuşan ve dinleyenin bildiği ya da belirli isimlerde the kullanılır.", "Use the for a specific or mutually identifiable noun.", "Close the door."),
    ("article.zero", "Sıfır artikel", "Zero article", "Genel çoğullar ve sayılamayan isimler çoğu kez artikelsiz kullanılır.", "General plurals and uncount nouns often take no article.", "Books are useful. · Water is essential."),
    ("pron.subject", "Özne zamirleri", "Subject pronouns", "I, you, he, she, it, we, they özne konumunda kullanılır.", "I, you, he, she, it, we and they function as subjects.", "They live here."),
    ("pron.object", "Nesne zamirleri", "Object pronouns", "me, you, him, her, it, us, them fiil veya edattan sonra gelir.", "Object pronouns follow a verb or preposition.", "Please call me."),
    ("possessive", "İyelik", "Possessives", "my/your gibi sıfatlar isimden önce; mine/yours gibi zamirler tek başına kullanılır.", "Possessive determiners precede nouns; possessive pronouns stand alone.", "This is my bag. · It is mine."),
    ("demonstratives", "İşaret sözcükleri", "Demonstratives", "this/these yakın, that/those daha uzak varlıkları gösterir.", "This/these point to nearer items; that/those to more distant items.", "This book · those shoes"),
    ("verb.be", "be fiili", "The verb be", "be; kişi ve zamana göre am/is/are, was/were biçimlerini alır.", "Be changes to am/is/are and was/were according to subject and tense.", "I am ready. · They were late."),
    ("verb.have", "have fiili", "The verb have", "have/has sahiplikte ve bazı yapılarda yardımcı fiil olarak kullanılır.", "Have/has expresses possession and also works as an auxiliary.", "She has a car."),
    ("tense.present_simple", "Present simple", "Present simple", "Alışkanlık, rutin ve genel gerçeklerde kullanılır; he/she/it -s alır.", "Use it for habits, routines and facts; he/she/it takes -s.", "He works on Mondays."),
    ("tense.present_continuous", "Present continuous", "Present continuous", "Şu anda süren veya geçici durum: am/is/are + -ing.", "Use am/is/are + -ing for actions in progress or temporary situations.", "We are studying now."),
    ("tense.past_simple", "Past simple", "Past simple", "Bitmiş geçmiş olaylarda düzenli -ed veya düzensiz ikinci biçim kullanılır.", "Use the -ed form or an irregular past form for completed past events.", "I visited Ankara. · She went home."),
    ("tense.past_continuous", "Past continuous", "Past continuous", "Geçmişte belli anda sürmekte olan eylem: was/were + -ing.", "Use was/were + -ing for an action in progress at a past time.", "They were sleeping at ten."),
    ("tense.present_perfect", "Present perfect", "Present perfect", "Geçmişle şimdiyi bağlar: have/has + past participle.", "Use have/has + past participle when a past event matters now.", "I have finished."),
    ("future.will", "will ile gelecek", "Future with will", "Anlık karar, tahmin ve sözlerde will + yalın fiil kullanılır.", "Use will + base verb for spontaneous decisions, predictions and promises.", "I will help you."),
    ("future.going_to", "be going to", "Be going to", "Plan ve mevcut kanıta dayalı tahminlerde be going to kullanılır.", "Use be going to for plans and evidence-based predictions.", "We are going to travel."),
    ("modals.can", "can / could", "Can and could", "Yetenek, olasılık ve rica; modalden sonra yalın fiil gelir.", "Use can/could for ability, possibility and requests; follow with the base verb.", "Can you swim?"),
    ("modals.must_should", "must / have to / should", "Obligation and advice", "must/have to zorunluluk, should tavsiye bildirir.", "Must/have to express obligation; should gives advice.", "You should rest."),
    ("questions", "Soru yapıları", "Questions", "Çoğu soruda yardımcı fiil özneden önce gelir.", "In most questions, an auxiliary comes before the subject.", "Do you work here?"),
    ("negation", "Olumsuzluk", "Negation", "be ile not; diğer basit zamanlarda do/does/did not kullanılır.", "Use not after be; use do/does/did not with other simple-tense verbs.", "She isn't busy. · I don't know."),
    ("adjectives", "Sıfatlar", "Adjectives", "Sıfatlar isimden önce veya bağlayıcı fiilden sonra gelir; çoğul eki almaz.", "Adjectives precede nouns or follow linking verbs and do not take plural endings.", "a small house · The house is small."),
    ("adverbs", "Zarflar", "Adverbs", "Zarflar eylemin nasıl, ne zaman veya ne sıklıkta olduğunu belirtir.", "Adverbs describe manner, time or frequency; position depends on type.", "She speaks slowly. · I often walk."),
    ("prepositions", "Edatlar", "Prepositions", "at/in/on zaman ve yerde farklı kalıplar kurar; kullanımı örneklerle öğrenilir.", "At, in and on form different time and place patterns.", "at five · on Monday · in July"),
    ("countability", "Sayılabilen ve sayılamayan", "Countability", "many/few sayılabilen; much/little sayılamayan isimlerle kullanılır.", "Use many/few with count nouns and much/little with uncount nouns.", "many books · much time"),
    ("comparison", "Karşılaştırma", "Comparison", "Kısa sıfatlarda -er/-est; uzunlarda more/most kullanılır.", "Short adjectives usually take -er/-est; longer ones use more/most.", "smaller · the most useful"),
    ("conditionals", "Zero ve first conditional", "Zero and first conditionals", "Genel gerçeklerde zero; gerçek gelecek olasılığında first conditional kullanılır.", "Use the zero conditional for facts and the first for realistic future possibilities.", "If it rains, we will stay home."),
    ("infinitive_gerund", "Mastar ve -ing", "Infinitives and gerunds", "Bazı fiiller to + fiil, bazıları -ing biçimini izler.", "Some verbs take to + base verb; others take an -ing form.", "want to learn · enjoy reading"),
    ("phrasal_verbs", "Phrasal verbs", "Phrasal verbs", "Fiil + parçacık yeni bir anlam oluşturabilir; bütün olarak öğrenilir.", "A verb plus particle can create a new meaning and should be learned as a unit.", "turn on · look for · get up"),
]

GRAMMAR_TOPICS = [
    {"code": code, "title": {"tr": tr, "en": en}, "rule": {"tr": rtr, "en": ren}, "example": example}
    for code, tr, en, rtr, ren, example in _TOPIC_ROWS
]

EXERCISES = [
    {"topic": "article.indef", "prompt": "I need ___ umbrella.", "answer": "an", "options": ["a", "an", "the", "–"], "explain": "Umbrella begins with a vowel sound."},
    {"topic": "article.def", "prompt": "Please close ___ window next to you.", "answer": "the", "options": ["a", "an", "the", "some"], "explain": "The speaker identifies a specific window."},
    {"topic": "article.zero", "prompt": "___ water is essential for life.", "answer": "–", "options": ["A", "An", "The", "–"], "explain": "Water is used generally as an uncount noun."},
    {"topic": "noun.number", "prompt": "one child → two ___", "answer": "children", "options": ["childs", "childes", "children", "child"], "explain": "Child has the irregular plural children."},
    {"topic": "pron.subject", "prompt": "Mina and I are ready. → ___ are ready.", "answer": "We", "options": ["We", "Us", "They", "Them"], "explain": "We is a subject pronoun."},
    {"topic": "pron.object", "prompt": "Please call Deniz. → Please call ___.", "answer": "him", "options": ["he", "his", "him", "they"], "explain": "Him is the object form."},
    {"topic": "verb.be", "prompt": "They ___ at home yesterday.", "answer": "were", "options": ["was", "were", "are", "be"], "explain": "Past be with they is were."},
    {"topic": "verb.have", "prompt": "She ___ a new bicycle.", "answer": "has", "options": ["have", "has", "having", "had got to"], "explain": "Present simple with she uses has."},
    {"topic": "tense.present_simple", "prompt": "He ___ English every day. (study)", "answer": "studies", "options": ["study", "studies", "studying", "studied"], "explain": "He/she/it takes -s; consonant + y changes to -ies."},
    {"topic": "tense.present_continuous", "prompt": "We ___ dinner now. (cook)", "answer": "are cooking", "options": ["cook", "cooked", "are cooking", "have cooked"], "explain": "Now signals am/is/are + -ing."},
    {"topic": "tense.past_simple", "prompt": "I ___ her yesterday. (see)", "answer": "saw", "options": ["see", "saw", "seen", "am seeing"], "explain": "The irregular past of see is saw."},
    {"topic": "tense.past_continuous", "prompt": "At nine, they ___ . (sleep)", "answer": "were sleeping", "options": ["slept", "sleep", "were sleeping", "have slept"], "explain": "An action in progress at a past time uses was/were + -ing."},
    {"topic": "tense.present_perfect", "prompt": "She ___ the work. (finish)", "answer": "has finished", "options": ["finished", "has finished", "finishes", "is finishing"], "explain": "Present perfect: has + past participle."},
    {"topic": "future.will", "prompt": "Don't worry. I ___ you.", "answer": "will help", "options": ["helped", "will help", "am help", "helping"], "explain": "A spontaneous promise commonly uses will."},
    {"topic": "future.going_to", "prompt": "We bought tickets. We ___ tomorrow.", "answer": "are going to travel", "options": ["travelled", "are going to travel", "will travelling", "travel"], "explain": "A prior plan uses be going to."},
    {"topic": "modals.can", "prompt": "___ you swim?", "answer": "Can", "options": ["Can", "Do can", "Are", "Have"], "explain": "Can comes before the subject in a question."},
    {"topic": "modals.must_should", "prompt": "You look tired. You ___ rest.", "answer": "should", "options": ["should", "mustn't", "can't", "did"], "explain": "Should expresses advice."},
    {"topic": "questions", "prompt": "___ she work here?", "answer": "Does", "options": ["Do", "Does", "Is", "Has"], "explain": "Present-simple questions with she use does."},
    {"topic": "negation", "prompt": "He ___ coffee. (not like)", "answer": "doesn't like", "options": ["not likes", "doesn't like", "isn't like", "don't likes"], "explain": "Use does not + base verb."},
    {"topic": "prepositions", "prompt": "The class starts ___ Monday.", "answer": "on", "options": ["at", "on", "in", "to"], "explain": "Use on with days."},
    {"topic": "countability", "prompt": "How ___ time do we have?", "answer": "much", "options": ["many", "much", "few", "several"], "explain": "Time is uncountable in this meaning."},
    {"topic": "comparison", "prompt": "This bag is ___ than that one. (small)", "answer": "smaller", "options": ["small", "smaller", "more small", "smallest"], "explain": "A short adjective takes -er."},
    {"topic": "conditionals", "prompt": "If it rains, we ___ home.", "answer": "will stay", "options": ["stay will", "will stay", "stayed", "staying"], "explain": "First conditional: if + present, will + base verb."},
    {"topic": "infinitive_gerund", "prompt": "I enjoy ___ books. (read)", "answer": "reading", "options": ["read", "to reading", "reading", "reads"], "explain": "Enjoy is followed by an -ing form."},
    {"topic": "phrasal_verbs", "prompt": "Please ___ the light. (activate)", "answer": "turn on", "options": ["turn on", "turn at", "look for", "get up"], "explain": "Turn on means activate."},
    {"topic": "orthography", "prompt": "Choose the correct spelling.", "answer": "don't", "options": ["dont", "don't", "do'nt", "don-t"], "explain": "The apostrophe replaces the omitted o in not."},
    {"topic": "orthography", "prompt": "Choose the silent-letter word.", "answer": "know", "options": ["now", "know", "cow", "how"], "explain": "The k in know is not pronounced."},
    {"topic": "orthography", "prompt": "Choose the correct past form.", "answer": "studied", "options": ["studyed", "studyd", "studied", "studyed"], "explain": "Consonant + y changes to i before -ed."},
]


def build(lab="grammar", n=10, rng=None):
    if lab not in {"grammar", "articles", "verbs", "tenses", "pronouns", "orthography"}:
        return []
    rng = rng or random.Random()
    source = list(EXERCISES)
    if lab == "articles":
        source = [e for e in source if e["topic"].startswith("article.")]
    elif lab == "verbs":
        source = [e for e in source if e["topic"].startswith(("verb.", "modals.", "phrasal_"))]
    elif lab == "tenses":
        source = [e for e in source if e["topic"].startswith(("tense.", "future."))]
    elif lab == "pronouns":
        source = [e for e in source if e["topic"].startswith("pron.")]
    elif lab == "orthography":
        source = [e for e in source if e["topic"] == "orthography"]
    return [dict(rng.choice(source)) for _ in range(n)] if source else []


RESOURCES = [
    {"id": "british-council", "title": "British Council LearnEnglish", "kind": "course", "level": "A1-C1", "url": "https://learnenglish.britishcouncil.org/", "license": "Free access; external copyright applies", "attribution": "British Council", "online": True},
    {"id": "bbc-learning-english", "title": "BBC Learning English", "kind": "video/audio", "level": "A1-C1", "url": "https://www.bbc.co.uk/learningenglish", "license": "Free access; BBC copyright applies", "attribution": "BBC Learning English", "online": True},
    {"id": "cambridge-english", "title": "Cambridge English free activities", "kind": "practice", "level": "A1-C2", "url": "https://www.cambridgeenglish.org/learning-english/activities-for-learners/", "license": "Free access; Cambridge copyright applies", "attribution": "Cambridge English", "online": True},
    {"id": "voa-learning-english", "title": "VOA Learning English", "kind": "news/course", "level": "A1-C1", "url": "https://learningenglish.voanews.com/", "license": "Free access; check item-specific reuse terms", "attribution": "Voice of America", "online": True},
    {"id": "wikibooks-eal", "title": "English as an Additional Language - Wikibooks", "kind": "book", "level": "A1-C1", "url": "https://en.wikibooks.org/wiki/English_as_an_Additional_Language", "license": "CC BY-SA 4.0", "attribution": "Wikibooks contributors", "online": True},
    {"id": "tatoeba-en", "title": "Tatoeba English sentences", "kind": "data", "level": "A1-C1", "url": "https://tatoeba.org/en/downloads", "license": "CC BY 2.0 FR / selected CC0", "attribution": "Tatoeba contributors; preserve sentence-level attribution", "online": True},
    {"id": "librivox-en", "title": "LibriVox English audiobooks", "kind": "audio", "level": "B1-C1", "url": "https://librivox.org/search?primary_key=0&search_category=language&search_page=1&search_form=get_results", "license": "Public domain in the USA; check local status", "attribution": "LibriVox volunteers", "online": True},
    {"id": "gutenberg-en", "title": "Project Gutenberg English books", "kind": "book", "level": "B1-C1", "url": "https://www.gutenberg.org/browse/languages/en", "license": "Project Gutenberg public-domain terms; check each item and local status", "attribution": "Project Gutenberg and named authors/editors", "online": True},
]
