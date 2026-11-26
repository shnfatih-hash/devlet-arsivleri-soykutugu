---
title: Devlet Arşivleri Soy Kütüğü & Köy Tarihi AI Skill
emoji: 📜
colorFrom: yellow
colorTo: blue
sdk: static
pinned: true
license: mit
short_description: 1500'lere kadar 1:1 kanıtlı Osmanlı soy kütüğü AI aracı
---

# Devlet Arşivleri Soy Kütüğü ve Köy Tarihi Araştırma Becerisi (`devlet-arsivleri-soykutugu`)

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Bir%20Kahve%20Ismarla-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/shnfatih8)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Projeye%20Destek%20Ol-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/shnfatih-hash)
[![Hugging Face Space](https://img.shields.io/badge/🤗%20Hugging%20Face-Canlı%20Web%20Aracı-FFD21E?style=for-the-badge)](https://huggingface.co/spaces/sahanfatih/devlet-arsivleri-soykutugu)
[![GitHub Repo](https://img.shields.io/badge/GitHub-shnfatih--hash%2Fdevlet--arsivleri--soykutugu-181717?style=for-the-badge&logo=github)](https://github.com/shnfatih-hash/devlet-arsivleri-soykutugu)

> **e-Devlet Alt-Üst Soy Bilgisi** belgeniz belli bir tarihte kesiliyor mu?  
> Bu açık kaynaklı yapay zekâ becerisi (**Agent Skill** + **Canlı Web Aracı**), şifrenizi hiçbir yere vermeden **T.C. Cumhurbaşkanlığı Devlet Arşivleri Başkanlığı Kataloğu** ve indirdiğiniz orijinal Osmanlıca el yazması defterler üzerinden **anne ve baba tarafı soy ağacınızı**, **köyünüzün eski adını, bölgesel göç/iskân geçmişini ve tarihini** 1:1 piksel belge kesitleriyle **1500'lü yıllara kadar** kanıtlı biçimde indirmenizi sağlar.  
> *Bu çalışma, **Said Sürücü**'nün seminerinden hareketle hazırlanmış ve topluluk geri bildirimleriyle geliştirilmiştir; ufuk açıcı katkıları için kendisine ve deneyimleriyle katkı sunan tüm araştırmacılara içtenlikle teşekkür ederiz.*

---

## İçindekiler

1. [Neden e-Devlet Soy Ağacı Herkeste Farklı Bir Tarihte Kesilir? ("Kütük Duvarı")](#1-neden-e-devlet-soy-ağacı-herkeste-farklı-bir-tarihte-kesilir-kütük-duvarı)
2. [500 Yıllık Geriye Gidiş Merdiveni (2026 → 1500)](#2-500-yıllık-geriye-gidiş-merdiveni-2026--1500)
3. [Gerekli Resmi İnternet Siteleri, Portallar ve Program Adresleri](#3-gerekli-resmi-internet-siteleri-portallar-ve-program-adresleri)
4. [Kurulum, Proje Klasörü Düzeni ve Chrome DevTools MCP Ayarı](#4-kurulum-proje-klasörü-düzeni-ve-chrome-devtools-mcp-ayarı)
5. [⚠️ Sık Karşılaşılan Hata: "Web Sayfasına Erişim Engellendi" Ekranı ve Kesin Çözümü](#5-️-sık-karşılaşılan-hata-web-sayfasına-erişim-engellendi-ekranı-ve-kesin-çözümü)
6. [Adım Adım Metodoloji: Arşivde Sıfır Hatayla Soy Sürme](#6-adım-adım-metodoloji-arşivde-sıfır-hatayla-soy-sürme)
7. [Defterde Karşılaşacağınız 15 Temel Osmanlıca Arşiv Kelimesi](#7-defterde-karşılaşacağınız-15-temel-osmanlıca-arşiv-kelimesi)
8. [Göçmen ve Mübadil Aileler İçin Rehber (Balkanlar, Adalar, Girit ve Kafkasya)](#8-göçmen-ve-mübadil-aileler-için-rehber-balkanlar-adalar-girit-ve-kafkasya)
9. [Çok Sayfalı Defter ve El Yazmalarını 10 Paralel Alt-Ajan ile Okutma / Tercüme](#9-çok-sayfalı-defter-ve-el-yazmalarını-10-paralel-alt-ajan-ile-okutma--tercüme)
10. [5 Adımda Hızlı Başlangıç ve Kopyala–Yapıştır Ana Prompt](#10-5-adımda-hızlı-başlangıç-ve-kopyalayapıştır-ana-prompt)
11. [Paket Yapısı, Kardeş Projeler, Gönüllü Destek ve Lisans](#11-paket-yapısı-kardeş-projeler-gönüllü-destek-ve-lisans)

---

## 1. Neden e-Devlet Soy Ağacı Herkeste Farklı Bir Tarihte Kesilir? ("Kütük Duvarı")

e-Devlet'ten aldığınız *Alt-Üst Soy Bilgisi* belgesinin (veya **İl/İlçe Nüfus Müdürlüğü**'nden aldığınız kayıt örneğinin) 1840'larda, 1880'lerde veya 1905'te aniden kesilmesi kayıtların yok olduğu anlamına **gelmez**. Bunun üç tarihsel nedeni vardır:

1. **Her bölgede farklı başlangıç yılı:** Modern nüfus kütüklerine dayanak olan Osmanlı *Sicill-i Nüfus Esas (Atîk) Defterleri* her vilayette aynı yıl tutulmadı. Kimi sancakta **1881–1883 (`R. 1297–1299`)**, kimi yerde **1904–1905 (`R. 1320`)** sayımı esas alındı; savaş, işgal veya hükümet konağı yangını yaşayan yerlerde ise kütükler daha geç yenilendi.
2. **İlk sayımdan önce vefat eden büyük dedeler:** Esas kütük yazılmadan önce vefat etmiş bir ata için kütükte müstakil satır açılmaz; adı yalnızca hayattaki çocuğunun **"Baba Adı"** sütununda asılı kalır.
3. **1934 öncesi lakaplar ve değişen köy adları:** *Soyadı Kanunu* (1934) öncesinde aileler **sülale lakaplarıyla** (`...oğulları`, `...zâde`, `...uşağı`), köyler ise **eski Osmanlıca adlarıyla** ve farklı idari birimlere (bugünkünden farklı kaza/nahiyelere) bağlı olarak kaydedildiğinden klasik metin aramasıyla iz sürmek zorlaşır.

> **İyi Haber:** 1500'lerden 1900'lerin başına uzanan milyonlarca sayfalık Osmanlı nüfus, temettuat, şer'iyye sicili, avârız/cizye ve tapu tahrir defteri **T.C. Cumhurbaşkanlığı Devlet Arşivleri**'nde dijital olarak durmaktadır!

---

## 2. 500 Yıllık Geriye Gidiş Merdiveni (2026 → 1500)

```text
  2026  ●  Bugün — e-Devlet Alt-Üst Soy PDF'i veya Nüfus Müdürlüğü Kayıt Örneği
        │
  1905  ◉  Kütük Duvarı — Sicill-i Nüfus aile esas kütüklerinin başlangıcı (1881–1905)
        │
  1845  ●  Temettuat Defterleri (ML.VRD.TMT.d) — Hane reisinin lakabı, mesleği, tarlası ve geliri
        │
  1831  ●  Nüfus & Yoklama Defterleri (NFS.d) — Boy/sakal eşkâlli erkek sayımları, doğum/ölüm/askerlik
        │
  1750  ●  Kadı (Şer'iyye) Sicilleri (MŞH.ŞSC.d) — Mahkeme ve Tereke (miras: eş ve kız çocukları dâhil!)
        │
  1642  ●  Avârız ve Cizye Defterleri (MAD.d / D..BŞM.CZY.d) — Vergi haneleri, cemaat ve aşiret listeleri
        │
  1500  ●  Tapu Tahrir Defterleri (TT.d / TK.GM.d) — Köyün ilk kaydı, mükellefler ve bölgesel göç/boy izleri
```

---

## 3. Gerekli Resmi İnternet Siteleri, Portallar ve Program Adresleri

### A. Resmi Arşiv ve Nüfus Portalları
| Kurum / Hizmet | Resmi İnternet Adresi | Ne İşe Yarar? |
| :--- | :--- | :--- |
| **e-Devlet — Alt-Üst Soy Bilgisi (NVİGM)** | https://www.turkiye.gov.tr/nvi-alt-ust-soy-bilgisi-sorgulama | Anne ve baba tarafı başlangıç soy ağacı PDF belgesini indirmenizi sağlar *(alternatif olarak İl/İlçe Nüfus Müdürlüğü'nden nüfus bilgisi istenebilir)*. |
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
| **Google Antigravity** | https://antigravity.google | Bu beceriyi (`SKILL.md`) çalıştıran, Chrome MCP'ye bağlanan ve 1:1 belge kesitlerini okuyan ajan ortamı. *(Claude Code, Cursor ve Codex ile de uyumludur.)* |
| **Google Chrome (Normal Masaüstü Tarayıcı)** | https://www.google.com/chrome/ | Devlet Arşivleri oturumunuzu açacağınız tarayıcı. Uzak bağlantı ayarı: `chrome://inspect/#remote-debugging` |
| **Node.js (LTS)** | https://nodejs.org | `npx` üzerinden Chrome DevTools MCP sunucusunu çalıştırmak için gereklidir. |
| **Chrome DevTools MCP** | https://github.com/ChromeDevTools/chrome-devtools-mcp <br/> https://www.npmjs.com/package/chrome-devtools-mcp | Yapay zekânın şifrenizi görmeden açık Chrome sekmenizde katalog araması yapmasını sağlayan resmi MCP köprüsü. |
| **Python 3 + Pillow** | https://www.python.org (`pip install Pillow`) | İndirdiğiniz `.zip / .jpg` arşiv sayfalarını sağ/sol varaklara bölen ve 1:1 piksel kesiti alan `scripts/crop_and_verify.py` betiği için gereklidir. |

---

## 4. Kurulum, Proje Klasörü Düzeni ve Chrome DevTools MCP Ayarı

### A. İlk Adım: Bilgisayarınızda Özel Bir Proje Klasörü Açın (`Önemli!`)

Belgelerin, 1:1 piksel kesitlerinin ve oluşturulan Word/HTML soyağacı raporlarının tek bir yerde düzenli toplanması için:
1. Masaüstünüzde veya Belgelerim'de yeni bir klasör oluşturun (ör. **`Soy_Kutugu_Arastirmam`**).
2. e-Devlet'ten indirdiğiniz *Alt-Üst Soy Bilgisi* PDF dosyanızı (ve varsa daha önce indirdiğiniz arşiv `.zip / .jpg` dosyalarını) bu klasörün içine atın.
3. **Google Antigravity**'yi açıp sol menüden **`Open Folder` / Yeni Proje** diyerek bu klasörü seçin.
4. Araştırma sırasında Antigravity sizden yardımcı paket kurma (`Pillow`), piksel kesiti alma veya Word/HTML rapor dosyası oluşturma izni istediğinde (**`Yes, allow` / `Submit`**) onay verin ki tüm belgeleri klasörünüze kaydedebilsin.

### B. Skill Paketini Tek Komutla Kurma

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

### C. Chrome DevTools MCP Bağlantısı (Canlı Katalog Taraması İçin)

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
2. Bilgisayarınızdaki **normal Google Chrome** tarayıcısında yeni bir sekme açıp adres çubuğuna **`chrome://inspect/#remote-debugging`** yazarak Enter'a basın ve **"Enable remote debugging"** kutucuğunu işaretleyin.
3. Yine **normal Google Chrome**'da yeni bir sekmede **`https://katalog.devletarsivleri.gov.tr`** adresini açıp **"e-Devlet ile Giriş"** butonundan bizzat giriş yapın. *(Şifreniz ve T.C. Kimlik Numaranız hiçbir aşamada yapay zekâya verilmez!)*

---

## 5. ⚠️ Sık Karşılaşılan Hata: "Web Sayfasına Erişim Engellendi" Ekranı ve Kesin Çözümü

Bazı kullanıcılarımız Antigravity'ye *"Devlet Arşivleri'ne gir"* dediğinde sağ panelde şu kırmızı uyarı ekranıyla karşılaşmaktadır:

> **❗ T.C. Cumhurbaşkanlığı Devlet Arşivleri Başkanlığı — Web Sayfasına Erişim Engellendi**  
> *Erişmeye çalıştığınız web sayfası, kurum politikaları doğrultusunda engellenmiştir.*

### Bu Hata Neden Çıkar?
Bu ekran, Antigravity'nin **kendi içindeki yerleşik tarayıcısı (*built-in browser*)** açıldığında ortaya çıkar. Devlet Arşivleri güvenlik duvarı, gömülü uygulama içi tarayıcıları bot/kurum dışı istemci sayarak otomatik engeller.

### 3 Adımda Kesin Çözüm (Nasıl Aşılır?)
1. **Dahili Tarayıcıyı Kapatın:** Antigravity penceresinin sağ tarafında açılan gömülü tarayıcı sekmesini kapatın.
2. **Normal Google Chrome'dan Giriş Yapın:** Bilgisayarınızda her zaman kullandığınız **normal Google Chrome** tarayıcısını açın:
   - Bir sekmede `chrome://inspect/#remote-debugging` adresine gidip **`Enable remote debugging`** kutusunu işaretleyin.
   - Diğer sekmede `https://katalog.devletarsivleri.gov.tr` adresine normal e-Devlet şifrenizle giriş yapın (normal Chrome'da hiçbir engel çıkmaz).
3. **Antigravity'ye Chrome MCP ile Bağlanmasını Söyleyin:** Sohbet kutusuna şu net cümleyi yazın:
   > *"Antigravity'nin kendi dahili tarayıcısını AÇMA; doğrudan **Chrome DevTools MCP** üzerinden bilgisayarımda açık olan normal Google Chrome sekmeme bağlanarak devam et."*

💡 **Hiç MCP Kurmadan Devam Etme Alternatifi (Sıfır Ayar):** Eğer Chrome MCP ayarıyla uğraşmak istemezseniz, normal Chrome tarayıcınızdan Devlet Arşivleri'ne kendiniz girip köyünüzün defter pozlarını `.zip` veya `.jpg` olarak proje klasörünüze indirin ve Antigravity'ye sadece *"Klasöre indirdiğim arşiv belgelerini `devlet-arsivleri-soykutugu` ile 1:1 kesit alarak oku"* deyin!

---

## 6. Adım Adım Metodoloji: Arşivde Sıfır Hatayla Soy Sürme

### Adım 1: Arşive Girmeden Önce Çıkarılacak 4 Altın İpucu
Milyonlarca belge içinde doğru defteri bulmak için işe e-Devlet *Alt-Üst Soy Bilgisi* belgenizden (veya **İl/İlçe Nüfus Müdürlüğü**'nden alınan nüfus kayıt bilgisinden) şu 4 ipucunu netleştirerek başlıyoruz:
1. **Köyün / Mahallenin Eski Adı:** Cumhuriyet döneminde pek çok yerleşimin adı değiştirildi. Arşivde arama daima **Osmanlıca eski adla** ve harf varyantlarıyla (`k/g`, `t/d`, `b/p`, `c/ç`) yapılır.
2. **Eski Sülale Lakapları ve Oymak Adları (`İşinizi En Çok Kolaylaştıran Anahtar`):** 1934 öncesi aileler `"…oğulları"`, `"…zâde"`, `"…uşağı"` gibi lakaplarla yazılırdı; aile büyüklerinden bilinen lakapları mutlaka nota ekleyin.
3. **Kütükteki En Eski Ataların Adı ve Doğum Yılları:** Belgenizdeki en dip satırlar ve bu kişilerin "Baba Adı" sütunundaki isimler.
4. **Osmanlı İdari Birimi (`Sancak / Kazâ / Nâhiye`):** Defterler bugünkü ilçelere göre değil, dönemin idari sınırlarına göre tutulmuştur (bugün A ilçesine bağlı bir köy, 1840'ta komşu B nahiyesinin defterinde olabilir!).

### Adım 2: Doğru Defter Serilerini ve Bölgesel Göç Bağlamını Tanımak
- **`NFS.d` (Nüfus Defterleri, 1830–1880'ler):** Köydeki tüm erkekleri hane hane, baba adıyla, lakabıyla, yaşıyla (`sinn`), hatta **boy ve sakal/bıyık eşkâliyle** yazar; doğum, ölüm ve askerlik şerhlerini düşer.
- **`ML.VRD.TMT.d` (Temettuat Defterleri, 1844–1845):** Hane reisinin mesleğini, tarla/bağ dönümünü, hayvan sayısını ve yıllık gelirini gösterir.
- **`MŞH.ŞSC.d` (Şer'iyye / Kadı Mahkemesi Sicilleri):** Bağlı bulunan kazanın mahkeme kayıtlarını ve vefat eden ataların miras taksimini (**tereke**) içerir; eşini, oğullarını ve nüfus defterlerinde yer almayan **kız çocuklarını** tek tek sayar.
- **`MAD.d` & `D..BŞM.CZY.d` (Avârız ve Cizye Defterleri, 1600–1850):** 17.–18. yüzyıl ayrıntılı avârız vergi hanelerini, aşiret/maden mükellefiyetlerini ve (gayrimüslim/karma veya ihtidâ geçmişi olan yerleşimlerde) **cizye** defterlerini barındırır.
- **`TT.d` & `TK.GM.d` / `A.{DVNSMHM.d` (15.–16. Yüzyıl Tapu Tahrir + Bölgesel Göç ve Kavim/Boy Analizi):** Köyün 500 yıllık ilk Osmanlı kaydını ve baba adlarıyla vergi mükelleflerini verir. Bu katmanda ayrıca **o bölgeye yapılan tarihsel göçler, konar-göçer aşiret/cemaat tahrirleri (`Yörükân, Türkmen, Ekrâd, Tatar vb.`) ve iskân fermanları** dikkatle incelenerek bölgedeki potansiyel boy ve kavim dokusu belgesel kanıtlarıyla ortaya konulur.

### Adım 3: Bütçe ve Zaman Koruyan "Önce Fihrist Testi → Nokta Atışı İndirme" Taktiği
- **Ücret Gerçeği:** Devlet Arşivleri Kataloğu'nda arama yapmak ücretsizdir; ancak filigransız yüksek çözünürlüklü her görüntü (poz) e-Satış sepetinden poz başı ücretle satın alınır. 300–500 sayfalık yanlış bir defteri toptan satın almak hem bütçeyi hem emeği boşa harcar!
- **1. Aşama (Fihrist Testi):** Defterin tamamını almadan önce sadece başındaki **Fihrist (`Mi=1..5`)** sayfalarını kontrol ettirin. Yapay zekâ fihristi ve tarihleri okuyarak yanlış dönem veya yanlış nahiyeye ait defterleri eler; doğru defterde ise **Poz (`Mi`) ≠ Varak (`vr.`)** kayma farkını hesaplayıp *"Aradığın köy Poz 33 ile 37 arasında!"* diyerek tam aralığı verir.
- **2. Aşama (Nokta Atışı İndirme):** Sadece köyünüzün bulunduğu 3–10 pozu satın alıp `.zip / .jpg` olarak bilgisayarınızdaki proje klasörüne indirin.

### Adım 4: 1:1 Piksel Kesitiyle Paleografik Okuma ve Kuşak Matematiği
Sıradan sohbet botları Osmanlıca el yazması sayfaya uzaktan bakıp harfleri tahmin eder; köy ve şahıs adlarını uydurabilir. Bu beceri ise `scripts/crop_and_verify.py` aracılığıyla:
1. İndirdiğiniz 3000 piksellik filigransız sayfaları Sağ (`R`) ve Sol (`L`) varaklara böler,
2. Her kritik satırdan **1:1 doğal piksel yakınlaştırma kesiti (crop)** alarak harf noktalarını kanıtlı okur,
3. **`+ΔYıl` Çapraz Sayım Matematiği** uygular (örneğin 1834 sayımında 4 yaşında yazılan çocuk, 6 yıl sonraki 1840 sayımında ~10 yaşında, 1844 sayımında ~14 yaşında görünmelidir),
4. **`1/N` Nadir İsim ve Yan Soy Filtresi** ile sadece düz üst soyu değil; amcaları, kardeşleri, dede adını ilk toruna verme geleneğini ve lakapları çapraz doğrular *(Unutmayın: Bir kadının soyadı veya lakabı babasından değil, eşinin hanesinden veya dul kaldığında kendi adından gelebilir!)*.

### Adım 5: Kanıt Seviyeleri ve En Sık Yapılan 5 Hata

Her eşleşme aynı kesinlikte değildir; bu beceri her bulguyu dört şeffaf kanıt seviyesinden biriyle işaretler:
- 🟢 **`[KESİN KANIT]`:** e-Devlet/Nüfus kütüğü, Esas Nüfus Defteri veya `isim + baba adı + lakap + köy + tutarlı yaş` zinciriyle doğrudan belgelenen kayıt.
- 🟡 **`[GÜÇLÜ EŞLEŞME]`:** Aynı köy, nadir isim, uyumlu yaş ve kardeş dizilimi bir arada bulunan güçlü aday.
- ⚪ **`[İSİM / SÜLALE İZİ]`:** Başka bir yüzyılda (ör. 1584 tahririnde) aynı köyde geçen aynı isim veya lakap; doğrudan kan bağı kanıtı sayılmaz, tarihsel süreklilik izi olarak belirtilir.
- 🔵 **`[BÖLGESEL GÖÇ & CEMAAT BAĞLAMI]`:** 15.–18. yüzyıl tahrir ve mühimme kayıtlarında köyün/nahiyenin çevresinde belgelenen konar-göçer boy, aşiret veya iskân hareketleri.

**En Sık Yapılan 5 Hata:**
1. *Antigravity'nin kendi dahili tarayıcısını açmak* → `"Web Sayfasına Erişim Engellendi"` hatası verir; daima normal Chrome + Chrome DevTools MCP kullanın.
2. *Benzer köy adına aldanmak* → Sayfa başlığındaki `tâbi-i ...` (bağlı olduğu kaza/nahiye) ibaresini ve komşu köyleri mutlaka doğrulayın.
3. *Dijital Poz (`Mi`) ile Osmanlıca Varak (`vr.`) numarasını karıştırmak* → Kapak ve boş sayfalar yüzünden arada sabit fark bulunur.
4. *Filigranlı düşük çözünürlüklü okumaya körü körüne güvenmek* → Kritik satırları filigransız aslından 1:1 kesitle kontrol edin.
5. *Hızlı paralel bot istekleriyle arşiv sitesini yormak* → `BelgeGoster` üzerinde çoklu paralel istek güvenlik engelini (`HTTP 418`) tetikler; daima sakin ve sıralı ilerleyin.

---

## 7. Defterde Karşılaşacağınız 15 Temel Osmanlıca Arşiv Kelimesi

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

## 8. Göçmen ve Mübadil Aileler İçin Rehber (Balkanlar, Adalar, Girit ve Kafkasya)

Ataları Anadolu dışından göç etmiş aileler için ayrıntılı kılavuz [`references/gocmen-ve-mubadil-rehberi.md`](./references/gocmen-ve-mubadil-rehberi.md) dosyasındadır. Özet yol haritası:

1. **1923–1925 Lozan Mübadilleri** (*Selanik, Drama, Kavala, Serez, Girit, Yanya, Kayalar, Midilli vb.*):  
   Cumhuriyet Arşivi **`130-16-13-2`** (*Muhtelit Mübadele Tasfiye Talepnameleri*) ve **`272`** (*Toprak İskân*) fonlarında aile reisinin adıyla arama yapın; geldikleri köy, aile fertleri ve bıraktıkları mallar tek tek yazar!
2. **93 Harbi (1877), Balkan Harbi (1912) ve Kafkasya/Kırım Muhacirleri** (*Bulgaristan, Üsküp, Manastır, Bosna, Çerkes, Çeçen, Abaza, Kırım, Ahıska*):  
   Osmanlı Arşivi **`DH.SN..THR.`**, **`DH.İ.UM`**, **`DH.MKT.`**, **`Y..PRK.KOM.`** ve **`A.}MKT.NZD.`** fonlarında *"Aile reisi + yerleştirildiği ilçe/köy"* ile Muhacir Kâğıdı ve İskân Kaydı aratın.
3. **Büyük Arşiv Sürprizi:**  
   *Tuna (Bulgaristan), Selanik, Manastır, Yanya, Filibe, Varna, Üsküp, Gümülcine, Midilli* gibi pek çok Balkan ve Adalar sancağının **1830–1875 Osmanlı Nüfus Defterleri (`NFS.d`)** Türkiye'deki Osmanlı Arşivi'ndedir! İsim Denklik Belgesi veya Tasfiye Talepnamesi ile eski köyünüzü öğrendikten sonra 1840 Balkan nüfus defterinizi de bu beceriyle okutabilirsiniz.

---

## 9. Çok Sayfalı Defter ve El Yazmalarını 10 Paralel Alt-Ajan ile Okutma / Tercüme

Elinizde 50–100+ sayfalık bir **Osmanlıca defter** veya **Arapça/Osmanlıca/Farsça bir el yazması PDF** varsa Antigravity'nin **paralel alt-ajan (`subagent`)** mimarisini kullanarak sayfaları tek tek beklemek yerine **10'ar 10'ar paralel** çevirtebilir veya okutabilirsiniz:

1. **10'lu Paralel Gruplar:** Ana sohbet oturumunuz koordinatör olarak çalışır; aynı anda 10 alt-ajan arka planda farklı birer sayfayı (`sayfa_001.md` ... `sayfa_010.md`) çevirip kaydeder ve işi bitince kapanır.
2. **Ortak Terim ve Lakap Sözlüğü (`glossary.md`):** Tüm alt-ajanlar ortak bir `glossary.md` dosyasını okur; teknik kavramların, şahıs adlarının ve lakapların her sayfada aynı karşılıkla çevrilmesini sağlar.
3. **Son Tutarlılık Editörü Ajanı:** Tüm sayfalar tamamlandığında ayrı bir denetçi ajan tüm dosyaları baştan sona tarayarak sayfalar arası üslup ve kavram birliğini sağlar.

> Hazır şablon istem için [`examples/ornek-kullanim-promptlari.md`](./examples/ornek-kullanim-promptlari.md) içindeki **5. Şablona**, kapsamlı yazma eser tercüme araçları için ise kardeş projemiz **[`shnfatih-hash/yazma-eser-paralel-tercume`](https://github.com/shnfatih-hash/yazma-eser-paralel-tercume)** deposuna göz atabilirsiniz.

---

## 10. 5 Adımda Hızlı Başlangıç ve Kopyala–Yapıştır Ana Prompt

1. **Proje Klasörü Aç & Belgeni Koy:** Masaüstünde `Soy_Kutugu_Arastirmam` klasörü aç, Antigravity'de bu klasörü aç ve [e-Devlet Alt-Üst Soy Bilgisi](https://www.turkiye.gov.tr/nvi-alt-ust-soy-bilgisi-sorgulama) PDF'ini (veya Nüfus Müdürlüğü belgeni) içine koy.
2. **Normal Chrome'da Kataloğa Gir:** Bilgisayarındaki **normal Google Chrome**'da `chrome://inspect/#remote-debugging` ayarını aç ve [katalog.devletarsivleri.gov.tr](https://katalog.devletarsivleri.gov.tr) adresine e-Devlet ile ücretsiz giriş yap *(Antigravity'nin kendi iç tarayıcısını kullanma)*.
3. **Önce Fihristi Kontrol Ettir:** Tüm defteri hemen satın alma! Önce fihrist veya ilk 5–10 pozu Antigravity'ye kontrol ettirip doğru defter ve varak aralığını buldur.
4. **Nokta Atışı İndir:** Sadece köyünün bulunduğu doğru sayfa aralığını e-Satış'tan indirip `.zip / .jpg` olarak proje klasörüne koy.
5. **1:1 Kanıtlı Okut:** Aşağıdaki komutu kopyalayıp Antigravity'ye gönder *(diğer 4 senaryo şablonu için bkz. [`examples/ornek-kullanim-promptlari.md`](./examples/ornek-kullanim-promptlari.md))*:

```markdown
Sana e-Devlet "Alt-Üst Soy Bilgisi" belgemi ve (varsa) Devlet Arşivleri'nden indirdiğim `.zip / .jpg` dosyalarını bu proje klasöründe verdim; normal Google Chrome'da `https://katalog.devletarsivleri.gov.tr` oturumum da açık.

ÖNEMLİ: Antigravity'nin kendi dahili tarayıcısını AÇMA ("Web Sayfasına Erişim Engellendi" hatası verir); doğrudan Chrome DevTools MCP ile açık Google Chrome sekmeme bağlan ve ürettiğin tüm 1:1 kesitleri ve raporları bu proje klasörüne kaydet.

Lütfen `devlet-arsivleri-soykutugu` becerisini etkinleştirerek tahmin yürütmeden, her kritik hane ve şerh satırını 1:1 piksel belge kesitiyle doğrulayarak anne ve baba tarafı üst soyumu, kardeş/amca yan kollarını, köyümüzün eski adını, idari evrimini, 15.–16. yy. bölgesel göç/boy bağlamını ve tarihî olaylarını kanıt seviyeleriyle (`[KESİN] / [GÜÇLÜ] / [İSİM İZİ] / [BÖLGESEL GÖÇ BAĞLAMI]`) çıkar.
```

---

## 11. Paket Yapısı, Kardeş Projeler, Gönüllü Destek ve Lisans

```text
devlet-arsivleri-soykutugu/
├── SKILL.md                                         # Yapay zekâ ajanları için ana beceri yönergesi
├── README.md                                        # Kurulum, sorun giderme, metodoloji ve kullanım kılavuzu
├── app.py                                           # Hugging Face Spaces canlı Gradio web aracı
├── requirements.txt                                 # Web aracı ve görüntü işleme bağımlılıkları
├── LICENSE                                          # MIT Açık Kaynak Lisansı
├── references/
│   ├── fon-kodlari-ve-paleografya-rehberi.md        # 1500–1925 fon kodları (Cizye & boy/iskân dâhil), takvim & sözlük
│   └── gocmen-ve-mubadil-rehberi.md                 # Balkanlar, Adalar, Girit ve Kafkasya göçmen/mübadil kılavuzu
├── scripts/
│   ├── dab_helpers.js                               # Chrome DevTools MCP sıralı/WAF korumalı arama ve varak yardımcıları
│   ├── crop_and_verify.py                           # .zip/.jpg defterlerden varak bölme ve 1:1 piksel kesit alma aracı
│   └── tarih_cevirici.py                            # 3 yönlü Hicrî ↔ Rûmî ↔ Milâdî kesin tarih çevirici (TTK bağlantılı)
└── examples/
    └── ornek-kullanim-promptlari.md                 # 5 farklı senaryo için hazır kopyala-yapıştır istem şablonları
```

### Kardeş Projeler (Osmanlıca Resmî Evrak & Yazma Eser Paralel Tercüme)

- **[`shnfatih-hash/osmanlica-resmi-evrak`](https://github.com/shnfatih-hash/osmanlica-resmi-evrak):** Ferman, Berat, İrade-i Seniyye, Tahrirat, Mazbata, Arz-ı Hâl, Hüccet ve Vakfiyeleri **TDV İA / TTK transkripsiyon sistemi**, şerh (kritik aparat) ve kelime/tamlama çözümlemeli interaktif HTML çalışma kartıyla okuma becerisi.
- **[`shnfatih-hash/yazma-eser-paralel-tercume`](https://github.com/shnfatih-hash/yazma-eser-paralel-tercume):** Çok sayfalı Arapça, Osmanlıca ve Farsça el yazması PDF/görsel eserleri **10'lu paralel alt-ajan (`subagents`)**, ortak terim sözlüğü (`glossary.md`) ve son tutarlılık editörü ajanıyla tercüme ve tahkik becerisi.

### Teşekkür ve İlham Kaynağı

Bu beceri paketi ve araştırma metodolojisi, **Said Sürücü**'nün seminerinden hareketle hazırlanmış ve geliştirilmiştir. Yapay zekâ destekli arşiv ve soy kütüğü araştırmalarına ilham veren kıymetli paylaşımı ve rehberliği için **Said Sürücü**'ye gönülden teşekkür ederiz.

### 🤝 Soru Sor, Fon / Terim Ekle ve Katkıda Bulun

Kod veya Git bilmeden de aşağıdaki hazır formlarla teknik soru sorabilir, yeni fon kodu, göçmen/mübadil kaynağı veya Osmanlıca arşiv kelimesi katkısı gönderebilirsiniz (ayrıntılar: [CONTRIBUTING.md](CONTRIBUTING.md)):

- ❓ **[Teknik Soru & Arşiv / Chrome MCP Desteği](https://github.com/shnfatih-hash/devlet-arsivleri-soykutugu/issues/new?template=01-soru-ve-teknik-destek.yml)**
- 📖 **[Yeni Fon Kodu, Eski Köy Adı veya Arşiv Terimi Katkısı](https://github.com/shnfatih-hash/devlet-arsivleri-soykutugu/issues/new?template=02-terim-ve-sozluk-katkisi.yml)**
- 💡 **[Yeni Prompt veya Özellik Önerisi](https://github.com/shnfatih-hash/devlet-arsivleri-soykutugu/issues/new?template=03-prompt-ve-yontem-onerisi.yml)**
- 🐛 **[Hata Bildirimi](https://github.com/shnfatih-hash/devlet-arsivleri-soykutugu/issues/new?template=04-hata-bildirimi.yml)** • 💬 **[Hugging Face Topluluk](https://huggingface.co/spaces/sahanfatih/devlet-arsivleri-soykutugu/discussions)**

### ♥ Projeye Gönüllü Destek

Bu proje tamamen ücretsiz ve açık kaynaklıdır; herkesin özgürce kullanımına açık kalacaktır. Çalışmayı faydalı bulduysanız ve yeni Osmanlı arşivi / dijital beşerî bilimler AI Skill'lerinin geliştirilmesine gönüllü olarak katkıda bulunmak isterseniz bir kahve ısmarlayarak veya GitHub Sponsors üzerinden destek olabilirsiniz:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Bir%20Kahve%20Ismarla-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/shnfatih8)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Projeye%20Destek%20Ol-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/shnfatih-hash)

### Lisans

Bu proje **MIT Lisansı** ile herkesin özgürce kullanımına, geliştirmesine ve paylaşımına sunulmuştur.
