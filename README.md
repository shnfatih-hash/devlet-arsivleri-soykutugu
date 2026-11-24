# Devlet Arşivleri Soy Kütüğü ve Köy Tarihi Araştırma Becerisi (`devlet-arsivleri-soykutugu`)

> **e-Devlet Alt-Üst Soy Bilgisi** belgeniz belli bir tarihte kesiliyor mu?  
> Bu açık kaynaklı yapay zekâ becerisi (**Agent Skill**), şifrenizi hiçbir yere vermeden **T.C. Cumhurbaşkanlığı Devlet Arşivleri Başkanlığı Kataloğu** ve indirdiğiniz orijinal Osmanlıca el yazması defterler üzerinden **anne ve baba tarafı soy ağacınızı**, **köyünüzün eski adını ve tarihini** 1:1 piksel belge kesitleriyle **1500'lü yıllara kadar** kanıtlı biçimde indirmenizi sağlar.  
> *Bu çalışma, **Said Sürücü**'nün seminerinden hareketle hazırlanmış ve geliştirilmiştir; ufuk açıcı katkıları için kendisine içtenlikle teşekkür ederiz.*

---

## İçindekiler

1. [Neden e-Devlet Soy Ağacı Herkeste Farklı Bir Tarihte Kesilir? ("Kütük Duvarı")](#1-neden-e-devlet-soy-ağacı-herkeste-farklı-bir-tarihte-kesilir-kütük-duvarı)
2. [500 Yıllık Geriye Gidiş Merdiveni (2026 → 1500)](#2-500-yıllık-geriye-gidiş-merdiveni-2026--1500)
3. [Gerekli Resmi İnternet Siteleri, Portallar ve Program Adresleri](#3-gerekli-resmi-internet-siteleri-portallar-ve-program-adresleri)
4. [Kurulum: Skill Paketi ve Chrome DevTools MCP Ayarı](#4-kurulum-skill-paketi-ve-chrome-devtools-mcp-ayarı)
5. [Adım Adım Metodoloji: Arşivde Sıfır Hatayla Soy Sürme](#5-adım-adım-metodoloji-arşivde-sıfır-hatayla-soy-sürme)
   - [Adım 1: Arşive Girmeden Önce Çıkarılacak 4 Altın İpucu](#adım-1-arşive-girmeden-önce-çıkarılacak-4-altın-ipucu)
   - [Adım 2: Doğru Defter Serilerini Tanımak](#adım-2-doğru-defter-serilerini-tanımak)
   - [Adım 3: Bütçe ve Zaman Koruyan "Önce Fihrist Testi → Nokta Atışı İndirme" Taktiği](#adım-3-bütçe-ve-zaman-koruyan-önce-fihrist-testi--nokta-atışı-indirme-taktiği)
   - [Adım 4: 1:1 Piksel Kesitiyle Paleografik Okuma ve Kuşak Matematiği](#adım-4-11-piksel-kesitiyle-paleografik-okuma-ve-kuşak-matematiği)
   - [Adım 5: Kanıt Seviyeleri ve En Sık Yapılan 5 Hata](#adım-5-kanıt-seviyeleri-ve-en-sık-yapılan-5-hata)
6. [Defterde Karşılaşacağınız 15 Temel Osmanlıca Arşiv Kelimesi](#6-defterde-karşılaşacağınız-15-temel-osmanlıca-arşiv-kelimesi)
7. [Göçmen ve Mübadil Aileler İçin Rehber (Balkanlar, Adalar, Girit ve Kafkasya)](#7-göçmen-ve-mübadil-aileler-için-rehber-balkanlar-adalar-girit-ve-kafkasya)
8. [5 Adımda Hızlı Başlangıç ve Kopyala–Yapıştır Ana Prompt](#8-5-adımda-hızlı-başlangıç-ve-kopyalayapıştır-ana-prompt)
9. [Paket Yapısı, Teşekkür ve Lisans](#9-paket-yapısı-teşekkür-ve-lisans)

---

## 1. Neden e-Devlet Soy Ağacı Herkeste Farklı Bir Tarihte Kesilir? ("Kütük Duvarı")

e-Devlet'ten aldığınız *Alt-Üst Soy Bilgisi* belgesinin 1840'larda, 1880'lerde veya 1905'te aniden kesilmesi kayıtların yok olduğu anlamına **gelmez**. Bunun üç tarihsel nedeni vardır:

1. **Her bölgede farklı başlangıç yılı:** Modern nüfus kütüklerine dayanak olan Osmanlı *Sicill-i Nüfus Esas (Atîk) Defterleri* her vilayette aynı yıl tutulmadı. Kimi sancakta **1881–1883 (`R. 1297–1299`)**, kimi yerde **1904–1905 (`R. 1320`)** sayımı esas alındı; savaş, işgal veya hükümet konağı yangını yaşayan yerlerde ise kütükler daha geç yenilendi.
2. **İlk sayımdan önce vefat eden büyük dedeler:** Esas kütük yazılmadan önce vefat etmiş bir ata için kütükte müstakil satır açılmaz; adı yalnızca hayattaki çocuğunun **"Baba Adı"** sütununda asılı kalır.
3. **1934 öncesi lakaplar ve değişen köy adları:** *Soyadı Kanunu* (1934) öncesinde aileler **sülale lakaplarıyla** (`...oğulları`, `...zâde`, `...uşağı`), köyler ise **eski Osmanlıca adlarıyla** ve farklı idari birimlere (bugünkünden farklı kaza/nahiyelere) bağlı olarak kaydedildiğinden klasik metin aramasıyla iz sürmek zorlaşır.

> **İyi Haber:** 1500'lerden 1900'lerin başına uzanan milyonlarca sayfalık Osmanlı nüfus, temettuat, şer'iyye sicili, avârız ve tapu tahrir defteri **T.C. Cumhurbaşkanlığı Devlet Arşivleri**'nde dijital olarak durmaktadır!

---

## 2. 500 Yıllık Geriye Gidiş Merdiveni (2026 → 1500)

```text
  2026  ●  Bugün — e-Devlet Alt-Üst Soy Bilgisi PDF'i (Başlangıç noktası)
        │
  1905  ◉  Kütük Duvarı — Sicill-i Nüfus aile esas kütüklerinin başlangıcı (1881–1905)
        │
  1845  ●  Temettuat Defterleri (ML.VRD.TMT.d) — Hane reisinin mesleği, tarlası, hayvanları ve geliri
        │
  1831  ●  Nüfus & Yoklama Defterleri (NFS.d) — Boy/sakal eşkâlli erkek sayımları, doğum/ölüm/askerlik
        │
  1750  ●  Kadı (Şer'iyye) Sicilleri (MŞH.ŞSC.d) & Mühimme — Tereke (miras: eş ve kız çocukları dâhil!)
        │
  1642  ●  Avârız ve Mukataa Defterleri (MAD.d) — Vergi haneleri ve aşiret/cemaat listeleri
        │
  1500  ●  Tapu Tahrir Defterleri (TT.d / TK.GM.d) — Köyün ilk Osmanlı kaydı ve baba adlarıyla mükellefler
```

---

## 3. Gerekli Resmi İnternet Siteleri, Portallar ve Program Adresleri

### A. Resmi Arşiv ve Nüfus Portalları
| Kurum / Hizmet | Resmi İnternet Adresi | Ne İşe Yarar? |
| :--- | :--- | :--- |
| **e-Devlet — Alt-Üst Soy Bilgisi (NVİGM)** | https://www.turkiye.gov.tr/nvi-alt-ust-soy-bilgisi-sorgulama | Anne ve baba tarafı başlangıç soy ağacı PDF belgesini indirmenizi sağlar. |
| **e-Devlet — İsim Denklik Belgesi (NVİGM)** | https://www.turkiye.gov.tr/nvi-isim-denklik-belgesi-talep-ve-sorgulama | Balkanlar, Adalar ve Kafkasya'dan gelen göçmen/mübadil ataların eski kayıtlarını sorgular. |
| **Devlet Arşivleri Başkanlığı Kataloğu (DAB)** | https://katalog.devletarsivleri.gov.tr | e-Devlet ile **ücretsiz** girilen Osmanlı ve Cumhuriyet Arşivleri dijital belge arama sistemi. |
| **DAB — Basit & Detaylı Arama Ekranları** | https://katalog.devletarsivleri.gov.tr/Sayfalar/Arama/Arama.aspx <br/> https://katalog.devletarsivleri.gov.tr/Sayfalar/Arama/OzelArama.aspx | Anahtar kelime veya doğrudan Fon Kodu (`NFS.d`, `TT.d`, `MAD.d` vb.) ve defter numarasıyla arama ekranları. |
| **Devlet Arşivleri Başkanlığı Resmi Sitesi** | https://www.devletarsivleri.gov.tr | Arşiv rehberleri ve Osmanlı yer adları sözlükleri/yayınları. |
| **İSAM — Kadı (Şer'iyye) Sicilleri Arşivi** | https://kadisicilleri.org | Şer'iyye sicilleri katalogları ve yayımlanmış mahkeme/tereke defterleri. |
| **MSB — Şehit Bilgi Kapısı** | https://www.msb.gov.tr/SehitBilgiKapisi | Osmanlı-Rus, Balkan, Çanakkale, I. Dünya ve İstiklâl Harbi şehit künyeleri sorgulama kapısı. |
| **TTK — Tarih Çevirme Kılavuzu** | https://www.ttk.gov.tr/tarih-cevirme-kilavuzu/ | Hicrî, Rûmî ve Milâdî tarihler arasında gün/ay/yıl bazında tam dönüşüm aracı. |
| **TKGM & VGM Resmi Portalları** | https://www.tkgm.gov.tr • https://parselsorgu.tkgm.gov.tr • https://www.vgm.gov.tr | Kuyûd-ı Kadîme tapu kayıtları, eski mevki/parsel sorgusu ve köy cami/zaviye vakıf kayıtları. |

### B. Gerekli Programlar ve Yapay Zekâ / MCP Bileşenleri
| Yazılım / Paket | İndirme ve Dokümantasyon Adresi | Görevi |
| :--- | :--- | :--- |
| **Google Antigravity** | https://antigravity.google | Bu beceriyi (`SKILL.md`) çalıştıran, tarayıcıya bağlanan ve 1:1 belge kesitlerini okuyan ajan ortamı. *(Claude Code, Cursor ve Codex ile de uyumludur.)* |
| **Google Chrome** | https://www.google.com/chrome/ | Devlet Arşivleri oturumunuzu açacağınız tarayıcı. Uzak bağlantı ayarı: `chrome://inspect/#remote-debugging` |
| **Node.js (LTS)** | https://nodejs.org | `npx` üzerinden Chrome DevTools MCP sunucusunu çalıştırmak için gereklidir. |
| **Chrome DevTools MCP** | https://github.com/ChromeDevTools/chrome-devtools-mcp <br/> https://www.npmjs.com/package/chrome-devtools-mcp | Yapay zekânın şifrenizi görmeden açık Chrome sekmenizde katalog araması yapmasını sağlayan resmi MCP köprüsü. |
| **Python 3 + Pillow** | https://www.python.org (`pip install Pillow`) | İndirdiğiniz `.zip / .jpg` arşiv sayfalarını sağ/sol varaklara bölen ve 1:1 piksel kesiti alan `scripts/crop_and_verify.py` betiği için gereklidir. |

---

## 4. Kurulum: Skill Paketi ve Chrome DevTools MCP Ayarı

### A. Skill Paketini Tek Komutla Kurma

Terminalinizi (Windows'ta **PowerShell**, macOS/Linux'ta **Terminal**) açıp kullandığınız yapay zekâ aracına göre aşağıdaki tek satırlık komutu çalıştırın:

**1. Google Antigravity (Tüm projelerde geçerli genel kurulum — Önerilen):**
```powershell
# Windows (PowerShell)
git clone https://github.com/shnfatih-hash/devlet-arsivleri-soykutugu.git "$HOME\.gemini\config\skills\devlet-arsivleri-soykutugu"
```
```bash
# macOS / Linux
git clone https://github.com/shnfatih-hash/devlet-arsivleri-soykutugu.git ~/.gemini/config/skills/devlet-arsivleri-soykutugu
```

**2. Proje Bazlı Kurulum (Sadece açık olan çalışma klasörü için):**
```bash
git clone https://github.com/shnfatih-hash/devlet-arsivleri-soykutugu.git .agents/skills/devlet-arsivleri-soykutugu
```

**3. Claude Code veya Codex Kurulumu:**
```bash
git clone https://github.com/shnfatih-hash/devlet-arsivleri-soykutugu.git ~/.claude/skills/devlet-arsivleri-soykutugu
```

**Python Görüntü Kesit Kütüphanesini Yükleme:**
```bash
pip install Pillow
```

### B. Chrome DevTools MCP Bağlantısı (Canlı Katalog Taraması İçin)

1. Antigravity MCP yapılandırma dosyanıza (`~/.gemini/config/mcp_config.json`) şu bloğu ekleyin (veya eklenti yöneticisinden resmi **Chrome DevTools** eklentisini etkinleştirin):
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
2. Google Chrome'da yeni bir sekme açıp adres çubuğuna **`chrome://inspect/#remote-debugging`** yazarak Enter'a basın ve **"Enable remote debugging"** kutucuğunu işaretleyin.
3. Yeni bir sekmede **`https://katalog.devletarsivleri.gov.tr`** adresini açıp **"e-Devlet ile Giriş"** butonundan bizzat giriş yapın. *(Şifreniz ve T.C. Kimlik Numaranız hiçbir aşamada yapay zekâya verilmez!)*

---

## 5. Adım Adım Metodoloji: Arşivde Sıfır Hatayla Soy Sürme

### Adım 1: Arşive Girmeden Önce Çıkarılacak 4 Altın İpucu
Milyonlarca belge içinde doğru defteri bulmak için işe şu 4 bilgiyi netleştirerek başlıyoruz:
1. **Köyün / Mahallenin Eski Adı:** Cumhuriyet döneminde pek çok yerleşimin adı Türkçeleştirildi veya değiştirildi. Arşivde arama daima **Osmanlıca eski adla** ve harf varyantlarıyla (`k/g`, `t/d`, `b/p`, `c/ç`) yapılır.
2. **Eski Sülale Lakapları ve Oymak Adları:** 1934 öncesi aileler `"…oğulları"`, `"…zâde"`, `"…uşağı"` gibi lakaplarla yazılırdı.
3. **Kütükteki En Eski Ataların Adı ve Doğum Yılları:** Alt-Üst Soy PDF'inizdeki en dip satırlar ve bu kişilerin "Baba Adı" sütunundaki isimler.
4. **Osmanlı İdari Birimi (`Sancak / Kazâ / Nâhiye`):** Defterler bugünkü ilçelere göre değil, dönemin idari sınırlarına göre tutulmuştur (bugün A ilçesine bağlı bir köy, 1840'ta komşu B nahiyesinin defterinde olabilir!).

### Adım 2: Doğru Defter Serilerini Tanımak
- **`NFS.d` (Nüfus Defterleri, 1830–1880'ler):** Köydeki tüm erkekleri hane hane, baba adıyla, yaşıyla (`sinn`), hatta **boy ve sakal/bıyık eşkâliyle** yazar; doğum, ölüm ve askerlik şerhlerini düşer.
- **`MŞH.ŞSC.d` (Şer'iyye / Kadı Sicilleri):** Vefat eden ataların miras taksimini (**tereke**) içerir; eşini, oğullarını ve nüfus defterlerinde yer almayan **kız çocuklarını** tek tek sayar.
- **`ML.VRD.TMT.d` & `MAD.d` (Temettuat ve Maliyeden Müdevver, 1600–1845):** 1844–1845 mal-mülk/gelir sayımlarını, 17. yüzyıl avârız vergi hanelerini ve aşiret/maden yükümlülüklerini barındırır.
- **`TT.d` & `TK.GM.d` / `A.{DVNSMHM.d` / `MVL` (1500'ler →):** 500 yıllık mufassal köy tahrirlerini, padişah mühimme fermanlarını ve Meclis-i Vâlâ davalarını içerir.

### Adım 3: Bütçe ve Zaman Koruyan "Önce Fihrist Testi → Nokta Atışı İndirme" Taktiği
- **Ücret Gerçeği:** Devlet Arşivleri Kataloğu'nda arama yapmak ücretsizdir; ancak filigransız yüksek çözünürlüklü her görüntü (poz) e-Satış sepetinden poz başı ücretle (ör. güncel tarifede poz başı cüzi bir bedelle) satın alınır. 300–500 sayfalık yanlış bir defteri toptan satın almak hem bütçeyi hem emeği boşa harcar!
- **1. Aşama (Fihrist Testi):** Defterin tamamını almadan önce sadece başındaki **Fihrist (`Mi=1..5`)** sayfalarını kontrol ettirin. Yapay zekâ fihristi ve tarihleri okuyarak yanlış dönem veya yanlış nahiyeye ait defterleri eler; doğru defterde ise **Poz (`Mi`) ≠ Varak (`vr.`)** kayma farkını hesaplayıp *"Aradığın köy Poz 33 ile 37 arasında!"* diyerek tam aralığı verir.
- **2. Aşama (Nokta Atışı İndirme):** Sadece köyünüzün bulunduğu 3–10 pozu satın alıp `.zip / .jpg` olarak bilgisayarınızdaki çalışma klasörüne indirin.

### Adım 4: 1:1 Piksel Kesitiyle Paleografik Okuma ve Kuşak Matematiği
Sıradan sohbet botları Osmanlıca el yazması sayfaya uzaktan bakıp harfleri tahmin eder; köy ve şahıs adlarını uydurabilir. Bu beceri ise `scripts/crop_and_verify.py` aracılığıyla:
1. İndirdiğiniz 3000 piksellik filigransız sayfaları Sağ (`R`) ve Sol (`L`) varaklara böler,
2. Her kritik satırdan **1:1 doğal piksel yakınlaştırma kesiti (crop)** alarak harf noktalarını kanıtlı okur,
3. **`+ΔYıl` Çapraz Sayım Matematiği** uygular (örneğin 1834 sayımında 4 yaşında yazılan çocuk, 6 yıl sonraki 1840 sayımında aynı babanın yanında ~10 yaşında, 1844 sayımında ~14 yaşında görünmelidir),
4. **`1/N` Nadir İsim ve Yan Soy Filtresi** ile sadece düz üst soyu değil; amcaları, kardeşleri, dede adını ilk toruna verme geleneğini ve lakapları çapraz doğrular *(Unutmayın: Bir kadının soyadı veya lakabı babasından değil, eşinin hanesinden veya dul kaldığında kendi adından gelebilir!)*.

### Adım 5: Kanıt Seviyeleri ve En Sık Yapılan 5 Hata

Her eşleşme aynı kesinlikte değildir; bu beceri her bulguyu üç kanıt seviyesinden biriyle işaretler:
- 🟢 **`[KESİN KANIT]`:** e-Devlet kütüğü, Esas Nüfus Defteri veya `isim + baba adı + lakap + köy + tutarlı yaş` zinciriyle doğrudan belgelenen kayıt.
- 🟡 **`[GÜÇLÜ EŞLEŞME]`:** Aynı köy, nadir isim, uyumlu yaş ve kardeş dizilimi bir arada bulunan güçlü aday.
- ⚪ **`[İSİM / SÜLALE İZİ]`:** Başka bir yüzyılda (ör. 1584 tahririnde) aynı köyde geçen aynı isim veya lakap; doğrudan kan bağı kanıtı sayılmaz, tarihsel süreklilik izi olarak belirtilir.

**En Sık Yapılan 5 Hata:**
1. *Benzer köy adına aldanmak* → Sayfa başlığındaki `tâbi-i ...` (bağlı olduğu kaza/nahiye) ibaresini ve komşu köyleri mutlaka doğrulayın.
2. *Yaş tutarsızlığını görmezden gelmek* → İki sayım arasındaki yıl farkı yaşlara yansımalıdır.
3. *Dijital Poz (`Mi`) ile Osmanlıca Varak (`vr.`) numarasını karıştırmak* → Kapak ve boş sayfalar yüzünden arada sabit fark bulunur.
4. *Filigranlı düşük çözünürlüklü okumaya körü körüne güvenmek* → Kritik satırları filigransız aslından 1:1 kesitle kontrol edin.
5. *Hızlı paralel bot istekleriyle arşiv sitesini yormak* → `BelgeGoster` üzerinde çoklu paralel istek güvenlik engelini (`HTTP 418`) tetikler; daima sakin ve sıralı ilerleyin.

---

## 6. Defterde Karşılaşacağınız 15 Temel Osmanlıca Arşiv Kelimesi

| Terim | Osmanlıca | Anlamı |
| :--- | :---: | :--- |
| **bin / ibn • veled-i** | `بن / ولد` | Oğlu (*Ahmed bin Mehmed* / *Ahmed veled-i Mehmed* = Mehmed oğlu Ahmed) |
| **bint / binti** | `بنت` | Kızı (*Ayşe binti Ali* = Ali kızı Ayşe — özellikle kadı sicillerinde) |
| **hâne** | `خانه` | Ev, aile ve vergi birimi |
| **nefer / neferân** | `نفر / نفران` | Kayıtlı erkek kişi / kişiler |
| **sinn** *(ve **sene**)* | `سن` *(ve `سنه`)* | **`sinn` = Yaş** (`سن ٤٠` = 40 yaşında); **`sene` = Yıl** (`سنه ٢٥٦` = [1]256 yılı) |
| **karye • mezra'a** | `قريه • مزرعه` | Köy • Ekili arazi / küçük geçici yerleşim |
| **tâbi-i** | `تابع` | İdari olarak bağlı olduğu nahiye veya kaza |
| **oğlu • zâde • uşağı** | `اوغلى • زاده` | Sülale, aile veya oymak topluluğu |
| **muhtâr-ı evvel / sânî** | `مختار اول / ثانى` | Köyün birinci ve ikinci muhtarı (`kethüdâ` = köy/aşiret kâhyası) |
| **mücerred • bennâk** | `مجرد • بناك` | Bekâr yetişkin erkek • Evli vergi mükellefi köylü |
| **şâb / şâb-ı emred** | `شاب امرد` | Bıyığı yeni terlemiş, henüz sakalı çıkmamış genç delikanlı |
| **tevellüd • fevt** | `تولد • فوت` | Doğdu • Vefat etti (yoklama defterlerinde kırmızı mürekkeple yazılır) |
| **reft be-askeriyye • redîf** | `رفت بعسكريه • رديف` | Nizamiye ordusuna gitti • Taşra ihtiyat (yedek) taburu askeri |
| **varak (`vr.`)** | `ورق` | Defter yaprak numarası (`a` = sağ ön yüz, `b` = sol arka yüz) |
| **Eşkâl Sıfatları** | `اورته / اوزون بويلو` | *orta boylu, uzun boylu, kara sakallı, kır sakallı, ak sakallı, köse, ter bıyıklı* |

---

## 7. Göçmen ve Mübadil Aileler İçin Rehber (Balkanlar, Adalar, Girit ve Kafkasya)

Ataları Anadolu dışından göç etmiş aileler için ayrıntılı kılavuz [`references/gocmen-ve-mubadil-rehberi.md`](./references/gocmen-ve-mubadil-rehberi.md) dosyasındadır. Özet yol haritası:

1. **1923–1925 Lozan Mübadilleri** (*Selanik, Drama, Kavala, Serez, Girit, Yanya, Kayalar, Midilli vb.*):  
   Cumhuriyet Arşivi **`130-16-13-2`** (*Muhtelit Mübadele Tasfiye Talepnameleri*) ve **`272`** (*Toprak İskân*) fonlarında aile reisinin adıyla arama yapın; geldikleri köy, aile fertleri ve bıraktıkları mallar tek tek yazar!
2. **93 Harbi (1877), Balkan Harbi (1912) ve Kafkasya/Kırım Muhacirleri** (*Bulgaristan, Üsküp, Manastır, Bosna, Çerkes, Çeçen, Abaza, Kırım, Ahıska*):  
   Osmanlı Arşivi **`DH.SN..THR.`**, **`DH.İ.UM`**, **`DH.MKT.`**, **`Y..PRK.KOM.`** ve **`A.}MKT.NZD.`** fonlarında *"Aile reisi + yerleştirildiği ilçe/köy"* ile Muhacir Kâğıdı ve İskân Kaydı aratın.
3. **Büyük Arşiv Sürprizi:**  
   *Tuna (Bulgaristan), Selanik, Manastır, Yanya, Filibe, Varna, Üsküp, Gümülcine, Midilli* gibi pek çok Balkan ve Adalar sancağının **1830–1875 Osmanlı Nüfus Defterleri (`NFS.d`)** Türkiye'deki Osmanlı Arşivi'ndedir! İsim Denklik Belgesi veya Tasfiye Talepnamesi ile eski köyünüzü öğrendikten sonra 1840 Balkan nüfus defterinizi de bu beceriyle okutabilirsiniz.

---

## 8. 5 Adımda Hızlı Başlangıç ve Kopyala–Yapıştır Ana Prompt

1. **Belgeni İndir:** [e-Devlet Alt-Üst Soy Bilgisi](https://www.turkiye.gov.tr/nvi-alt-ust-soy-bilgisi-sorgulama) PDF'inden en eski atalarını, doğum yıllarını ve köyünün eski adını çıkar (göçmensen [İsim Denklik Belgesi](https://www.turkiye.gov.tr/nvi-isim-denklik-belgesi-talep-ve-sorgulama) ve iskân yerini not et).
2. **Kataloğa Gir:** Chrome'da `chrome://inspect/#remote-debugging` ayarını aç ve [katalog.devletarsivleri.gov.tr](https://katalog.devletarsivleri.gov.tr) adresine e-Devlet ile ücretsiz giriş yap.
3. **Önce Fihristi Kontrol Ettir:** Tüm defteri hemen satın alma! Önce fihrist veya ilk 5–10 pozu Antigravity'ye kontrol ettirip doğru defter ve varak aralığını buldur.
4. **Nokta Atışı İndir:** Sadece köyünün bulunduğu doğru sayfa aralığını e-Satış'tan indirip `.zip / .jpg` olarak bir klasöre koy.
5. **1:1 Kanıtlı Okut:** Klasörü Google Antigravity'de aç ve aşağıdaki komutu gönder *(diğer senaryo şablonları için bkz. [`examples/ornek-kullanim-promptlari.md`](./examples/ornek-kullanim-promptlari.md))*:

```markdown
Sana e-Devlet "Alt-Üst Soy Bilgisi" belgemi ve (varsa) Devlet Arşivleri'nden indirdiğim `.zip / .jpg` dosyalarını verdim; Chrome'da `https://katalog.devletarsivleri.gov.tr` oturumum da açık.

Lütfen `devlet-arsivleri-soykutugu` becerisini etkinleştirerek tahmin yürütmeden, her kritik hane ve şerh satırını 1:1 piksel belge kesitiyle doğrulayarak anne ve baba tarafı üst soyumu, kardeş/amca yan kollarını, köyümüzün eski adını, idari evrimini ve tarihî olaylarını kanıt seviyeleriyle (`[KESİN] / [GÜÇLÜ] / [İSİM İZİ]`) çıkar.
```

---

## 9. Paket Yapısı, Teşekkür ve Lisans

```text
devlet-arsivleri-soykutugu/
├── SKILL.md                                         # Yapay zekâ ajanları için ana beceri yönergesi
├── README.md                                        # Kurulum, metodoloji, resmi linkler ve kullanım kılavuzu
├── LICENSE                                          # MIT Açık Kaynak Lisansı
├── references/
│   ├── fon-kodlari-ve-paleografya-rehberi.md        # 1500–1925 fon kodları, takvim hesabı, harf varyantları & sözlük
│   └── gocmen-ve-mubadil-rehberi.md                 # Balkanlar, Adalar, Girit ve Kafkasya göçmen/mübadil kılavuzu
├── scripts/
│   ├── dab_helpers.js                               # Chrome DevTools MCP sıralı/WAF korumalı arama ve varak yardımcıları
│   ├── crop_and_verify.py                           # .zip/.jpg defterlerden varak bölme ve 1:1 piksel kesit alma aracı
│   └── tarih_cevirici.py                            # 3 yönlü Hicrî ↔ Rûmî ↔ Milâdî kesin tarih çevirici (TTK bağlantılı)
└── examples/
    └── ornek-kullanim-promptlari.md                 # 4 farklı senaryo için hazır kopyala-yapıştır istem şablonları
```

### Kardeş Proje (Osmanlıca Resmî Evraklar İçin)

Ferman, Berat, İrade-i Seniyye, Tahrirat, Mazbata, Arz-ı Hâl, Hüccet ve Telgrafname gibi resmî belgeleri üniversitelerde geçerli **TDV İA / TTK transkripsiyon sistemi**, şerh (kritik aparat), kelime/tamlama çözümlemeli interaktif HTML ve Kubbealtı/TDV İslâm Ansiklopedisi atıflarıyla okumak için kardeş beceriye göz atın: **[`shnfatih-hash/osmanlica-resmi-evrak`](https://github.com/shnfatih-hash/osmanlica-resmi-evrak)**

### Teşekkür ve İlham Kaynağı

Bu beceri paketi ve araştırma metodolojisi, **Said Sürücü**'nün seminerinden hareketle hazırlanmış ve geliştirilmiştir. Yapay zekâ destekli arşiv ve soy kütüğü araştırmalarına ilham veren kıymetli paylaşımı ve rehberliği için **Said Sürücü**'ye gönülden teşekkür ederiz.

### ♥ Projeye Gönüllü Destek

Bu proje tamamen ücretsiz ve açık kaynaklıdır; herkesin özgürce kullanımına açık kalacaktır. Çalışmayı faydalı bulduysanız ve yeni Osmanlı arşivi / dijital beşerî bilimler AI Skill'lerinin geliştirilmesine gönüllü olarak katkıda bulunmak isterseniz bir kahve ısmarlayarak veya GitHub Sponsors üzerinden destek olabilirsiniz:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Bir%20Kahve%20Ismarla-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/shnfatih8)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Projeye%20Destek%20Ol-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/shnfatih-hash)

### Lisans

Bu proje **MIT Lisansı** ile herkesin özgürce kullanımına, geliştirmesine ve paylaşımına sunulmuştur.
