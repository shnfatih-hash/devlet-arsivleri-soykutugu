# Hazır Kullanım İstemleri (Kopyala – Yapıştır Prompt Şablonları)

Bu dosyadaki hazır istemleri (promptları), araştırma aşamanıza göre doğrudan kopyalayıp **Google Antigravity** (veya beceriyi yüklediğiniz diğer yapay zekâ ajanlarına) gönderebilirsiniz.

---

## 1. Ana Başlangıç İstemi: e-Devlet / Nüfus Müdürlüğü Belgesi + Canlı Chrome DevTools MCP Taraması

*Kullanım zamanı: Bilgisayarınızda özel bir proje klasörü (ör. `Soy_Kutugu_Arastirmam`) oluşturup Antigravity'de açtığınızda, e-Devlet Alt-Üst Soy PDF belgenizi bu klasöre koyduğunuzda ve **normal Google Chrome**'da `katalog.devletarsivleri.gov.tr` oturumunuzu açtığınızda.*

```markdown
Sana e-Devlet'ten aldığım "Alt-Üst Soy Bilgisi" belgemi (veya Nüfus Müdürlüğü kayıt örneğimi) bu proje klasörünün içine koydum. Bilgisayarımdaki normal Google Chrome tarayıcımda `chrome://inspect/#remote-debugging` ayarını etkinleştirdim ve `https://katalog.devletarsivleri.gov.tr` adresine kendi e-Devlet şifremle giriş yaptım. (Bilinen aile lakaplarımız / ek bilgilerimiz: [...varsa buraya yazın...])

ÖNEMLİ KURAL: Antigravity'nin kendi dahili/yerleşik tarayıcısını ASLA açma ("Web Sayfasına Erişim Engellendi" hatası verir); doğrudan `chrome-devtools` MCP üzerinden açık olan normal Google Chrome sekmeme bağlanarak ilerle. İhtiyaç duyduğun yardımcı betikleri kullan ve ürettiğin tüm 1:1 belge kesitleri ile raporları bu proje klasörünün içine düzenli alt klasörler halinde kaydet.

Lütfen `devlet-arsivleri-soykutugu` becerisini kullanarak şu adımları uygula:

1. **4 Temel İpucu ve Kütük Duvarı Analizi:**
   - Baba ve anne tarafımdaki en eski atalarımı, baba/anne adlarını, doğum yıllarını (`tarih_cevirici.py` ile Milâdî → Hicrî/Rûmî karşılıklarıyla), Cilt–Hane–Sıra numaralarını, sülale lakaplarımızı ve köylerimizin Cumhuriyet öncesi **eski Osmanlıca adlarını** ve bağlı oldukları **eyalet / sancak / kaza / nahiye** zincirini (komşu kaza/nahiye geçiş ihtimalleriyle birlikte) çıkar.

