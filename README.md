# English Course AI

English Course AI, İngilizce öğrenimi için yerel veriyi önceleyen bağımsız bir Windows masaüstü uygulamasıdır. Türkçe ve English arayüzleri aynı özellik derinliğini sunar; kelime, yazım, telaffuz ve dilbilgisi içeriği İngilizce için hazırlanmıştır.

> Temel çalışma özellikleri ve öğrenci verileri yereldir. Kaynak bağlantılarını açmak ve isteğe bağlı uzak servisleri kullanmak internet gerektirir; uygulama bu nedenle yanıltıcı bir “%100 çevrimdışı” iddiasında bulunmaz.

## Öne çıkan özellikler

- SM-2 ve Leitner tabanlı aralıklı tekrar; günlük hedef ve seri
- 160'ın üzerinde yerleşik A1 kelime; çoğul, sözcük türü ve örnek cümleler
- İngilizce-Türkçe sözlük, favoriler ve yanlış kelimeler
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

## Kurulum ve kaynaktan çalıştırma

Gereksinim: Python 3.11 veya üzeri.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python .\English_Course_AI.pyw
```

Öğrenci verileri `%APPDATA%\EnglishCourseAI` altında tutulur. Test veya taşınabilir deneme için `ECA_HOME` ortam değişkeniyle ayrı bir klasör seçilebilir.

## Windows EXE üretimi

```powershell
python -m pip install -r requirements-dev.txt
.\build.bat
```

Çıktı: `dist\EnglishCourseAI.exe`. `build`, `dist` ve kullanıcı verileri Git deposuna alınmaz.

## Yerel AI kurulumu

1. LM Studio'yu kurun ve bir sohbet modeli indirin.
2. OpenAI uyumlu Local Server'ı başlatın.
3. Varsayılan adres `http://127.0.0.1:1234` değeridir.
4. Uygulama içindeki Ayarlar sayfasından görev modelini veya adresi değiştirin.

LM Studio kapalıysa uygulama çalışmaya devam eder; yalnız AI özellikleri devre dışı kalır. Prompt ve AI yanıt metinleri veritabanına yazılmaz. Token defteri yalnız model, görev, token sayıları, süre ve başarı durumunu saklar. NVIDIA NIM varsayılan olarak kapalıdır; anahtarlar ayar dosyasına yazılmaz.

## Gizlilik ve internet

- Profil, ilerleme, sınav, PDF notları ve sayaçlar ayrı SQLite veritabanında yerel saklanır.
- SRS, sınav, sözlük, dilbilgisi ve paket özellikleri internet olmadan çalışır.
- Kaynak Merkezi bağlantıları yalnız kullanıcı eylemiyle açılır ve internet kullanır.
- Uzak AI servisleri isteğe bağlıdır ve varsayılan olarak kapalıdır.

## Testler

```powershell
python -m pytest -q
```

Testler pencere/17 sayfa kurulumu, anlık ve kalıcı dil değişimi, i18n bütünlüğü, SQLite geçişi, 150+ kelime, SRS, kart/sınav akışı, büyük-küçük harf duyarsız arama, apostrof ve kısa çizgi duyarlı doğru yazım, Unicode CSV, AI çevrimdışı davranışı, token gizliliği ve paket turunu kapsar.

## Ücretsiz kaynak kataloğu

Katalog British Council LearnEnglish, BBC Learning English, Cambridge English ve VOA Learning English gibi ücretsiz erişimli resmî öğrenme sayfalarına; ayrıca Wikibooks, Tatoeba, LibriVox ve Project Gutenberg gibi açık/kamu malı koleksiyonlara bağlantı verir. Üçüncü taraf içerik uygulamaya kopyalanmaz. Her bağlantıda erişim/lisans ve atıf notu gösterilir; kamu malı durumu ülkeye göre değişebileceğinden yerel durum kontrol edilmelidir.
