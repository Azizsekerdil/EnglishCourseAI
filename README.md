# English Course AI

[![sürüm](https://img.shields.io/github/v/release/Azizsekerdil/EnglishCourseAI?display_name=tag&sort=semver&label=s%C3%BCr%C3%BCm&color=2ea44f)](https://github.com/Azizsekerdil/EnglishCourseAI/releases/latest)
[![lisans MIT](https://img.shields.io/github/license/Azizsekerdil/EnglishCourseAI?label=lisans&color=blue)](LICENSE)
[![platform Windows ve macOS](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-0078D4)](https://github.com/Azizsekerdil/EnglishCourseAI/releases/latest)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB)](https://www.python.org/downloads/)

**Türkçe** | [English](README.en.md)

English Course AI, İngilizce öğrenimi için yerel veriyi önceleyen bağımsız bir masaüstü uygulamasıdır; Windows ve macOS için dağıtılır. Türkçe ve English arayüzleri aynı özellik derinliğini sunar; kelime, yazım, telaffuz ve dilbilgisi içeriği İngilizce için hazırlanmıştır.

**Kullanım kılavuzu:** [docs/KULLANIM_KILAVUZU.md](docs/KULLANIM_KILAVUZU.md) - kurulum, 18 ekran, sözlük ve yön seçimi, yapay zekâ kurulumu, veri yönetimi ve sorun giderme.

> Temel çalışma özellikleri ve öğrenci verileri yereldir. Kaynak bağlantılarını açmak ve isteğe bağlı uzak servisleri kullanmak internet gerektirir; uygulama bu nedenle yanıltıcı bir “%100 çevrimdışı” iddiasında bulunmaz.

## Öne çıkan özellikler

- SM-2 ve Leitner tabanlı aralıklı tekrar; günlük hedef ve seri
- 160'ın üzerinde yerleşik A1 kelime; çoğul, sözcük türü ve örnek cümleler
- İngilizce-Türkçe sözlük, favoriler ve yanlış kelimeler
- Çift yönlü **İngilizce ↔ Türkçe öğrenci sözlüğü** sekmesi: 1.210+ gömülü madde, her maddede sade İngilizce tanım ve düzensiz fiil/çoğul biçimleri; yön seçici (`Otomatik`, `EN → TR`, `TR → EN`; sabit yönde yalnızca kaynak dil aranır, seçim kaydedilir), seslendirme, kelime bankasına ekleme, CSV/TSV içe/dışa aktarma (başlık satırı tanınır, sütun sırası serbest)
- **AI destekli sözlük**: sözlükte bulunmayan kelimeler LM Studio'ya ya da alternatif bir OpenAI uyumlu uç noktaya (NVIDIA NIM veya herhangi bir URL + API anahtarı) yapılandırılmış JSON olarak sorulur; sonuçlar (Türkçe çeviri, sade İngilizce tanım, örnek cümle) yerel sözlüğe önbelleklenir ve sonraki aramalar çevrimdışı çalışır
- Kart, çoktan seçmeli, yazma, dinleme ve eşleştirme çalışma seçenekleri
- CEFR A1-C1 profili ve puanlanan sınav motoru
- Kısa/uzun ünlüler, iki `th` sesi, `sh/ch`, sessiz harfler, `-ed` ve `-s` okunuşları, apostrof, UK/US yazımı, vurgu ve dikte laboratuvarı
- Artikeller, sayılabilirlik, zamirler, temel zamanlar, gelecek, modallar, soru/olumsuzluk, karşılaştırma, koşullar, mastar/-ing ve phrasal verb konuları
- Telaffuz, konuşma, serbest yazma ve el yazısı alanı
- Yerel PDF metin okuma ve sayfa notları
- Lisans/erişim ve atıf bilgili ücretsiz Kaynak Merkezi
- LM Studio ile yerel AI öğretmen; açıklama, çeviri, düzeltme, konuşma ve görsel/OCR görevleri
- Göreve göre model profilleri ve metin içermeyen token defteri
- Haftalık ilerleme raporu, açık/koyu tema ve öğrenci profilleri
- Unicode CSV ve `.ecapack` paket içe/dışa aktarımı

## İndirme

Hazır paketi indirip doğrudan çalıştırabilirsiniz; Python kurmanız gerekmez. Tüm sürümler için [Sürümler sayfasına](https://github.com/Azizsekerdil/EnglishCourseAI/releases/latest) bakın.

| Dosya | Bağlantı |
| --- | --- |
| Windows paketi | [EnglishCourseAI-Windows.zip](https://github.com/Azizsekerdil/EnglishCourseAI/releases/latest/download/EnglishCourseAI-Windows.zip) |
| macOS paketi (Apple Silicon) | [EnglishCourseAI-macOS.zip](https://github.com/Azizsekerdil/EnglishCourseAI/releases/latest/download/EnglishCourseAI-macOS.zip) |
| Kullanım kılavuzu (PDF) | [EnglishCourseAI-Kullanim-Kilavuzu.pdf](https://github.com/Azizsekerdil/EnglishCourseAI/releases/latest/download/EnglishCourseAI-Kullanim-Kilavuzu.pdf) |

Bağlantılar her zaman en güncel sürümü verir. Windows'ta ZIP'i açın ve `EnglishCourseAI.exe` dosyasını çalıştırın.

macOS paketi Apple Silicon için derlenmiştir ve **imzalanmamış, notarize edilmemiştir**. Bu nedenle ilk açılışta çift tıklama engellenir: `EnglishCourseAI.app` dosyasına **sağ tık → Aç** deyin ve çıkan uyarıda yeniden **Aç**'ı seçin. Sonraki açılışlarda bu adım gerekmez.

Kaynaktan çalıştırmak isterseniz aşağıya bakın.

## Kurulum ve kaynaktan çalıştırma

Gereksinim: Python 3.11 veya üzeri.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python .\English_Course_AI.pyw
```

Öğrenci verileri Windows'ta `%APPDATA%\EnglishCourseAI`, macOS'ta `~/.englishcourseai` altında tutulur. Test veya taşınabilir deneme için `ECA_HOME` ortam değişkeniyle ayrı bir klasör seçilebilir.

## Paket üretimi (Windows ve macOS)

### Windows EXE

Paket **temiz bir sanal ortamdan** derlenir; böylece yalnızca `requirements.txt`
içindeki kütüphaneler pakete girer. Genel `site-packages` kullanılırsa
uygulamanın hiç çağırmadığı kütüphaneler de EXE'ye girer ve dosya gereksiz yere
büyür.

```powershell
python -m venv $env:TEMP\EnglishCourseAI-venv
& "$env:TEMP\EnglishCourseAI-venv\Scripts\python.exe" -m pip install -r requirements.txt pyinstaller
$env:PYTHON = "$env:TEMP\EnglishCourseAI-venv\Scripts\python.exe"
.\build.bat
```

`PYTHON` tanımlı değilse `build.bat` sistemdeki `python` komutunu kullanır.
Çıktılar: `dist\EnglishCourseAI.exe` ve dağıtım arşivi
`dist\EnglishCourseAI-Windows.zip` (EXE + `LICENSE` + `THIRD_PARTY_NOTICES.md`).
`build`, `dist` ve kullanıcı verileri Git deposuna alınmaz. Testleri çalıştırmak
için `python -m pip install -r requirements-dev.txt`.

### macOS uygulaması

macOS paketi bir Mac üzerinde derlenir:

```bash
chmod +x build_macos.sh
./build_macos.sh
```

Çıktılar: `dist/EnglishCourseAI.app` ve dağıtım arşivi
`dist/EnglishCourseAI-macOS.zip` (uygulama paketi, içinde `LICENSE` ve
`THIRD_PARTY_NOTICES.md`). Depodaki **macOS Paketi** iş akışı
(`.github/workflows/build-macos.yml`) aynı betiği GitHub'ın macOS koşucusunda
çalıştırır; yalnızca elle tetiklenir. Paket imzalanmaz ve notarize edilmez.

## Yerel AI kurulumu

1. LM Studio'yu kurun ve bir sohbet modeli indirin.
2. OpenAI uyumlu Local Server'ı başlatın.
3. Varsayılan adres `http://127.0.0.1:1234` değeridir.
4. Uygulama içindeki Ayarlar sayfasından görev modelini veya adresi değiştirin.

LM Studio kapalıysa uygulama çalışmaya devam eder; yalnız AI özellikleri devre dışı kalır. Prompt ve AI yanıt metinleri veritabanına yazılmaz. Token defteri yalnız model, görev, token sayıları, süre ve başarı durumunu saklar.

### Sözlük için AI sağlayıcısı

Sözlük sekmesi iki sağlayıcı kullanabilir:

- **LM Studio** (yerel, anahtar gerekmez) — `app.ai`, yukarıdaki adres.
- **Alternatif uç nokta** — herhangi bir OpenAI uyumlu API: varsayılan `https://integrate.api.nvidia.com/v1` (NVIDIA NIM, model `meta/llama-3.1-8b-instruct`); OpenRouter, Groq veya Ollama gibi başka bir temel URL, model adı ve API anahtarı da girilebilir. Ayarlar sayfasında etkinleştirilir, "Bağlantıyı test et" ile denenir.

Ayarlardaki (ve sözlük araç çubuğundaki) **Sözlük AI kaynağı** politikası: `Otomatik` (LM Studio erişilebilirse o, değilse etkinse alternatif), `LM Studio`, `Alternatif` veya `Kapalı`. Sözlükte sonuç çıkmazsa AI arka planda sorulur; bulunan maddeler `AI` kaynağıyla listelenir ve (varsayılan olarak) `dict_entries` tablosuna kaydedilir. "AI'a sor" düğmesi yerel sonuç olsa bile AI maddelerini listenin üstüne ekler.

API anahtarı Windows Kimlik Bilgisi Yöneticisi'nde (`EnglishCourseAI/alt_api_key`) saklanır; Windows dışında veya API başarısız olursa `settings/secrets.json` dosyasına düşer. Anahtar hiçbir zaman `settings.json` içine yazılmaz. `ENGLISHCOURSEAI_API_KEY` ortam değişkeni kayıtlı anahtarı geçersiz kılar.

## Gizlilik ve internet

- Profil, ilerleme, sınav, PDF notları ve sayaçlar ayrı SQLite veritabanında yerel saklanır.
- SRS, sınav, sözlük, dilbilgisi ve paket özellikleri internet olmadan çalışır.
- Kaynak Merkezi bağlantıları yalnız kullanıcı eylemiyle açılır ve internet kullanır.
- Uzak AI servisleri isteğe bağlıdır ve varsayılan olarak kapalıdır; API anahtarı Kimlik Bilgisi Yöneticisi'nde tutulur, ayar dosyasına yazılmaz.

## Testler

```powershell
python -m pytest -q
```

Testler pencere/18 sayfa kurulumu, anlık ve kalıcı dil değişimi, i18n bütünlüğü, SQLite geçişi, 150+ kelime, 1.210+ maddelik sözlük motoru (sabit ve otomatik yönler, içe/dışa aktarma, SQLite kullanıcı maddeleri), yerel sahte OpenAI sunucusuyla AI sözlük araması (JSON ayrıştırma, Bearer başlığı, sağlayıcı seçimi, sözlük sekmesi akışı), gizli anahtar deposu (dosya arka ucu), `dict_entries` şema geçişi, SRS, kart/sınav akışı, büyük-küçük harf duyarsız arama, apostrof ve kısa çizgi duyarlı doğru yazım, Unicode CSV, AI çevrimdışı davranışı, token gizliliği ve paket turunu kapsar. Testler gerçek ağa ya da Kimlik Bilgisi Yöneticisi'ne asla dokunmaz.

## Ücretsiz kaynak kataloğu

Katalog British Council LearnEnglish, BBC Learning English, Cambridge English ve VOA Learning English gibi ücretsiz erişimli resmî öğrenme sayfalarına; ayrıca Wikibooks, Tatoeba, LibriVox ve Project Gutenberg gibi açık/kamu malı koleksiyonlara bağlantı verir. Üçüncü taraf içerik uygulamaya kopyalanmaz. Her bağlantıda erişim/lisans ve atıf notu gösterilir; kamu malı durumu ülkeye göre değişebileceğinden yerel durum kontrol edilmelidir.

## Lisans

English Course AI, MIT Lisansı ile dağıtılır. Tam metin için [LICENSE](LICENSE) dosyasına bakın.

Uygulamanın kullandığı ve paketlenmiş sürümlerin içinde yer alan üçüncü taraf bileşenler, gerçek lisanslarıyla birlikte [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) dosyasında listelenir.