2. **Bütçe Koruyan "Önce Fihrist" Katalog Taraması (1830–1500):**
   - Katalogda `NFS.d` (1830–1880 Nüfus), `ML.VRD.TMT.d` (1844–1845 Temettuat), `A.{RSK.d` (1835–1838 İmam-Muhtar), `MŞH.ŞSC.d` (Şer'iyye Sicilleri / Tereke), `MAD.d` & `D..BŞM.CZY.d` (Avârız ve varsa Cizye defterleri) ile `TT.d / TK.GM.d` (15.–16. yy. Tapu Tahrir ve bölgesel cemaat/göç kayıtları) fonlarında köyümü ve bağlı olduğu kaza/nahiye toplu defterlerini ara.
   - Güvenlik duvarını (`HTTP 418`) tetiklememek için paralel istek atmadan, önce defterlerin **Fihrist (`Mi=1..5`)** sayfalarını kontrol et; yanlış dönem veya farklı nahiyeye ait defterleri ele; doğru defterlerde **Poz (`Mi`) ≠ Varak (`vr.`)** farkını hesaplayarak köyümün tam hangi poz aralığında başladığını tespit et.

3. **Kanıtlı Eşleştirme, Bölgesel Göç Bağlamı ve Nokta Atışı İndirme Listesi:**
   - Önizlemeden okunabilen kayıtları kuşak matematiğiyle (`+ΔYıl` yaş farkı ve `1/N` hane filtresi) analiz et; 15.–16. yy. tahrir katmanında bölgemize yapılan göç/iskân hareketlerini ve belgelerde geçen cemaat/boy kayıtlarını da tarihsel bağlamıyla incele. Her bulguyu `[KESİN KANIT]`, `[GÜÇLÜ EŞLEŞME]`, `[İSİM İZİ]` veya `[BÖLGESEL GÖÇ & CEMAAT BAĞLAMI]` olarak etiketle, okunamayan yerleri asla tahminle doldurma.
   - e-Satış sepetinden gereksiz tüm defteri değil, **sadece doğru sayfa aralıklarını** indirebilmem için tam `Fon Kodu | Defter No | Tarih | Varak No | Dijital Poz (Mi) Aralığı | İçerik` tablosunu ver.
```

---

## 2. İndirilmiş `.zip / .jpg` Klasörü İstemi: 1:1 Piksel Kesitli Kesin Okuma

*Kullanım zamanı: Devlet Arşivleri e-Satış sepetinden doğru sayfa aralıklarını `.zip` veya `.jpg` olarak bilgisayarınızdaki bir klasöre indirdiğinizde.*

```markdown
Devlet Arşivleri'nden indirdiğim filigransız yüksek çözünürlüklü `.zip / .jpg` arşiv belgelerini çalışma klasörüme koydum.

Lütfen `devlet-arsivleri-soykutugu` becerisindeki `scripts/crop_and_verify.py` aracını kullanarak:
1. Klasördeki tüm sayfaların envanterini çıkar; her sayfanın başlığındaki `Karye-i ... tâbi-i ...` ibaresini kontrol ederek yanlış/komşu köy sayfası karışmışsa kanıtıyla ayır.
2. Doğru köy sayfalarını Sağ (`R`) ve Sol (`L`) varaklara ve yatay okuma şeritlerine böl; tahmin yürütmeden, her kritik hane ve şerh satırından **1:1 doğal piksel yakınlaştırma kesiti (crop)** alarak oku.
3. Sadece düz üst soyumu değil; aynı lakabı taşıyan **amca, kardeş ve yan kol hanelerini**, doğum (`tevellüd`), vefat (`fevt`) ve askerlik (`reft be-askeriyye / redîf`) şerhlerini de eksiksiz çıkar.
4. Sayımlar arası yaş artışlarını (`+ΔYıl`) çapraz doğrula ve her halkanın kanıt seviyesini (`[KESİN] / [GÜÇLÜ] / [İSİM İZİ]`) belirterek kapsamlı soy kütüğü raporumu oluştur.
```

---

## 3. Göçmen ve Mübadil Aileler İçin Özel Tarama İstemi

*Kullanım zamanı: Ataları Balkanlar, Ege/Akdeniz Adaları, Girit, Kırım veya Kafkasya'dan göç etmiş / mübadeleyle gelmiş aileler için.*

```markdown
Atalarımız [Selanik / Drama / Girit / Bulgaristan-Tuna / Üsküp / Kafkasya vb.] bölgesinden gelerek [İl / İlçe / Köy] yerleşimine iskân edilmiş. e-Devlet Alt-Üst Soy belgemi (ve varsa İsim Denklik bilgimi) ekledim; Chrome'da `https://katalog.devletarsivleri.gov.tr` oturumum açık.

Lütfen `devlet-arsivleri-soykutugu` göçmen ve mübadil rehberini izleyerek:
1. 1923–1925 mübadelesi ise Cumhuriyet Arşivi `130-16-13-2` (*Tasfiye Talepnameleri*) ve `272` (*Toprak İskân*) fonlarında; 93 Harbi, Balkan Harbi veya Kafkas göçü ise Osmanlı Arşivi `DH.SN..THR.`, `DH.İ.UM`, `DH.MKT.`, `Y..PRK.KOM.` ve `A.}MKT.NZD.` fonlarında aile reisimizin adı ve iskân yeriyle tarama yap.
2. Geldikleri tam kaza ve köy adını netleştirdikten sonra, Osmanlı Arşivi'ndeki **1830–1875 Balkan/Adalar Nüfus (`NFS.d`) ve 1845 Temettuat (`ML.VRD.TMT.d`)** defterlerinde o köyün kaydını ara ve indirmem gereken tam defter/poz numaralarını çıkar.
```

---

## 4. Avrupa *Ortsgeschichte* Usulünde Köy ve Aile Tarihi Kitabı İstemi

*Kullanım zamanı: Soy kütüğü ve köy belgeleri toplandıktan sonra kalıcı bir aile/köy monografisi hazırlatmak istediğinizde.*

```markdown
Elde ettiğimiz tüm birincil arşiv belgelerini, filigransız hane kayıtlarını ve katalog bulgularını kullanarak; Avrupa yerel ve mikro-tarihçiliği (*Ortsgeschichte / Microstoria*) disipliniyle köyümüzün ve ailemizin tarihini çok bölümlü, baskıya hazır bir monografi olarak yaz.

Yazım kuralları:
- Tüm yer, kurucu sülale, şahıs ve kurum adlarının belgede geçen özgün Osmanlıca yazılışlarını parantez içinde göster; her olayı ve rakamı tam arşiv künyesine (`Fon, Defter/Dosya, Varak/Poz, Hicrî/Milâdî Tarih`) bağla.
- Köyün coğrafyasını, isim kökenini, 16.–19. yüzyıl idari/vergi evrimini, kurucu ocaklarını, salgın ve kıtlıklarını, dini/tasavvufi ve gündelik yaşamını, Osmanlı'dan Çanakkale ve İstiklâl Harbi'ne askerlerini/şehitlerini ve Cumhuriyet dönemi göç serüvenini katmanlı biçimde ele al; orijinal belge kesitlerini ilgili bölümlere tıpkıbasım levha olarak yerleştir.
```

---

## 5. Çok Sayfalı Defter veya Yazma Eseri 10 Paralel Alt-Ajan (`Subagents`) + Ortak Sözlük (`glossary.md`) ile Okutma

*Kullanım zamanı: Elinizde 20–100+ sayfalık toplu bir Nüfus/Temettuat/Şer'iyye defteri veya Arapça/Osmanlıca el yazması PDF dosyası olduğunda.*

```markdown
Bu proje klasöründeki çok sayfalı arşiv defteri / el yazması dosyasını (`defter.pdf` veya görüntü klasörü) paralel alt-ajan orkestrasyonuyla eksiksiz oku ve tercüme/transkripsiyon et:

1. Önce sayfaları ayrı görüntülere çıkar ve proje klasöründe tüm ajanların ortak okuyup güncelleyeceği bir `glossary.md` (sülale lakapları, şahıs/yer adları, teknik terimler ve yazım kuralları sözlüğü) dosyası oluştur.
2. Sayfaları **10'arlı gruplar halinde paralel alt-ajanlara (`subagent`)** dağıt: aynı anda çalışan 10 ajan kendi sayfasını 1:1 kesit disipliniyle okuyup `sayfalar/sayfa_001.md`, `sayfa_002.md` ... şeklinde kaydetsin; okunamayan yerleri uydurmayıp `[...]` şerhi düşsün ve yeni tespit ettiği terimleri/lakapları ortak `glossary.md` için raporlasın.
3. Tüm sayfalar tamamlandığında ayrı bir **Tutarlılık ve Tahkik Editörü Alt-Ajanı** görevlendir; `glossary.md` üzerinden varak sonlarındaki rekabe (*müş‘ir kelime*) tekrarlarını temizleyip sayfa geçişinde bölünen kayıtları birleştir ve tüm sayfalardaki şahıs adlarını, lakapları, tarihleri ve kavram birliğini baştan sona denetleyip tek parça nihai metin ve dizin dosyasını oluştur.
```
