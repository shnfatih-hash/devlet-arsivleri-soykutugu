---
name: devlet-arsivleri-soykutugu
description: >-
  e-Devlet Alt-Üst Soy Bilgisi belgesi, Chrome DevTools MCP ve/veya indirilmiş
  filigransız arşiv görüntüleri (.zip/.jpg) kullanarak T.C. Cumhurbaşkanlığı
  Devlet Arşivleri Başkanlığı Kataloğu (katalog.devletarsivleri.gov.tr) üzerinde
  anne ve baba tarafı soy kütüğünü 1500'lere kadar indirme; Osmanlı Nüfus
  (NFS.d), Temettuat (ML.VRD.TMT.d), Şer'iyye Sicilleri (MŞH.ŞSC.d), İmam-Muhtar
  (A.{RSK.d), Avârız (MAD.d), Tapu Tahrir (TT.d / TK.GM.d) ve Göçmen/Mübadil
  (BCA 130.16.13.2, DH.SN.THR) fonlarından 1:1 belge kesitiyle kanıtlı soy ağacı
  ve köy/mahalle tarihi çıkarma becerisi. Kullanıcı soy ağacı, soy kütüğü, ata
  kaydı, eski köy adı, mübadil/muhacir kaydı veya Osmanlıca arşiv okuması
  istediğinde etkinleştirin.
---

# Devlet Arşivleri Soy Kütüğü ve Köy Tarihi Araştırma Becerisi

Bu beceri, **Said Sürücü**'nün seminerinden hareketle geliştirilmiş olup; kullanıcının **e-Devlet Alt-Üst Soy Bilgisi** belgesindeki en eski kayıt duvarını ("Kütük Duvarı", 1881–1905) aşarak, **T.C. Cumhurbaşkanlığı Devlet Arşivleri Başkanlığı Kataloğu** (`https://katalog.devletarsivleri.gov.tr`) ve indirilen orijinal defter görüntüleri üzerinden **anne ve baba tarafı soy kütüğünü**, **köyün/mahallenin eski adını ve idari evrimini**, **köydeki önemli şahsiyetleri** ve **tarihî olayları** 16. yüzyıla kadar kanıtlı biçimde araştırır.

- **Fon Kodları, Takvim Hesabı, Varyant Matrisi ve Sözlük:** [fon-kodlari-ve-paleografya-rehberi.md](./references/fon-kodlari-ve-paleografya-rehberi.md)
- **Balkanlar, Adalar, Girit ve Kafkasya Göçmen/Mübadil Rehberi:** [gocmen-ve-mubadil-rehberi.md](./references/gocmen-ve-mubadil-rehberi.md)
- **Tarayıcı İçi Güvenli Arama ve Varak Ayırma Yardımcıları:** [dab_helpers.js](./scripts/dab_helpers.js)
- **İndirilen `.zip / .jpg` Belgelerden 1:1 Piksel Kesiti Alma Aracı:** [crop_and_verify.py](./scripts/crop_and_verify.py)
- **3 Yönlü Hicrî ↔ Rûmî ↔ Milâdî Tarih Çevirici:** [tarih_cevirici.py](./scripts/tarih_cevirici.py)
- **GEDCOM İçe Aktarma, Doğrulama & İnteraktif HTML Göç Haritası Üretici:** [soyagaci_ve_harita.py](./scripts/soyagaci_ve_harita.py)
- **Kullanıcılar İçin Hazır Şablon İstemler:** [ornek-kullanim-promptlari.md](./examples/ornek-kullanim-promptlari.md)

---

## Güvenlik, Mahremiyet, Yerleşik Tarayıcı Yasağı ve Hız Sınırı Kuralları (Zorunlu)

1. **Şifre, Kimlik ve "Dış Aramalarda İsim Kullanmama" Gizlilik Kuralı:**
   - Kullanıcının T.C. Kimlik Numarasını veya e-Devlet şifresini **asla** istemeyin. Kullanıcı `https://katalog.devletarsivleri.gov.tr` adresine kendi normal Google Chrome tarayıcısında bizzat giriş yapar.
   - **Dış aramalarda kişi adı sızdırmama:** Web aramaları, akademik API'ler (DergiPark, OpenAlex, Nişanyan Map vb.) ve görsel aramaları yalnızca **yer adı, yıl ve konu** içerir; yaşayan veya gerçek şahıs isimleri kullanıcının açık onayı olmadan dış arama motorlarına gönderilmez. Üretilen rapor ve haritalar yerel dosya olarak kalır.
2. **Antigravity Yerleşik Tarayıcısı (`browser` Alt-Ajanı) Yasağı — `"Web Sayfasına Erişim Engellendi"` Çözümü:**
   - `katalog.devletarsivleri.gov.tr` veya `turkiye.gov.tr` adreslerini **ASLA** Antigravity'nin kendi dahili tarayıcısında (`browser` subagent / yerleşik webview) açmayın! Kurum güvenlik duvarı yerleşik tarayıcıyı *"(!) Web Sayfasına Erişim Engellendi"* uyarısıyla engeller.
   - Yalnızca **`chrome-devtools` MCP** üzerinden kullanıcının bilgisayarındaki **normal Google Chrome** oturumuna bağlanın.
   - Kullanıcı *"Web Sayfasına Erişim Engellendi"* ekranıyla karşılaşırsa veya Antigravity içi tarayıcı açılmışsa şu 3 adımı anlaşılır dille tarif edin:
     1. Antigravity'nin sağ panelindeki dahili tarayıcı sekmesini kapatın.
     2. Bilgisayarınızdaki **normal Google Chrome** uygulamasını açın; yeni sekmede `chrome://inspect/#remote-debugging` adresine gidip **Enable remote debugging** kutucuğunu işaretleyin ve Devlet Arşivleri'ne normal Chrome üzerinden e-Devlet ile girin.
     3. Sohbette *"Kendi tarayıcını açma, Chrome DevTools MCP ile açık Google Chrome sekmeme bağlan"* diyerek devam edin (veya MCP kurmadan doğrudan normal Chrome'dan indirdiğiniz `.zip / .jpg` dosyalarını proje klasörüne koyup **Mod B** ile okutun).
3. **Doğrulama / CAPTCHA ve WAF (`HTTP 418`) Kuralı:**
   - e-Devlet giriş ekranı, oturum zaman aşımı veya herhangi bir doğrulama/CAPTCHA ekranıyla karşılaşıldığında **derhal durun** ve işlemi tarayıcıda kullanıcının tamamlamasını isteyin.
   - `BelgeGoster.aspx` görüntü sunucusuna **asla paralel (`Promise.all`) çoklu istek göndermeyin**; paralel istekler güvenlik duvarını (`HTTP 418 — Erişim Engellendi`) tetikler. Yalnızca sıralı ve en az `1800 ms` aralıklı istek kullanın; `HTTP 418` alınırsa otomatik görüntü çekimini derhal durdurup kullanıcıya tam defter ve poz (`Mi`) numaralarını verin.
4. **Sıfır Uydurma, Sıfır Atlama ve 1:1 Kesit Disiplini:** Osmanlıca el yazmasında okunamayan veya filigran altında kalan harfleri **asla tahminle tamamlamayın**; `[şüpheli okuma / filigran altında: ...]` olarak işaretleyin. Her kritik hane ve isim satırını [crop_and_verify.py](./scripts/crop_and_verify.py) veya `<canvas>` ile **1:1 piksel kesiti** alarak doğrulayın. Şer‘iyye sicili hüccet/terekelerinde ve vakfiyelerde Arapça/Osmanlıca dua, vakıf şartı, kenar `sahh` (`صح`) tashihi, satır üstü yoklama şerhi ve `şuhûdü'l-hâl` listelerini *"klasik formüldür"* diyerek özetleyip atlamayın; varak geçişlerinde **rekabe (*müş‘ir kelime*)** takibiyle bölünen hane veya miras kayıtlarını birleştirin.

---

## Çalışma Modları

Kullanıcının elindeki veriye göre uygun modu (veya birleşimini) çalıştırın:

- **Mod A — Canlı Katalog ve Fihrist Keşfi (`Chrome DevTools MCP`):** Kullanıcının açık normal Google Chrome oturumunda fon/defter araması yapar, fihrist (`Mi=1..5`) sayfalarını okuyarak doğru defteri ve tam varak/poz aralığını tespit eder (kullanıcının yanlış defteri toptan satın almasını önler).
- **Mod B — İndirilmiş Filigransız `.zip / .jpg` Klasöründen 1:1 Paleografik Okuma (MCP Gerektirmez):** Kullanıcının normal Chrome üzerinden e-Satış sepetinden indirip proje klasörüne koyduğu yüksek çözünürlüklü (`.zip` veya `.jpg`) defter sayfalarını [crop_and_verify.py](./scripts/crop_and_verify.py) ile sağ/sol varak ve 1:1 satır kesitlerine ayırarak sıfır filigran hatasıyla okur.
- **Mod C — Çok Sayfalı Defterlerde Paralel Alt-Ajan (`Subagents`) + Ortak Sözlük (`glossary.md`) Orkestrasyonu:** 20–100+ sayfalık büyük defter/evrak serilerinde sayfaları 10'arlı gruplar halinde paralel alt-ajanlara dağıtır; tüm ajanların ortak okuduğu bir `glossary.md` (köy lakapları, şahıs ve yer adı imlâları) dosyası tutar ve işlem sonunda bir **Tutarlılık Denetçisi Ajan** çalıştırarak tüm sayfalar arasında isim, yaş ve kuşak bütünlüğünü doğrular (ayrıntılı yazma eser tercümesi için kardeş beceri `yazma-eser-paralel-tercume` ile uyumludur).

---

## Adım 0: Proje Klasörü ve Oturum Hazırlığı

1. **Özel Proje Klasörü (`Workspace`) Düzeni:** Kullanıcı henüz bir çalışma klasörü açmadıysa masaüstünde/belgelerinde müstakil bir klasör (ör. `Soy_Kutugu_Arastirmam`) oluşturup Antigravity'de **Open Folder** ile açmasını önerin. İndirilen kaynak belgeleri, `kesitler/` alt klasöründeki 1:1 kanıt görsellerini ve üretilen `.md / .html / .docx` raporlarını düzenli olarak bu proje klasörüne kaydedin.
2. `chrome-devtools` MCP sunucusu etkin değilse (Mod A için) resmi `chrome-devtools-mcp` kurulumunu önerin:
   - Gereksinimler: Google Chrome (`https://www.google.com/chrome/`) ve Node.js LTS (`https://nodejs.org`).
   - `mcp_config.json` tanımı:
     ```json
     {
       "mcpServers": {
         "chrome-devtools": {
           "command": "npx",
           "args": ["-y", "chrome-devtools-mcp@latest", "--autoConnect"]
         }
       }
     }
     ```
3. Kullanıcıdan **normal Google Chrome**'da `chrome://inspect/#remote-debugging` sayfasından **Enable remote debugging** kutusunu işaretlemesini ve yeni sekmede `https://katalog.devletarsivleri.gov.tr/Sayfalar/Arama/Arama.aspx` adresine e-Devlet ile giriş yapmasını isteyin.
4. `<appDataDir>/mcp/chrome-devtools/` altındaki şema dosyalarını (`list_pages.json`, `evaluate_script.json`, `navigate_page.json`) okuyun ve `list_pages` ile katalog sekmesinin `pageId` değerini alın.
   - *Teknik İpucu:* Büyük arşiv sayfalarında `take_screenshot` (`fullPage: true`) zaman aşımına uğrayabileceğinden, görüntü aktarımında `dab_helpers.js` içindeki `<canvas>` `toDataURL('image/jpeg', 0.88)` çıktısını tercih edin.

---

## Adım 1: "Kütük Duvarı" Analizi ve 4 Temel İpucunun Çıkarılması

Kullanıcının `https://www.turkiye.gov.tr/nvi-alt-ust-soy-bilgisi-sorgulama` adresinden indirdiği belgeden **veya İl/İlçe Nüfus Müdürlüğü'nden temin ettiği vukuatlı nüfus kayıt örneği / eski esas kütük bilgisinden** **Baba Tarafı** ve **Anne Tarafı** için ayrı ayrı **4 Temel İpucunu** çıkarın:

1. **Köy / Mahallenin Eski Adı:** Cumhuriyet döneminde değişmişse 1928 *Son Teşkilât-ı Mülkiyede Köylerimizin Adları* ve yerel kaynaklardan Osmanlıca adını ve tüm fonetik varyantlarını (`k/g/ğ`, `t/d`, `b/p`, `c/ç`, ünlü düşmesi) üretin (ör. *Güzelyurt ← Gelveri*, *Yeşilköy ← Ayastefanos*).
2. **1934 Öncesi Sülale Lakapları ve Oymak Adları (En Güçlü Anahtar):** `...oğulları`, `...zâde`, `...uşağı`, `...gil`, meslek unvanları (*Demircioğlu, Hacıalioğlu, Molla...*) veya dul annenin adından türeyen lakaplar. Aile lakabı biliniyorsa nüfus ve temettuat defterlerinde hane tespiti çok hızlanır. Kadın atalarda soyadının babadan değil eşin hanesinden gelebileceğini dikkate alın.
3. **Kütükteki En Eski Atalar ve Doğum Tarihleri:**
   - Nüfus esas kütükleri bazı sancaklarda **1881–1883 (`R. 1297–1299`)**, bazılarında **1904–1905 (`R. 1320`)**, yangın/işgal gören yerlerde ise daha geç başlar. İlk sayımdan önce vefat eden büyük dedeler ayrı satır olarak açılmaz; yalnızca çocuğunun **"Baba Adı"** hanesinde görünür.
   - Bu en eski atanın doğum yılından [tarih_cevirici.py](./scripts/tarih_cevirici.py) ile Milâdî → Hicrî/Rûmî dönüşüm yaparak 1831–1848 nüfus ve 1844–1845 temettuat defterlerindeki beklenen yaşını hesaplayın.
4. **Osmanlı İdari Zinciri (`Eyâlet/Vilâyet → Sancak/Livâ → Kazâ → Nâhiye`):**
   - Bugün X ilçesine bağlı bir köy, 19. yüzyılda komşu bir **nahiye veya kazaya** bağlı olabilir. Çevredeki tüm komşu kaza ve nahiyeleri arama havuzuna ekleyin.
   - Aile Balkanlar, Adalar veya Kafkasya göçmeni/mübadili ise doğrudan [gocmen-ve-mubadil-rehberi.md](./references/gocmen-ve-mubadil-rehberi.md) iş akışını devreye sokun (`https://www.turkiye.gov.tr/nvi-isim-denklik-belgesi-talep-ve-sorgulama`, `BCA 130-16-13-2`, `DH.SN..THR.`).

---

## Adım 2: 500 Yıllık Arşiv Merdiveni ve Bütçe Koruyan "Önce Fihrist" Taktiği

Arşivde günümüzden 1500'lere doğru şu **6 basamaklı merdiveni** izleyin:

1. **1881–1905 (`Sicill-i Nüfus Atîk/Esas Kütükleri` & Nüfus Müdürlüğü Kayıtları):** e-Devlet soy ağacının ve Nüfus Müdürlüğü kayıtlarının dayandığı başlangıç katmanı.
2. **1830–1880 (`BOA, NFS.d..` & `D..CRD.d...` — Nüfus ve Yoklama Defterleri):** Köydeki tüm erkekleri hane hane, baba adıyla (`bin / veled-i`), sülale lakabıyla, yaşıyla (`sinn`), boy ve sakal/bıyık eşkâliyle, doğum (`tevellüd`), ölüm (`fevt`) ve askerlik (`reft be-askeriyye`, `redîf`) şerhleriyle kaydeder. *(Balkan sancaklarının 1830–1875 `NFS.d` defterleri de bu fondadır!)*
3. **1844–1845 (`BOA, ML.VRD.TMT.d...` — Temettuat Defterleri) & 1835–1838 (`A.{RSK.d...` — İmam-Muhtar Defterleri):** Hane reisinin mesleğini, tarla dönümünü, hayvanlarını, yıllık gelirini ve köyün ilk muhtar/imamlarını verir.
4. **1500–1924 (`BOA, MŞH.ŞSC.d` / `kadisicilleri.org` — Şer'iyye Sicilleri & `EV.d` Vakıf Kayıtları):** Bağlı olunan kazanın kadı mahkemesi sicillerindeki vefat/miras (**tereke**), nikâh, vasiyet ve arazi hüccetlerinden eşini, kızları dâhil tüm çocuklarını ve mal dökümünü verir. **Kritik İpucu (`Şuhûdü'l-Hâl`):** Hüccet ve terekelerin en altındaki **`شهود الحال` (*şuhûdü’l-hâl* — hal şahitleri)** listesini mutlaka okuyun; müstakil terekesi bulunamayan ataların bile komşu/akraba terekelerinde şahit olarak baba adı ve lakabıyla yer aldığı sıkça görülür!
5. **1600–1850 (`BOA, MAD.d..`, `D..BŞM.CZY.d`, `ML.VRD.CMH.d` & `A.{DVNSMHM.d...` — Avârız, Cizye, Mukataa ve Mühimme Defterleri):** Ayrıntılı *Avârız* hane sayımlarını (ör. 1642), gayrimüslim/mühtedi veya karma yerleşimler için *Cizye* defterlerini, aşiret/cemaat vergi listelerini ve padişah fermanlarını içerir.
6. **1450–1600 (`BOA, TT.d...` & `TK.GM.d...` — Tapu Tahrir Defterleri + Bölgesel Göç ve Boy/Cemaat Analizi):** Köyün en eski Osmanlı mufassal kaydını ve vergi mükellefi erkeklerin baba adlarıyla tam listesini verir. Bu aşamada **o bölgeye yapılan tarihsel göç ve iskân hareketlerini** (*konar-göçer Yörükân / Türkmen / Ekrâd / Tatar cemaat tahrirleri, sürgün ve şenlendirme kayıtları*) dikkatle inceleyerek bölgede yer alan potansiyel boy, oymak ve kavimleri belgesel kaynaklarıyla ele alın *(doğrudan hane kaydı ile bölgesel/etnik-tarihsel bağlamı birbirine karıştırmadan ayrı başlık ve kanıt seviyesiyle sunun)*.

### Bütçe ve Zaman Koruyan "Önce Fihrist" Kuralı (Zorunlu)
- Katalogda arama ücretsizdir; ancak e-Satış üzerinden filigransız yüksek çözünürlüklü her poz ücretlidir. 300–500 sayfalık bir defteri kontrolsüzce sepete ekletmeyin!
- Önce defterin başındaki **Fihrist (`Mi=1..5`)** pozlarını veya örnek sayfayı okuyarak:
  1. Defterin aranan kaza/nahiye ve döneme ait olduğunu doğrulayın.
  2. **Poz (`Mi`) ≠ Varak (`vr.`) Ofset Hesabını** yapın: Defter üzerindeki Osmanlıca varak/sayfa numarası ile dijital görüntü (`Mi`) numarası arasında kapak, boş sayfa veya mükerrer çekim kaynaklı sabit bir fark vardır. Köy başlığını (`Karye-i ... tâbi-i ...`) bizzat doğruladıktan sonra kullanıcıya **yalnızca ilgili 3–10 pozluk aralığı** indirtin.

---

## Adım 3: Kuşak Matematiği, Kanıt Seviyeleri ve Hata Denetimi

### 1. Kuşak Bağlama Matematiği
- **`+ΔYıl` Çapraz Sayım Eşleştirmesi:** İki sayım arasındaki yıl farkı (ör. `1834 → 1844 = +10 yıl`), aynı hanedeki baba, oğul ve kardeşlerin yaşlarına tutarlı biçimde (`±2–3` yıl taşra yuvarlama payıyla) yansımalıdır.
- **`1/N` Nadir İsim ve Yan Soy Filtresi:** Köydeki tüm haneleri tarayın; sadece düz üst soyu değil, **amcaları, kardeşleri, dede adını ilk toruna verme geleneğini ve sülale lakabını** çapraz doğrulayın.

### 2. Beşli Kanıt Seviyesi ve Anlatım Üslubu (Her Eşleşmede Açıkça Etiketleyin)
- **`[KESİN KANIT]`:** e-Devlet kütüğü, Esas Nüfus Defteri veya `isim + baba adı + lakap + köy + tutarlı yaş` bütünlüğüyle doğrudan kanıtlanan kayıt *(raporda düz kesin ifadeyle yazılır)*.
- **`[GÜÇLÜ EŞLEŞME]`:** Aynı köyde nadir isim, uyumlu yaş ve hane/kardeş dizilimiyle örtüşen, ara kütük teyidiyle kesinleşecek kayıt *(raporda "kayıtlar ... işaret etmektedir / büyük olasılıkla" üslubuyla yazılır)*.
- **`[İSİM / SÜLALE İZİ]`:** 16.–17. yüzyıl tahrir/avârız defterlerinde aynı köyde geçen aynı ad veya lakap *(doğrudan kan bağı kanıtı değil, köy içi tarihsel süreklilik izidir)*.
- **`[BÖLGESEL GÖÇ & CEMAAT BAĞLAMI]`:** 15.–18. yüzyıl tahrir ve mühimme kayıtlarında bölgede belgelenen aşiret/oymak/iskân hareketleri.
- **`[AİLE ANLATISI / SÖZLÜ TARİH]`:** Aile veya köy içinde kuşaktan kuşağa aktarılan ancak henüz birincil arşiv belgesiyle doğrulanmamış hikâyeler (ör. göç vapuru, sandık, göç sebebi) *(raporda daima "ailede anlatılana göre..." / "sözlü rivayete göre..." ihtiyat kalıbıyla yazılır)*.

### 3. En Sık Yapılan 5 Hata (Kaçınılması Zorunlu)
1. **Eş adlı köye aldanmak:** Sayfa başlığındaki `tâbi-i ...` (bağlı olduğu kaza/nahiye) kaydını ve komşu köy sırasını kontrol etmeden okuma yapmayın.
2. **Poz (`Mi`) ile Varak (`vr.`) numarasını karıştırmak:** Her defterde ofseti bizzat hesaplayın.
3. **Yaş tutarsızlığını görmezden gelmek:** Baba-oğul yaş farkını ve sayımlar arası `+ΔYıl` artışını mutlaka test edin.
4. **Filigranlı düşük çözünürlükte harf uydurmak:** Mavi filigran yazısının harf noktalarını örttüğü yerlerde filigransız asıl görüntüden [crop_and_verify.py](./scripts/crop_and_verify.py) ile 1:1 kesit alın.
5. **Yan soyu ve köy bütününü atlamak:** Köyün tamamını okumak, aynı sülalenin komşu hanelerdeki amcazade kollarını da ortaya çıkarır.

---

## Adım 4: Çıktı ve Sunum Düzeni

Bulguları kullanıcıya şu yapılandırılmış düzende sunun:

1. **Soy Kütüğü Sentezi (Baba ve Anne Tarafı Ayrı Ayrı):** Kuşak kuşak şema, Osmanlıca özgün yazılışlar (parantez içinde) ve her halkanın kanıt seviyesi (`[KESİN] / [GÜÇLÜ] / [İSİM İZİ]`).
2. **Köyün / Mahallenin Tarihçesi, Eski Adı ve İdari Evrimi:** 16. yüzyıldan günümüze idari bağlılık zinciri ve demografik/mali gelişim tablosu (her rakamın yılı, birimi ve birincil kaynağı belirtilerek).
3. **Köydeki Kurucu Ocaklar, Önemli Kişiler ve Tarihî Olaylar:** İmamlar, muhtarlar, sipahiler, vakıflar, göç/iskân, salgınlar, eşkıya/aşiret fermanları ve askerî/seferberlik (*Asâkir-i Mansûre, Redîf, Balkan, Çanakkale, İstiklâl Harbi*) kayıtları.
4. **Tam Arşiv Künyeleri ve Nokta Atışı İndirme Tablosu:** `Arşiv | Fon Kodu | Defter/Dosya-Gömlek | Hicrî/Rûmî & Milâdî Tarih | Varak & Poz (Mi) | İçerik Özeti`.
5. *(İsteğe Bağlı İleri Çıktılar)*: Kullanıcı talep ederse bulguları **Avrupa *Ortsgeschichte* tarzında çok bölümlü baskıya hazır HTML/PDF köy-aile kitabı** ve `scripts/soyagaci_ve_harita.py` ile **sıfır kurulumlu İnteraktif HTML Göç Haritası ve Kuşak Zaman Çizelgesi** olarak üretin.
