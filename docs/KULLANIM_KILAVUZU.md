# English Course AI - Kullanım Kılavuzu

Sürüm 1.2.1 · Windows ve macOS masaüstü uygulaması · Arayüz dilleri: Türkçe ve English

- [1. Bu kılavuz hakkında](#1-bu-kılavuz-hakkında)
- [2. Kurulum](#2-kurulum)
- [3. Uygulamayı ilk çalıştırma](#3-uygulamayı-ilk-çalıştırma)
- [4. Ekranlar](#4-ekranlar)
- [5. Sözlük (ayrıntılı)](#5-sözlük-ayrıntılı)
- [6. Yapay zeka](#6-yapay-zeka)
- [7. Veri yönetimi](#7-veri-yönetimi)
- [8. Kısayollar ve ipuçları](#8-kısayollar-ve-ipuçları)
- [9. Sorun giderme](#9-sorun-giderme)
- [10. Sürüm notları özeti](#10-sürüm-notları-özeti)
- [11. Sık sorulan sorular](#11-sık-sorulan-sorular)
- [12. Lisans](#12-lisans)

---

## 1. Bu kılavuz hakkında

Bu kılavuz **English Course AI** sürüm **1.2.1** içindir. Uygulama, ana dili Türkçe olan öğrenciler için hazırlanmış, verilerini sizin bilgisayarınızda tutan bağımsız bir İngilizce çalışma ortamıdır. Tekrar, sözlük, laboratuvarlar, sınav, PDF notları ve ilerleme internet olmadan çalışır; yapay zeka özellikleri isteğe bağlıdır.

Baştan sona okumanız gerekmez: yeni başlıyorsanız [2](#2-kurulum), [3](#3-uygulamayı-ilk-çalıştırma) ve [4](#4-ekranlar) bölümleri yeterlidir; sözlüğü yoğun kullanacaksanız [5. bölüm](#5-sözlük-ayrıntılı), yapay zeka bağlayacaksanız [6. bölüm](#6-yapay-zeka), bir şey beklediğiniz gibi çalışmıyorsa [9. bölüm](#9-sorun-giderme) size göredir. Düğme ve alan adları arayüzün Türkçe dilindeki biçimiyle yazılmış, İngilizce karşılıkları yararlı olduğunda parantez içinde verilmiştir.

## 2. Kurulum

### Windows (zip)

1. `EnglishCourseAI-Windows.zip` dosyasını indirin.
2. Zip'i bir klasöre çıkarın (arşivin içinden çalıştırmayın).
3. `EnglishCourseAI.exe` dosyasına çift tıklayın.

Kurulum sihirbazı, yönetici hakkı veya kayıt defteri değişikliği yoktur; uygulama tek dosyadır ve ilk açılışı birkaç saniye sürebilir.

### macOS (zip, Apple Silicon)

1. `EnglishCourseAI-macOS.zip` dosyasını indirip açın, `EnglishCourseAI.app` uygulamasını `Applications` klasörüne taşıyın.
2. Uygulama **notarize edilmemiştir**: ilk açılışta simgeye **sağ tıklayın** (veya Control ile tıklayın) ve **Aç**'ı seçin; çıkan uyarıda yine **Aç**'a basın.
3. Bu izni bir kez verirsiniz; sonraki açılışlarda çift tıklama yeterlidir.

Paket Apple Silicon içindir ve kimliği `com.englishcourseai.desktop`.

### Kaynaktan çalıştırma

Gereksinim: Python 3.11 veya üzeri. Kaynaktan çalıştırmanın tek dış bağımlılığı, PDF Okuyucu için kullanılan `pypdf`'tir (BSD-3-Clause). Paketlenmiş `.exe` ve `.app` sürümleri ayrıca Python yorumlayıcısını, Tcl/Tk'yi ve PyInstaller'ın açılış bileşenini içerir; hepsinin dökümü [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) dosyasındadır.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python .\English_Course_AI.pyw
```

macOS ve Linux'ta ortamı `source .venv/bin/activate` ile açar, `python English_Course_AI.pyw` komutunu kullanırsınız.

### Verileriniz nerede tutuluyor?

Öğrenci verileri programın yanında değil, ayrı bir kullanıcı klasöründe saklanır: Windows'ta `%APPDATA%\EnglishCourseAI`, diğer sistemlerde `~/.englishcourseai`.

| Alt klasör | İçerik |
| --- | --- |
| `data` | `EnglishCourseAI.db` (bütün SQLite verisi) |
| `settings` | `settings.json` ve gerekirse `secrets.json` |
| `exports` | Sözlük CSV dışa aktarımları için önerilen klasör |
| `downloads` | Uygulamanın ayırdığı çalışma klasörü |

Taşınabilir kullanım için `ECA_HOME` ortam değişkenini ayarlayın; uygulama her şeyi o klasörde tutar:

```powershell
$env:ECA_HOME = "E:\EnglishCourseAI-veri"
.\EnglishCourseAI.exe
```

## 3. Uygulamayı ilk çalıştırma

Pencere 1360 × 860 boyutunda açılır (en küçük 1080 × 700) ve başlıkta `English Course AI 1.2.1` yazar. Solda gruplanmış sayfa listesi, üstte araç şeridi, altta durum çubuğu vardır. Üst şeritte sayfa başlığı, `🌐` ile **arayüz dili** kutusu (`Türkçe` / `English`), yeni profil açan **+** düğmesi, **profil** kutusu ve sağ uçta `AI: Kullanılabilir` / `AI: Kullanılamıyor` rozeti bulunur.

İlk açılışta uygulama sizden hiçbir şey istemez; veri klasörünü ve `EnglishCourseAI.db` veritabanını oluşturur, `Alex` adlı varsayılan profili açar, Kelime Bankası'na 162 kelimelik A1 düzeyi başlangıç setini yükler (kelimeler Temel, Fiiller, Yiyecek gibi 20 konu destesine dağıtılmıştır) ve 1210 maddelik gömülü sözlüğü hazırlar (indirme gerekmez).

**Arayüz dilini** üst şeritten değiştirirsiniz; sayfalar anında yeniden çizilir ve seçim kaydedilir (varsayılan: Türkçe). **Temayı** değiştirmek için **Ayarlar → Tema** kutusundan `dark` ya da `light` seçip **Kaydet**'e basın (varsayılan: `dark`). **Günlük hedef** (varsayılan 20) ve **Seslendirme** (varsayılan açık) yine Ayarlar sayfasındadır.

**İpucu:** Tanışmak için **Aralıklı Tekrar** sayfasında `new` kuyruğuyla 10 kartlık kısa bir tur yapın, sonra **Sözlük EN-TR** sayfasında birkaç kelime arayın.

## 4. Ekranlar

Sol menüde 18 sayfa beş grup altında sıralanır; aşağıdaki sıra menüdeki sıranın aynısıdır.

| Grup | Sayfalar |
| --- | --- |
| ÖĞREN | Aralıklı Tekrar · Kelime Bankası · Sözlük EN-TR · Sınav |
| LABORATUVARLAR | Yazım ve Ses · Telaffuz · Dilbilgisi |
| OKU & KEŞFET | Kaynak Merkezi · PDF Okuyucu · Ders Kitaplığı |
| PRATİK | AI Öğretmen · Konuşma · Yazma & El Yazısı |
| İLERLEME & SİSTEM | İlerleme · Paketler · Token Defteri · Çevrimdışı Kılavuz · Ayarlar |

### ÖĞREN

#### Aralıklı Tekrar (Spaced Review)

**Ne işe yarar.** SM-2 algoritması ve Leitner kutularıyla günlük tekrar planınızı yürütür.

**Nasıl kullanılır.** Üstteki dört kutu **Bugün**, **Yeni**, **Yanlışlar** ve **Favoriler** sayılarını gösterir. Kuyruk kutusundan `new`, `due`, `wrong` veya `favorites` seçin; yanındaki kutudan **Kart**, **Çoktan seçmeli**, **Yazma**, **Dinleme** ya da **Eşleştirme** modunu seçin; sayaçtan kart sayısını belirleyip (5-50, varsayılan 10) **Başlat**'a basın. Kartta kelime, çoğul ve tür görünür; **Cevabı göster**'e bastıktan sonra kendinizi **Tekrar**, **Zor**, **İyi** veya **Kolay** ile değerlendirirsiniz. Kart yüzü her modda aynıdır; **Dinleme** seçiliyse kelime ayrıca seslendirilir. Kuyruk bitince **Oturum tamamlandı** yazar.

**İpucu:** **Tekrar** dediğiniz kelime ertesi güne, **Kolay** dediğiniz giderek uzayan aralıklara atılır; dürüst değerlendirme planı doğru tutar.

#### Kelime Bankası (Word Bank)

**Ne işe yarar.** Bütün çalışma kelimelerinizin listesidir; tekrar ve sınav buradan beslenir.

**Nasıl kullanılır.** Kutuya yazıp **Ara**'ya (veya Enter'a) basın; arama İngilizce kelimede, Türkçe karşılıkta ve ipucu alanında yapılır. Tabloda **İngilizce**, **Türkçe**, **İngilizce ipucu**, **Artikel**, **Çoğul** ve **Deste** sütunları vardır; satır seçtiğinizde altta örnek cümleler görünür. **★ Favori** seçili kelimeyi favorilere ekler ya da çıkarır. **↑ Dışa aktar** UTF-8 CSV yazar, **↓ İçe aktar** aynı biçimdeki dosyayı geri okur.

**İpucu:** Sözlükten **★ Kelime bankasına ekle** ile gönderdiğiniz kelime `Sözlük EN-TR` destesine düşer ve tekrar kuyruğunuza katılır.

#### Sözlük EN-TR (Dictionary EN-TR)

**Ne işe yarar.** Çift yönlü İngilizce ↔ Türkçe öğrenci sözlüğüdür: 1210 gömülü madde çevrimdışı çalışır, bulunmayan kelimeler istenirse yapay zekaya sorulur ve yanıt yerel sözlüğe kaydedilir.

**Nasıl kullanılır.** Ayrıntılı anlatım için [5. bölüme](#5-sözlük-ayrıntılı) bakın.

**İpucu:** Yeni bir kelime öğrenmek için **🎲 Rastgele kelime** düğmesine basın; gömülü destesinden seçilen madde doğrudan karşınıza gelir.

#### Sınav (Exam)

**Ne işe yarar.** Kelime bankanızdan çoktan seçmeli sınav üretir ve puanlar.

**Nasıl kullanılır.** **Soru sayısı** sayacını ayarlayın (5-50, varsayılan 10) ve **Başlat**'a basın. Her soruda İngilizce kelime gösterilir; dört Türkçe seçenekten birini işaretleyip **Kontrol et**'e basarsınız. Son sorudan sonra **Sınav bitti** ve **Puan: 80.0%** biçiminde bir satır görünür; sonuç ilerleme kaydına yazılır. Sınav kaydına yazılan CEFR düzeyi ayar dosyasındaki `cefr` alanından okunur (varsayılan `A1`); bu sürümde arayüzde düzey seçimi yoktur.

**İpucu:** `wrong` kuyruğu, Aralıklı Tekrar'da **Tekrar** ya da **Zor** dediğiniz kelimelerden oluşur; sınav sonuçları ayrı saklanır ve bu kuyruğu değiştirmez.

### LABORATUVARLAR

#### Yazım ve Ses (Spelling & Sound)

**Ne işe yarar.** İngilizce yazım-ses ilişkisini 15 kuralla gösterir ve kısa bir dikte alıştırması sunar.

**Nasıl kullanılır.** Soldaki tablodan bir satır seçin (başlıksız simge sütunu ile **Yazım ve ses kuralları** ve **Örnekler** sütunları); sağ panelde kuralın açıklaması belirir. **Dikte alıştırması** bölümünde **▶ Seslendir**'e basıp sözcüğü dinleyin, kutuya yazın ve **Kontrol et**'e basın: doğruysa `✓`, yanlışsa doğru yazım gösterilir. Dikte sözcüğü bu sürümde sabittir, arayüzden değiştirilemez ve şu an Almanca `Straße` sözcüğüdür - kardeş Almanca uygulamadan kalan, İngilizce sürümde düzeltilecek bir kalıntıdır.

**İpucu:** Yazım denetimi büyük-küçük harfi yok sayar ama kesme işaretini ve kısa çizgiyi önemser: `dont` ile `don't` aynı cevap sayılmaz.

#### Telaffuz (Pronunciation)

**Ne işe yarar.** Bir sözcüğü bilgisayar sesiyle dinletir ve İngilizcenin zorlu seslerini karşılaştırmalı listeler.

**Nasıl kullanılır.** Üstteki kutuya sözcüğü yazın ve **▶ Seslendir**'e basın; kutu bu sürümde Almanca `Mädchen` sözcüğüyle açılır (aynı kalıntı), üzerine kendi sözcüğünüzü yazabilirsiniz. Altta **Telaffuz ipucu** başlığıyla 10 satırlık ses tablosu vardır: ses adı, IPA yazımı ve örnek sözcükler (`th` `/θ/ /ð/` → *think, this*). **◉ Mikrofonla karşılaştır** bu sürümde etkin değildir; basıldığında **Kullanılamıyor** yazar, uygulama ses kaydı almaz.

**İpucu:** Aynı sözcüğü sözlükte arayıp sade İngilizce tanımını okuyun; yapay zekayla bulunan maddelerde **Ek bilgi** sütununda IPA yazımı da bulunur.

#### Dilbilgisi (Grammar)

**Ne işe yarar.** 30 dilbilgisi konusunu kural, örnek ve alıştırmayla çalıştırır.

**Nasıl kullanılır.** Soldaki listeden konuyu seçin (Temel söz dizimi, a / an, Present perfect, Phrasal verbs…); sağda başlık, kural ve örnek cümle görünür. **Alıştırma** bölümünde seçeneklerden birini işaretleyip **Kontrol et**'e basın: doğruysa `✓`, yanlışsa doğru cevap ve açıklaması gösterilir. **Sonraki** yeni bir alıştırma çeker. Alıştırmalar 28 sorudan rastgele seçilir, seçtiğiniz konuya göre süzülmez; doğru ve yanlışlarınız konu bazında kaydedilir.

**İpucu:** Kuralı okuduktan sonra üst üste birkaç kez **Sonraki**'ye basıp farklı soru tiplerini görmek tek soruda takılmaktan öğreticidir.

### OKU & KEŞFET

#### Kaynak Merkezi (Resource Center)

**Ne işe yarar.** Ücretsiz erişimli, kamu malı ve Creative Commons İngilizce kaynaklara bağlantı verir; üçüncü taraf içeriği kopyalamaz.

**Nasıl kullanılır.** Sekiz kartın her birinde kaynağın adı, düzeyi, **Lisans** ve **Atıf** bilgisi yazar (British Council LearnEnglish, BBC Learning English, VOA Learning English, Tatoeba, LibriVox, Project Gutenberg gibi). **Aç ↗** düğmesi bağlantıyı varsayılan tarayıcınızda açar; sayfa başındaki `ⓘ Bağlantıları açmak internet kullanır.` uyarısı bunu hatırlatır.

**İpucu:** Kamu malı durumu ülkeye göre değişebilir; indirdiğiniz metinleri paylaşmadan önce kendi ülkenizdeki durumu kontrol edin.

#### PDF Okuyucu (PDF Reader)

**Ne işe yarar.** Kendi PDF ders dosyanızın metnini sayfa sayfa okur ve her sayfaya not tutmanızı sağlar.

**Nasıl kullanılır.** **PDF seç**'e basıp dosyayı seçin; yolu yanında görünür ve bir sonraki açılışta hatırlanır. **Sayfa** sayacıyla dolaşın, sol panelde o sayfanın metni (salt okunur) görünür. Sağdaki **Sayfa notu** kutusuna yazıp **Kaydet**'e basın; not profil + dosya + sayfa üçlüsüne bağlı saklanır. Metin, PDF'in metin katmanından çıkarılır; taranmış PDF'lerde panel boş kalır.

**İpucu:** Taranmış bir sayfayı okumak için ekran görüntüsünü alıp **AI Öğretmen** sayfasındaki **Görsel / OCR** görevine verin.

#### Ders Kitaplığı (Course Library)

**Ne işe yarar.** Programın yanındaki `Resources` klasöründeki kendi dosyalarınızı listeler.

**Nasıl kullanılır.** **Ders klasörünü aç** klasörü Dosya Gezgini'nde açar (Windows). PDF, ses veya metin dosyalarınızı kopyalayıp **Yenile**'ye basın; liste dosya adını, türünü ve MB cinsinden boyutunu gösterir. Bir satıra çift tıklamak dosyayı sistemin varsayılan uygulamasında açar (Windows).

**İpucu:** Alt klasörler de taranır; dersleri ünite ünite klasörlemek listeyi bozmaz.

### PRATİK

#### AI Öğretmen (AI Tutor)

**Ne işe yarar.** LM Studio'da çalışan yerel modele açıklama, çeviri, düzeltme ve görsel/OCR görevleri verir.

**Nasıl kullanılır.** **Görev** kutusundan **Açıkla**, **Çevir**, **Düzelt** ya da **Görsel / OCR**'yi seçin, metninizi üstteki kutuya yazın ve **Gönder**'e basın; yanıt alttaki salt okunur panelde belirir. Görsel için sağdaki **Görsel / OCR** düğmesiyle `.png`, `.jpg`, `.jpeg` veya `.webp` dosyası seçin, görev kendiliğinden değişir. Yerel AI kapalıysa ya da LM Studio'ya ulaşılamıyorsa `AI kapalı veya LM Studio erişilemiyor.` yazar. Bu sayfa yalnızca LM Studio'yu kullanır.

**İpucu:** Sayfanın altındaki `🔒 Prompt ve yanıt metni kaydedilmez; yalnızca token sayıları tutulur.` notu bu sayfanın gizlilik sözüdür.

#### Konuşma (Speaking)

**Ne işe yarar.** Seçtiğiniz senaryoda yerel yapay zeka ile yazışarak konuşma pratiği yaptırır.

**Nasıl kullanılır.** **Senaryo** kutusundan birini seçin (`At a café`, `At the station`, `At a hotel`, `In a shop`, `At the doctor's`) ve **Konuşmayı başlat**'a basın; karşı taraf kısa bir soru sorar. Alttaki kutuya İngilizce yanıtınızı yazıp **Gönder**'e basın. Panelde her zaman en son yanıt görünür; önceki metin bağlam olarak modele gönderilir.

**İpucu:** Rol yapma A1 düzeyi için kurgulanmıştır; kısa ve tam cümleler en iyi sonucu verir.

#### Yazma & El Yazısı (Writing & Handwriting)

**Ne işe yarar.** Serbest yazma metninizi yapay zekaya düzelttirir ve yazı çalışmanız için boş bir alan sunar.

**Nasıl kullanılır.** Soldaki yönergeyi (`Bugün ne yaptığınızı İngilizce yazın.`) okuyup metninizi kutuya yazın ve **AI ile düzelt**'e basın; alttaki panelde düzeltilmiş metin, kuralın adı ve kısa açıklama görünür. Sağdaki **El yazısı alanı**'na fareyle yazabilir, **Temizle** ile boşaltabilirsiniz. El yazısı alanı kaydedilmez.

**İpucu:** Düzeltmeyi okuduktan sonra aynı metni bir kez daha, düzeltmeye bakmadan yazın; kalıcılığı en çok bu ikinci deneme artırır.

### İLERLEME & SİSTEM

#### İlerleme (Progress)

**Ne işe yarar.** Günlük hedefinizi, serinizi ve son yedi günün çalışma yoğunluğunu gösterir.

**Nasıl kullanılır.** Sayfayı açın: üstte **Günlük hedef**, **Günlük seri**, **Çalışılan** ve **Öğrenilen** ölçütleri, altında **Son 7 gün** sütun grafiği ve **Haftalık rapor** satırı (`Doğru`, `Yanlış` ve yüzde olarak `Puan`) yer alır.

**İpucu:** Seri, arka arkaya çalıştığınız gün sayısıdır; kısa ama düzenli oturumlar onu korumanın en kolay yoludur.

#### Paketler (Packs)

**Ne işe yarar.** Kelimelerinizi (ve isterseniz ilerlemenizi) tek dosyada paketleyip başka bilgisayara taşır.

**Nasıl kullanılır.** İlerleme verisini de istiyorsanız **İlerlemeyi ekle** kutusunu işaretleyin, **↑ Dışa aktar**'a basıp `.ecapack` uzantılı bir ad verin (`Paket oluşturuldu` mesajı yolu gösterir). Karşı bilgisayarda **↓ İçe aktar** ile aynı dosyayı seçin; `Paket içe aktarıldı` mesajı kaç kelime alındığını söyler. Paket, `manifest.json` ve `data.json` içeren bir zip'tir; başka bir dilin uygulamasından gelen paket reddedilir.

**İpucu:** İçe aktarılan kelimeler karşı bilgisayardaki deste adlarını korur; yalnızca destesi olmayan satırlar `Paket` destesine düşer. Kelime Bankası'nda deste adına göre süzme yoktur, arama kutusu yalnızca İngilizce kelimede, Türkçe karşılıkta ve İngilizce ipucunda arar; desteyi **Deste** sütunundan görürsünüz.

#### Token Defteri (Token Ledger)

**Ne işe yarar.** Yapay zeka çağrılarının sayısal özetini tutar; metin içermez.

**Nasıl kullanılır.** Üstte **Çağrı** ve **Toplam token** ölçütleri, altında son 500 çağrının tablosu bulunur: zaman damgası, model, görev, istem tokenı, yanıt tokenı, toplam, milisaniye ve başarı durumu.

**İpucu:** Alternatif uç nokta ücretliyse harcamanızı buradan izleyin; **Task** sütunu `dictionary`, `grammar`, `translate`, `correct`, `dialogue` ve `vision` değerlerini alır.

#### Çevrimdışı Kılavuz (Offline Guide)

**Ne işe yarar.** Uygulamanın içindeki kısa yardım metnidir: hangi özelliklerin tamamen yerel çalıştığını, sözlük yönlerini ve CSV sütunlarını özetler.

**Nasıl kullanılır.** Sayfayı açıp okuyun; en altta, ayırıcı çizginin altında **veri klasörünüzün tam yolu** yazar. Yedek alırken bu yolu kullanın.

**İpucu:** İnternetsiz ortamda en hızlı başvuru kaynağı budur.

#### Ayarlar (Settings)

**Ne işe yarar.** Tema, hedef, ses, yerel yapay zeka ve alternatif uç nokta seçeneklerini toplar.

**Nasıl kullanılır.** Alanları düzenleyip **Kaydet**'e basın; `Ayarlar kaydedildi` yazar. Tema değiştiyse pencere yeniden çizilir.

| Alan | Anlamı | Varsayılan |
| --- | --- | --- |
| **Tema** | `dark` / `light` | `dark` |
| **Günlük hedef** | Günlük kart hedefi (5-200) | 20 |
| **Seslendirme** | Metin okuma açık/kapalı | açık |
| **Yerel AI** | LM Studio kullanımı açık/kapalı | açık |
| **LM Studio adresi** | Yerel sunucunun adresi | `http://127.0.0.1:1234` |
| **Varsayılan model** | Görevlerde tercih edilen model | `qwen2.5-7b-instruct` |
| **Sözlük AI kaynağı** | `Otomatik` / `LM Studio` / `Alternatif` / `Kapalı` | `Otomatik` |
| **AI sözlük sonuçlarını sözlüğe kaydet** | AI maddelerini önbelleğe alır | açık |
| **Alternatif uç noktayı kullan** | İkinci sağlayıcıyı etkinleştirir | kapalı |
| **Temel URL** | OpenAI uyumlu adres | `https://integrate.api.nvidia.com/v1` |
| **Model** | Alternatif uç noktadaki model adı | `meta/llama-3.1-8b-instruct` |
| **API anahtarı** | Yazıldığında güvenli depoya taşınır | boş |

**İpucu:** **Varsayılan model** kutusu gömülü profilleri listeler ama serbest metin de kabul eder; LM Studio'da yüklü modelin adını doğrudan yazabilirsiniz.

## 5. Sözlük (ayrıntılı)

**Sözlük EN-TR** sayfası üç katmanı birleştirir: programın içindeki **1210 gömülü madde**, sizin eklediğiniz maddeler ve yapay zekanın bulup önbelleğe aldığı maddeler. Her maddede İngilizce madde başı, Türkçe karşılık(lar), tür ve sade İngilizce tanım bulunur; düzensiz fiil ve çoğul biçimleri tanımın sonuna ` — ` işaretinden sonra eklenir (`tooth` maddesinde `— plural: teeth` gibi). **Ek bilgi** (IPA) ve **Örnek cümle** alanları gömülü maddelerde boştur; bu alanlar yapay zekanın bulduğu ve sizin eklediğiniz maddelerde dolar.

### Yön seçici

Araç şeridinin ikinci satırındaki **Yön:** kutusunda üç seçenek vardır.

| Seçenek | Aranan taraf | Ne zaman seçmeli |
| --- | --- | --- |
| **Otomatik** | Hem İngilizce madde başı/tanım hem Türkçe karşılık; en yüksek puanı alan taraf kazanır, eşitlikte madde başı öne geçer | Günlük kullanım; yazdığınız dilin hangisi olduğunu düşünmek istemiyorsanız |
| **EN → TR** | Yalnızca İngilizce madde başı ve İngilizce tanım | İngilizce bir kelimenin Türkçesini ararken |
| **TR → EN** | Yalnızca Türkçe karşılık | Türkçe bir kelimenin İngilizcesini ararken |

Sabit bir yönde yalnızca o yönün kaynak tarafı aranır; bu yüzden `TR → EN` seçiliyken `house` yazarsanız sonuç çıkmaz. Bu bir hata değil, yönün gereğidir. Seçiminiz ayarlara kaydedilir ve uygulamayı kapatıp açtığınızda korunur; yönü değiştirdiğinizde kutudaki sorgu yeni yönde tekrarlanır. Arama kutusunun sağındaki küçük etiket aramadan sonra geçerli yönü gösterir (`EN → TR` veya `TR → EN`); **Otomatik** modda bu, uygulamanın sizin için algıladığı yöndür.

### Türkçe sütunu ve detay paneli

Sol taraftaki tabloda beş sütun vardır.

| Sütun | İçerik |
| --- | --- |
| **İngilizce** | Madde başı |
| **Türkçe** | Karşılık(lar); birden çoksa `;` ile ayrılır |
| **Tür** | `isim`, `fiil`, `sıfat`, `zarf`, `zamir`, `edat`, `bağlaç`, `sayı`, `tanımlık`, `ünlem`, `parçacık`, `deyim` |
| **Ek bilgi** | IPA yazımı (`/brɪdʒ/` gibi); gömülü maddelerde boştur |
| **Kaynak** | `gömülü`, `kullanıcı` ya da `AI` |

Bir satır seçtiğinizde sağdaki panel açılır: büyük punto ile madde başı, altında tür ve ek bilgi satırı, **Türkçe:** karşılığı, tırnak içinde örnek cümle, sade İngilizce tanım ve kelime bankasında karşılığı varsa `★ Kelime Bankası: … (deste)` satırı. Düğmeler: **🔊 Seslendir**, **✦ AI'a sor**, **Kopyala**, **★ Kelime bankasına ekle** ve yalnızca kaydedilmemiş bir AI maddesi seçiliyken görünen **💾 Sözlüğe kaydet**. Altta son 12 sorgunuzu tutan **Son aramalar** listesi ile **AI yanıtı** paneli, en altta ise `1210 madde · gömülü 1210 · kullanıcı 0 · AI 0` biçiminde bir sayaç bulunur.

### Arama kuralları

- Kutuya **iki harften itibaren** yazdıkça liste anında süzülür; bu anlık arama yapay zekaya istek göndermez.
- **Enter** ya da **Ara** tam aramayı çalıştırır: sorgu geçmişe eklenir, sonuç yoksa yapay zekaya sorulabilir.
- Sıralama: **tam eşleşme** > `to`/`the`/`a`/`an` atıldıktan sonraki tam eşleşme > **önek** > **sözcük başı** > **içerme** (en az üç harf) > yalnızca tanımda geçme.
- Arama büyük-küçük harfe ve aksana duyarsızdır; Türkçe harfler katlanır (`ç/c`, `ğ/g`, `ş/s`, `ö/o`, `ü/u`) ve `İ`, `I`, `ı` aynı `i` gibi aranır. `IŞIK`, `ışık` ve `isik` aynı sonucu verir.
- **Düzensiz biçimler** tanımın içinde saklandığı için bulunur: `teeth` yazınca `tooth`, `went` yazınca `go` listelenir.
- Bir arama en fazla 200 sonuç döndürür.

### Kaynak etiketleri

| Etiket | Anlamı |
| --- | --- |
| **gömülü** | Programla gelen 1210 maddeden biri; silinemez, her kurulumda aynıdır |
| **kullanıcı** | **+ Madde ekle** ile eklediğiniz ya da CSV'den içe aktardığınız madde |
| **AI** | Yapay zekanın bulduğu ve yerel sözlüğe önbelleklenmiş madde |

Detay panelindeki tür satırında AI maddeleri için sonda `· AI` yazar.

### Yapay zeka ile eksik karşılığı doldurma

Sözlükte olmayan bir kelimeyi aradığınızda ve **AI:** politikası `Kapalı` değilse:

1. Durum çubuğunda `Sözlükte bulunamadı. AI'a sorabilir veya kendiniz ekleyebilirsiniz.` yazar ve arka planda sorulur (`AI'a soruluyor…`).
2. Yanıt yapılandırılmış JSON olarak gelir: madde başı, tür, IPA, Türkçe karşılık, örnek cümle ve sade İngilizce tanım; bir sorguda en çok 5 madde döner.
3. **AI sözlük sonuçlarını sözlüğe kaydet** açıksa (varsayılan) maddeler yerel sözlüğe yazılır; aynı kelimeyi bir daha aradığınızda çevrimdışı bulunur.
4. Maddeler listenin üstünde `AI` kaynağıyla görünür ve **AI yanıtı** paneline `— Yanıtlayan: LM Studio · …` satırıyla yazılır.
5. Yapay zeka madde bulamazsa `AI bu sorgu için madde döndürmedi.` yazar.

**✦ AI'a sor** düğmesi, sözlükte sonuç bulunsa bile sorar ve dönen maddeleri yerel sonuçların üstüne ekler. Otomatik kayıt kapalıysa maddeler geçicidir; kalıcı yapmak için maddeyi seçip **💾 Sözlüğe kaydet**'e basın. Yanıt gelene kadar sorguyu değiştirirseniz eski yanıt ekrana basılmaz (`Sorgu değiştiği için önceki AI yanıtı gösterilmedi.`); **AI sözlük sonuçlarını sözlüğe kaydet** açıksa üretilen maddeler yine de kaydedilir, kapalıysa kaybolur.

### Kelime bankasına ekleme

Seçili maddede **★ Kelime bankasına ekle**'ye basın. Kelime `Sözlük EN-TR` destesiyle Kelime Bankası'na yazılır; Türkçe alanına ilk karşılık, yanına örnek cümle ve tanım taşınır. Durum çubuğunda `Kelime bankasına eklendi: …` görünür, detay panelinde `★ Kelime Bankası: …` satırı belirir ve kelime artık Aralıklı Tekrar ile Sınav havuzundadır.

### CSV içe/dışa aktarma

**↑ CSV dışa aktar**, ekranda sonuç listesi varsa onu, yoksa sözlüğün tamamını yazar; pencere `exports` klasörünü ve `dictionary_en.csv` adını önerir.

| # | Sütun | İçerik |
| --- | --- | --- |
| 1 | `headword` | İngilizce madde başı |
| 2 | `translation` | Türkçe karşılık(lar), `;` ile ayrılır |
| 3 | `pos` | Tür kodu (`n`, `v`, `adj`, `adv`, `pron`, `prep`, `conj`, `num`, `art`, `int`, `part`, `phr`) |
| 4 | `extra` | IPA yazımı veya boş |
| 5 | `note` | Sade İngilizce tanım |
| 6 | `source` | `builtin`, `user` veya `ai` |
| 7 | `example` | Örnek cümle |

```csv
headword,translation,pos,extra,note,source,example
house,ev,n,,a building where people live,builtin,
tooth,diş,n,,one of the hard white things in your mouth — plural: teeth,builtin,
bridge,köprü,n,/brɪdʒ/,a structure built over a river or road,user,We walked across the old bridge.
```

**↓ CSV/TSV içe aktar**, `.csv`, `.tsv` ve `.txt` dosyalarını okur; ayırıcı kendiliğinden belirlenir. Başlık satırı tanınır ve **sütunlar herhangi bir sırada** olabilir: `word`, `target`, `en`, `english` madde başı; `meaning`, `tr`, `turkish`, `türkçe` karşılık; `definition` ise tanım sütunu sayılır. Başlık yoksa yukarıdaki sıra geçerlidir. Madde başı ya da karşılığı boş satırlar atlanır, maddeler `kullanıcı` kaynağıyla saklanır ve aynı (madde başı, karşılık) çifti iki kez eklenmez. Sonunda `N madde içe aktarıldı` yazar.

### Madde ekleme

**+ Madde ekle** küçük bir pencere açar; arama kutusundaki metin, algılanan yöne göre uygun alana kendiliğinden yazılır.

| Alan | Zorunlu | Açıklama |
| --- | --- | --- |
| **İngilizce** | evet | Madde başı (sözlük biçimi) |
| **Türkçe** | evet | Karşılık; birden çoksa `;` ile ayırın |
| **Tür (n/v/adj/…)** | hayır | Tür kodu |
| **Ek bilgi** | hayır | IPA yazımı |
| **Not / tanım** | hayır | Sade İngilizce tanım |
| **Örnek cümle** | hayır | Kısa örnek |

**Kaydet** (ya da Enter) maddeyi `kullanıcı` kaynağıyla ekler ve hemen arar; zorunlu alanlardan biri boşsa `İngilizce ve Türkçe alanları zorunlu.` uyarısı çıkar. **Esc** pencereyi kapatır.

## 6. Yapay zeka

### LM Studio kurulumu ve yerel sunucu

1. LM Studio'yu kurun ve bir sohbet modeli indirin.
2. OpenAI uyumlu **Local Server**'ı başlatın.
3. Varsayılan adres `http://127.0.0.1:1234`'tür; farklı port kullanıyorsanız **Ayarlar → LM Studio adresi** alanına yazıp **Kaydet**'e basın.

Uygulama sunucuya `GET /v1/models` ve `POST /v1/chat/completions` uç noktalarından bağlanır. LM Studio kapalıyken uygulama çalışmaya devam eder, yalnızca yapay zeka özellikleri devre dışı kalır.

### Model seçimi

Ayarlardaki **Varsayılan model** yüklüyse doğrudan kullanılır; değilse göreve göre bir profil listesi denenir, o da tutmazsa yüklü modeller sıralanıp en uygunu seçilir.

| Görev | Tercih sırası |
| --- | --- |
| `chat`, `dialogue`, `dictionary` | `qwen2.5-7b-instruct`, `llama-3.1-8b-instruct` |
| `grammar`, `correct` | `qwen2.5-7b-instruct`, `qwen2.5-14b-instruct` |
| `translate` | `qwen2.5-7b-instruct`, `gemma-2-9b-it` |
| `vision` | `qwen2-vl-7b-instruct`, `llava-v1.6-mistral-7b` |

**Uzman modeller neden atlanır?** Gömme (`embed`), yeniden sıralama (`rerank`), matematik (`math`), kod (`coder`, `code-`), görüntü (`vision`, `-vl`, `llava`, `moondream`, `clip`), tıp (`bio`, `medic`), ses (`whisper`, `tts`, `audio`) ve görsel üretim (`sd-`, `stable-diffusion`) modelleri sözlük ve sohbet görevlerinde işe yaramaz; adında bu izlerden biri geçen model en sona atılır ve yalnızca başka model yoksa kullanılır. Eşitlikte 4-16 milyar parametreli, adında `instruct`/`chat`/`-it` geçen genel modeller öne alınır; bu boyut sıradan bir dizüstü bilgisayara sığar.

**Düşünen modeller.** Bazı modeller bütçenin tamamını akıl yürütmeye harcayıp boş yanıt döndürür. Uygulama yerel sunuculara `reasoning_effort: "none"` gönderir; sunucu bu alanı reddederse istek alansız yinelenir. Yanıt boş ve kesilmiş geldiyse üç kat bütçeyle bir kez daha denenir.

### Alternatif uç nokta

Sözlük, LM Studio yerine ya da yanı sıra OpenAI uyumlu herhangi bir servisi kullanabilir: NVIDIA NIM, OpenRouter, Groq, ağdaki bir Ollama sunucusu…

1. **Ayarlar** sayfasında **Alternatif uç nokta** başlığını bulun ve **Alternatif uç noktayı kullan** kutusunu işaretleyin.
2. **Temel URL** alanına adresi (varsayılan `https://integrate.api.nvidia.com/v1`), **Model** alanına model adını (varsayılan `meta/llama-3.1-8b-instruct`) yazın.
3. **API anahtarı** alanına anahtarınızı yapıştırın; alan noktalarla (•) gizlenir.
4. **Kaydet**'e basın: alan boşalır ve yanında `••••• kayıtlı` yazar.
5. **Bağlantıyı test et** ile deneyin; `Bağlantı başarılı · N model` beklenir. Model listede yoksa `seçili model listede yok`, anahtar eksikse `anahtar kaydedilmeden sözlük bu uç noktayı kullanmaz` uyarısı eklenir.

`https://` ile başlayan uzak adresler anahtar ister; `127.0.0.1` ve `localhost` gibi yerel adresler ile düz `http://` ağ sunucuları anahtarsız kabul edilir.

**Anahtarınızın saklandığı yer.** Windows'ta anahtar **Windows Kimlik Bilgisi Yöneticisi**'nde `EnglishCourseAI/alt_api_key` adlı genel kimlik bilgisi olarak tutulur; diğer sistemlerde veya bu API başarısız olursa `settings/secrets.json` dosyasına düşer (destekleyen sistemlerde 0600 izniyle). Anahtar **hiçbir zaman** `settings.json` içine yazılmaz. `ENGLISHCOURSEAI_API_KEY` ortam değişkeni tanımlıysa kayıtlı anahtarın yerine o kullanılır. **Anahtarı sil** düğmesi kaydı kaldırır (`Anahtar silindi`).

### AI politikası

**Sözlük AI kaynağı** hem Ayarlar sayfasında hem sözlük araç şeridindeki **AI:** kutusundadır; ikisi aynı ayarı gösterir.

| Politika | Davranış |
| --- | --- |
| **Otomatik** | LM Studio erişilebilirse onu kullanır; değilse etkinleştirilmiş alternatif uç noktaya geçer; o da yoksa yapay zeka kullanılmaz |
| **LM Studio** | Yalnızca yerel sunucu; **Yerel AI** açık ve sunucu erişilebilir olmalı |
| **Alternatif** | Yalnızca alternatif uç nokta; etkin olmalı ve gerekiyorsa anahtar kayıtlı olmalı |
| **Kapalı** | Sözlük hiçbir yapay zeka isteği göndermez; AI Öğretmen, Konuşma ve Yazma & El Yazısı bundan etkilenmez |

Araç şeridindeki etiket seçili politikanın o anki karşılığını gösterir: `LM Studio: bağlı`, `Alternatif: hazır`, `AI erişilemiyor` ya da `AI kapalı`. Erişilebilirlik yanıtı 30 saniye önbelleklenir, bu yüzden LM Studio'yu yeni başlattıysanız etiket biraz gecikebilir. Alternatif uç noktayı yalnızca **Sözlük** sayfası kullanır; **AI Öğretmen**, **Konuşma** ve **Yazma & El Yazısı** her zaman LM Studio üzerinden çalışır.

### Token defteri ve gizlilik

Her çağrı **Token Defteri**'ne bir satır yazar: zaman, model, görev, istem tokenı, yanıt tokenı, toplam, süre (ms) ve başarı durumu. **İstem ve yanıt metni hiçbir yerde saklanmaz** - ne veritabanında ne de günlük dosyalarında. Sözlük soruları modele 0,1 sıcaklıkla, en fazla 1200 token bütçesiyle ve 90 saniyelik zaman aşımıyla gönderilir.

## 7. Veri yönetimi

**Profiller.** Üst şeritteki kutu profil değiştirir, **+** düğmesi yeni profil açar (bir ad sorulur). Profil başına ayrı tutulanlar: tekrar planı ve ilerleme, çalışma günlüğü, sınavlar, PDF sayfa notları ve dilbilgisi istatistikleri. Ortak olanlar: Kelime Bankası, sözlük maddeleri, token defteri ve ayarlar. Profil silme arayüzde yoktur.

**Yedekleme.**

| Yöntem | Ne kapsar | Nasıl |
| --- | --- | --- |
| Veritabanı kopyası | Her şey | `…\EnglishCourseAI\data\EnglishCourseAI.db` dosyasını uygulama kapalıyken kopyalayın |
| Kelime CSV'si | Kelime Bankası | **Kelime Bankası → ↑ Dışa aktar** |
| Sözlük CSV'si | Sözlük maddeleri | **Sözlük EN-TR → ↑ CSV dışa aktar** |
| Paket dosyası | Kelimeler (+ isteğe bağlı ilerleme) | **Paketler → ↑ Dışa aktar** (`.ecapack`) |

**Veri klasörü ve sıfırlama.** Klasörün tam yolunu **Çevrimdışı Kılavuz** sayfasının altında görürsünüz. Uygulamayı kapatın; her şeyi sıfırlamak için veri klasörünü silin ya da yeniden adlandırın (bir sonraki açılışta boş kurulum oluşur), yalnızca ayarları sıfırlamak için `settings/settings.json` dosyasını silin, denemek için `ECA_HOME` ile geçici bir klasör gösterin. API anahtarı veri klasöründe değil işletim sisteminin güvenli deposundadır; klasörü silmek anahtarı silmez, bunun için **Ayarlar → Anahtarı sil** düğmesini kullanın.

## 8. Kısayollar ve ipuçları

Uygulamada menü kısayolu yoktur; aşağıdakiler kodda tanımlı gerçek kısayollardır.

| Kısayol | Nerede | Ne yapar |
| --- | --- | --- |
| **Enter** | Sözlük arama kutusu | Tam aramayı çalıştırır (gerekirse yapay zekaya sorar) |
| İki harften itibaren yazmak | Sözlük arama kutusu | Anında süzer, yapay zekaya istek göndermez |
| **Çift tıklama** | Sözlük sonuç listesi | Seçili maddeyi seslendirir |
| **Enter** | Kelime Bankası arama kutusu | Aramayı çalıştırır |
| **Enter** | Madde ekle penceresi | Maddeyi kaydeder |
| **Esc** | Madde ekle penceresi | Pencereyi kapatır |
| **Çift tıklama** | Ders Kitaplığı listesi | Dosyayı varsayılan uygulamada açar (Windows) |

- **Yönü sabitleyin:** uzun bir Türkçe metinden kelime çalışıyorsanız `TR → EN` yanlış eşleşmeleri tamamen keser.
- **🎲 Rastgele kelime**, seçili yöne uygun tarafı bilinen bir gömülü madde çeker; sabit yönde bile hep sonuç bulur ve gereksiz yapay zeka isteği doğurmaz.
- **Son aramalar** listesindeki satıra tıklamak aramayı tekrarlar.
- **Kopyala**, maddeyi `kelime — karşılık` biçiminde panoya alır.
- Ayarlar sayfası her açılışında güncel değerleri okur; sözlük araç şeridinden değiştirdiğiniz AI politikası orada da görünür.

## 9. Sorun giderme

**LM Studio'ya bağlanılamıyor (`AI: Kullanılamıyor`, `AI erişilemiyor`).** Genellikle yerel sunucu başlatılmamıştır: LM Studio'yu açıp Local Server'ı başlatın. Ardından Ayarlar'daki **LM Studio adresi** ile LM Studio'nun gösterdiği adres/port aynı mı bakın ve **Kaydet**'e basın; kaydetmek istemcileri tazeler. **Yerel AI** kutusunun işaretli olduğundan emin olun. Erişilebilirlik yanıtı 30 saniye önbelleklendiği için etiket hemen değişmeyebilir; 30 saniye geçtikten sonra sözlük sayfasından çıkıp dönmek durumu yeniden ölçtürür. Üst şeritteki `AI:` rozeti yalnızca açılışta ölçülür, sonradan güncellenmez.

**Yapay zeka boş yanıt veriyor (`AI bu sorgu için madde döndürmedi.`).** En sık neden, "düşünen" bir modelin bütçeyi akıl yürütmeye harcamasıdır; uygulama bunu bir kez üç kat bütçeyle yineler. Yine boşsa LM Studio'da düşünmeyen, 4-16 milyar parametreli bir `instruct` modeli yükleyip adını **Varsayılan model** alanına yazın. Belleğe sığmayan model yanıtları çok yavaşlatır ya da kestirir; yüklü tek model matematik, gömme veya görüntü modeliyse sözlük anlamlı yanıt üretemez.

**Bir kelimenin Türkçe karşılığı yok / sonuç bulunamıyor.** Önce yönü kontrol edin: `TR → EN` yalnızca Türkçe karşılıkları, `EN → TR` yalnızca İngilizce tarafı arar; emin değilseniz **Otomatik**'e alın. Kelime gömülü sözlükte yoksa ve AI politikası `Kapalı` ise ya da sağlayıcıya ulaşılamıyorsa `Sözlükte bulunamadı…` yazısı kalır. O zaman ya bir sağlayıcı bağlayın, ya **+ Madde ekle** ile kendiniz girin, ya da hazır bir CSV listesi içe aktarın.

**macOS "uygulama açılamıyor" uyarısı veriyor.** Paket notarize edilmemiştir: simgeye sağ tıklayıp (veya Control ile tıklayıp) **Aç**'ı seçin, çıkan uyarıda yine **Aç**'a basın. Bir kez izin verdikten sonra çift tıklama çalışır. Uyarı yine çıkarsa **Sistem Ayarları → Gizlilik ve Güvenlik** bölümünün altındaki **Yine de Aç** düğmesini kullanın.

**Ses çıkmıyor.** Seslendirme, Windows'un `System.Speech` bileşenini PowerShell üzerinden çağırır ve kurulu `en-*` seslerden ilkini seçer. İngilizce ses paketi yoksa varsayılan ses okur ya da hiç ses çıkmaz; Windows ayarlarından bir İngilizce ses ekleyin ve **Ayarlar → Seslendirme** kutusunun işaretli olduğunu doğrulayın. macOS ve Linux'ta bu bileşen bulunmadığından seslendirme sessizce çalışmaz.

**exe açılmıyor.** Zip'i çıkarmadan içinden çalıştırmayın. SmartScreen uyarırsa **Ek bilgi → Yine de çalıştır**'ı seçin. Bazı virüs korumaları PyInstaller ile paketlenmiş dosyaları karantinaya alır; karantina listesine bakın ve gerekirse klasörü ayrıcalıklı listeye ekleyin. `%APPDATA%` yazma korumalıysa uygulama veri klasörünü oluşturamaz; `ECA_HOME` ile yazılabilir bir klasör gösterin.

**Verilerim nerede?** Tam yol **Çevrimdışı Kılavuz** sayfasının en altında yazılıdır: Windows'ta `%APPDATA%\EnglishCourseAI`, diğer sistemlerde `~/.englishcourseai`. `ECA_HOME` tanımlıysa o klasör geçerlidir.

## 10. Sürüm notları özeti

| Sürüm | Öne çıkanlar |
| --- | --- |
| **v1.0.0** | İlk sürüm: 17 sayfa, SM-2/Leitner tekrar, 162 kelimelik A1 düzeyi başlangıç seti, sınav, yazım/telaffuz/dilbilgisi laboratuvarları, PDF notları, Kaynak Merkezi, paketler, LM Studio ile AI Öğretmen, Türkçe ve İngilizce arayüz |
| **v1.1.0** | **Sözlük EN-TR** sekmesi (1210 gömülü madde, çift yönlü arama, seslendirme, CSV içe/dışa aktarma) ve sözlük için **AI bağlantısı**: LM Studio ya da OpenAI uyumlu alternatif uç nokta, anahtar Kimlik Bilgisi Yöneticisi'nde, sonuçlar yerel sözlüğe önbelleklenir |
| **v1.1.1** | Düşünen modellerde boş yanıt düzeltmesi (`reasoning_effort`) ve uzman modelleri eleyen model seçimi |
| **v1.1.2** | Sözlük AI cilası: ek bilgi alanının temizlenmesi, AI yanıtından sonra yön etiketi, araç şeridinin ayrı satıra alınması, tekrar eden anlamların ayıklanması |
| **v1.2.0** | **Yön seçici**: `Otomatik`, `EN → TR`, `TR → EN`; sabit yönde yalnızca kaynak taraf aranır ve seçim ayarlara kaydedilir. Türkçe sözlük motorunda tam bir üçüncü dil olarak ele alınır; CSV içe aktarımı başlık satırını tanır ve sütunları herhangi bir sırada kabul eder |
| **v1.2.1** | Türkçe aramada **ASCII ve büyük harf desteği**: `sinav` = `SINAV` = `sınav`, `cok` = `çok`, `ogrenci` = `öğrenci`. Türkçe sütunu karşılaştırmada ASCII'ye katlanır, gösterilen yazım değişmez ve katlanarak bulunan eşleşme doğrudan eşleşmenin altına oranlanır; böylece `ask` yazan kullanıcı İngilizce karşılığını alır. Ayrıca bu **kullanım kılavuzu** (Türkçe ve İngilizce) depoya eklendi; PDF sürümü sürüm ekleri arasında yayımlanır |

## 11. Sık sorulan sorular

**1. Uygulamayı kullanmak için internet gerekir mi?** Hayır. Tekrar, Kelime Bankası, sözlük (1210 gömülü madde), sınav, laboratuvarlar, PDF notları, paketler ve ilerleme tamamen yereldir. İnternet yalnızca Kaynak Merkezi bağlantılarında ve alternatif uzak uç noktada devreye girer.

**2. Yapay zeka olmadan da işime yarar mı?** Evet. AI politikasını `Kapalı` yaparsanız **sözlük** hiçbir istek göndermez ve gömülü maddelerle çalışır; AI Öğretmen, Konuşma ve **AI ile düzelt** bundan etkilenmez - onları da kapatmak için **Ayarlar → Yerel AI** kutusunun işaretini kaldırın.

**3. Sözlükte kaç madde var?** Programla 1210 madde gelir; kendi eklediğiniz ve önbelleğe alınan AI maddeleri buna eklenir. Güncel toplamı sözlük sayfasının altındaki sayaçta kaynak kaynak görürsünüz.

**4. Yön seçicide hangi seçeneği kullanmalıyım?** Günlük kullanımda **Otomatik** yeterlidir; tek yönde çalışıyorsanız ilgili sabit yön yanlış eşleşmeleri tamamen keser. Seçiminiz kaydedilir.

**5. `TR → EN` seçiliyken İngilizce kelime yazınca neden sonuç çıkmıyor?** Sabit yönler yalnızca kendi kaynak tarafını arar; `TR → EN` sadece Türkçe karşılıklara bakar. **Otomatik**'e geçin ya da yönü `EN → TR` yapın.

**6. API anahtarım güvende mi?** Windows'ta Kimlik Bilgisi Yöneticisi'nde, diğer sistemlerde yalnızca yerel bir gizli dosyada saklanır. Ayar dosyasına asla yazılmaz, dışa aktarımlarda ve paketlerde yer almaz; **Anahtarı sil** ile istediğiniz an kaldırırsınız.

**7. Yapay zekaya yazdıklarım kaydediliyor mu?** Hayır. Ne istem ne de yanıt metni saklanır; Token Defteri yalnızca model, görev, token sayıları, süre ve başarı bilgisini tutar.

**8. Verilerimi başka bilgisayara nasıl taşırım?** En kolayı **Paketler** sayfasından `.ecapack` üretip karşı tarafta içe aktarmaktır; birebir taşımak için veri klasöründeki `EnglishCourseAI.db` dosyasını kopyalayın.

**9. Kendi kelimelerimi nasıl eklerim?** Sözlüğe **+ Madde ekle** ile tek tek, **↓ CSV/TSV içe aktar** ile toplu ekleyin; çalışma listenize almak için **★ Kelime bankasına ekle**'yi kullanın. Kelime Bankası'nın kendi CSV içe aktarımı da vardır.

**10. Sınav düzeyini değiştirebilir miyim?** Bu sürümde arayüzde CEFR seçimi yoktur; sınav kaydına ayar dosyasındaki `cefr` değeri (varsayılan `A1`) yazılır. Soru sayısını **Soru sayısı** sayacından ayarlayabilirsiniz.

**11. Mikrofonla telaffuzumu neden karşılaştıramıyorum?** **◉ Mikrofonla karşılaştır** bu sürümde etkin değildir ve **Kullanılamıyor** yazar; uygulama ses kaydı almaz. Telaffuz sayfasını dinleme ve IPA karşılaştırması için kullanın.

**12. Aynı bilgisayarda iki kişi çalışabilir mi?** Evet. **+** düğmesiyle ikinci bir profil açın; tekrar planı, sınavlar, PDF notları ve istatistikler profil başına ayrılır, kelime listesi ile sözlük ve ayarlar ortaktır.

## 12. Lisans

English Course AI, MIT Lisansı ile yayımlanır; tam metin depo kökündeki [`LICENSE`](../LICENSE) dosyasındadır. Uygulamayla gelen kelime, sözlük, dilbilgisi ve alıştırma içeriği bu proje için yazılmıştır ve aynı lisans kapsamındadır.

Uygulamanın kullandığı ve paketlenmiş sürümlerin (Windows `.exe`, macOS `.app`) içinde yer alan üçüncü taraf bileşenlerin tamamı, gerçek lisanslarıyla birlikte [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) dosyasında listelenir. Kaynak Merkezi'ndeki dış kaynaklar uygulamaya kopyalanmaz; oradan indirdiğiniz her şey kendi lisansına tabidir.
