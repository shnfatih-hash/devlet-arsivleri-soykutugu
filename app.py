#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hugging Face Spaces Canlı Web Aracı — Devlet Arşivleri Soy Kütüğü ve Köy Tarihi AI Skill
"""

from __future__ import annotations

import datetime
from pathlib import Path
from PIL import Image

import gradio as gr

from scripts.tarih_cevirici import (
    HICRI_AY_ADLARI,
    HICRI_AYLAR,
    RUMI_AY_ADLARI,
    RUMI_AYLAR,
    TTK_URL,
    format_tr,
    gregorian_to_jdn,
    hijri_to_jdn,
    jdn_to_gregorian,
    jdn_to_hijri,
    jdn_to_rumi,
    julian_to_jdn,
    parse_hicri_day,
)

ROOT = Path(__file__).resolve().parent

SUPPORT_BANNER_HTML = """
<div style="background: linear-gradient(135deg, #1b2838 0%, #2b3e50 100%); color: #fff; padding: 20px 24px; border-radius: 12px; border-bottom: 4px solid #ffdd00; margin-bottom: 14px;">
  <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 14px;">
    <div>
      <h2 style="margin: 0 0 6px; font-size: 1.45rem; color: #fff;">📜 Devlet Arşivleri Soy Kütüğü ve Köy Tarihi AI Skill</h2>
      <p style="margin: 0; opacity: 0.92; font-size: 0.95rem;">
        e-Devlet / Nüfus Müdürlüğü kaydından 1500'lü yıllara kadar 1:1 piksel kesitli Osmanlı arşiv araştırma aracı ve AI ajan becerisi.
      </p>
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 10px; align-items: center;">
      <a href="https://buymeacoffee.com/shnfatih8" target="_blank" rel="noopener"
         style="background: #FFDD00; color: #111; font-weight: 700; padding: 9px 16px; border-radius: 8px; text-decoration: none; font-size: 0.92rem; box-shadow: 0 2px 6px rgba(0,0,0,0.2);">
        ☕ Bir Kahve Ismarla (Buy Me a Coffee)
      </a>
      <a href="https://github.com/sponsors/shnfatih-hash" target="_blank" rel="noopener"
         style="background: #ea4aaa; color: #fff; font-weight: 700; padding: 9px 16px; border-radius: 8px; text-decoration: none; font-size: 0.92rem;">
        💖 GitHub Sponsors
      </a>
      <a href="https://github.com/shnfatih-hash/devlet-arsivleri-soykutugu" target="_blank" rel="noopener"
         style="background: #24292f; color: #fff; font-weight: 600; padding: 9px 14px; border-radius: 8px; text-decoration: none; font-size: 0.9rem; border: 1px solid #57606a;">
        ⭐ GitHub Deposu
      </a>
    </div>
  </div>
</div>
"""


def convert_calendar(cal_type: str, day_str: str, month_str: str, year_val: int) -> str:
    try:
        year = int(year_val)
        if cal_type == "Hicrî Kamerî":
            ay_key = month_str.split(" ")[0].strip().lower()
            m = HICRI_AYLAR[ay_key]
            d1, d2, label = parse_hicri_day(day_str)
            j1 = hijri_to_jdn(year, m, d1)
            dt1 = jdn_to_gregorian(j1)
            if d1 == d2:
                miladi = format_tr(dt1)
                rumi = jdn_to_rumi(j1)
            else:
                j2 = hijri_to_jdn(year, m, d2)
                miladi = f"{format_tr(dt1)} — {format_tr(jdn_to_gregorian(j2))}"
                rumi = f"{jdn_to_rumi(j1)} — {jdn_to_rumi(j2)}"
            return (
                f"### Dönüşüm Sonucu\n"
                f"- **Girdi:** H. {label} {HICRI_AY_ADLARI[m]} {year}\n"
                f"- **Milâdî Karşılık:** {miladi}\n"
                f"- **Rûmî Karşılık:** {rumi}\n"
                f"- **Resmî Doğrulama:** [TTK Tarih Çevirme Kılavuzu]({TTK_URL})"
            )

        if cal_type == "Rûmî Malî":
            d = int(day_str.strip())
            ay_key = month_str.split(" ")[0].strip().lower()
            m = RUMI_AYLAR[ay_key]
            if year < 1333 or (year == 1333 and m in (1, 2)):
                jy = year + (585 if m in (1, 2) else 584)
                jdn = julian_to_jdn(jy, m, d)
            else:
                dt_g = datetime.date(year + 584, m, d)
                jdn = gregorian_to_jdn(dt_g.year, dt_g.month, dt_g.day)
            dt = jdn_to_gregorian(jdn)
            hy, hm, hd = jdn_to_hijri(jdn)
            return (
                f"### Dönüşüm Sonucu\n"
                f"- **Girdi:** R. {d} {RUMI_AY_ADLARI[m]} {year}\n"
                f"- **Milâdî Karşılık:** {format_tr(dt)}\n"
                f"- **Hicrî Karşılık:** H. {hd} {HICRI_AY_ADLARI[hm]} {hy}\n"
                f"- **Resmî Doğrulama:** [TTK Tarih Çevirme Kılavuzu]({TTK_URL})"
            )

        d = int(day_str.strip())
        m = int(month_str.split(" ")[0].strip())
        dt = datetime.date(year, m, d)
        jdn = gregorian_to_jdn(dt.year, dt.month, dt.day)
        hy, hm, hd = jdn_to_hijri(jdn)
        return (
            f"### Dönüşüm Sonucu\n"
            f"- **Girdi (Milâdî):** {format_tr(dt)}\n"
            f"- **Hicrî Karşılık:** H. {hd} {HICRI_AY_ADLARI[hm]} {hy}\n"
            f"- **Rûmî Karşılık:** {jdn_to_rumi(jdn)}\n"
            f"- **Resmî Doğrulama:** [TTK Tarih Çevirme Kılavuzu]({TTK_URL})"
        )
    except Exception as exc:
        return f"**Hata:** Lütfen girdi alanlarını kontrol edin (`{exc}`)."


def calculate_census_ages(birth_year: int) -> str:
    by = int(birth_year)
    censuses = [
        (1831, "H. 1246–1247 II. Mahmud İlk Erkek Nüfus Sayımı (`NFS.d`)"),
        (1840, "H. 1256 Tanzimat Nüfus Yoklama Defteri (`NFS.d`)"),
        (1845, "H. 1260–1261 Genel Nüfus ve Temettuat Sayımı (`NFS.d` / `ML.VRD.TMT.d`)"),
        (1882, "R. 1297–1299 Sicill-i Nüfus Atîk/Esas Kütüğü — 1. Dalga"),
        (1905, "R. 1320–1321 Genel Nüfus Tahriri — 2. Dalga"),
    ]
    lines = [f"### Milâdî **{by}** Doğumlu Bir Atanın Osmanlı Defterlerinde Beklenen Yaşı (`sinn`)\n"]
    for cy, desc in censuses:
        diff = cy - by
        if diff < 0:
            durum = f"Henüz doğmamış ({abs(diff)} yıl sonra doğacak — babasının hanesini arayın)"
        else:
            durum = f"**~{diff} yaşında** (`±2–3` yaş taşra kaydı payıyla: `{max(0, diff - 3)}–{diff + 3}`)"
        lines.append(f"- **{cy}** — {desc}: {durum}")
    return "\n".join(lines)


def split_and_crop(img: Image.Image | None, x1: float, y1: float, x2: float, y2: float, zoom: float):
    if img is None:
        return None, None, None
    im = img.convert("RGB")
    w, h = im.size
    right_folio = im.crop((int(w * 0.47), 0, w, h))
    left_folio = im.crop((0, 0, int(w * 0.53), h))

    bx1, bx2 = sorted([int(x1 * w), int(x2 * w)])
    by1, by2 = sorted([int(y1 * h), int(y2 * h)])
    bx2 = max(bx1 + 10, bx2)
    by2 = max(by1 + 10, by2)
    crop = im.crop((bx1, by1, min(w, bx2), min(h, by2)))
    if zoom > 1.0:
        crop = crop.resize((int(crop.width * zoom), int(crop.height * zoom)), Image.Resampling.NEAREST)
    return right_folio, left_folio, crop


def generate_custom_prompt(il_ilce: str, koy: str, eski_koy: str, lakap: str, koken: str) -> str:
    il_ilce = il_ilce.strip() or "[İl / İlçe]"
    koy = koy.strip() or "[Köy / Mahalle]"
    eski_str = f" (bilinen eski adı: {eski_koy.strip()})" if eski_koy.strip() else ""
    lakap_str = lakap.strip() or "Henüz bilinmiyor — defterlerden tespit edilsin"

    goc_ek = ""
    if "Mübadil" in koken or "Göçmen" in koken:
        goc_ek = (
            "\n- Ailemiz göçmen/mübadil kökenli olduğundan Cumhuriyet Arşivi `130-16-13-2` (Tasfiye Talepnameleri), "
            "`272` (Toprak İskân) ve Osmanlı Arşivi `DH.SN..THR.` fonlarıyla birlikte geldikleri Balkan/Adalar/Kafkas "
            "yerleşiminin 1830–1875 `NFS.d` nüfus defterlerini de tara."
        )

    return f"""Sana e-Devlet "Alt-Üst Soy Bilgisi" belgemi (veya Nüfus Müdürlüğü kayıt örneğimi) bu proje klasörünün içine koydum. Bilgisayarımdaki normal Google Chrome tarayıcımda `chrome://inspect/#remote-debugging` ayarını etkinleştirdim ve `https://katalog.devletarsivleri.gov.tr` adresine kendi e-Devlet şifremle giriş yaptım.

- Araştırılacak Yerleşim: {il_ilce} — {koy}{eski_str}
- Bilinen Sülale Lakabı / Ek Bilgi: {lakap_str}
- Aile Köken Durumu: {koken}

ÖNEMLİ KURAL: Antigravity'nin kendi dahili tarayıcısını ASLA açma ("Web Sayfasına Erişim Engellendi" hatası verir); doğrudan `chrome-devtools` MCP üzerinden açık olan normal Google Chrome sekmeme bağlan ve ürettiğin tüm 1:1 piksel kesitleri ile raporları bu proje klasörüne kaydet.

Lütfen `devlet-arsivleri-soykutugu` becerisini kullanarak:
1. En eski atalarımı, doğum yıllarının Hicrî/Rûmî karşılıklarını ve köyümüzün Cumhuriyet öncesi Osmanlıca adını ve bağlı olduğu Sancak/Kaza/Nahiye zincirini çıkar.
2. `NFS.d` (Nüfus), `ML.VRD.TMT.d` (Temettuat), `MŞH.ŞSC.d` (Şer'iyye Sicilleri / Tereke), `MAD.d` & `D..BŞM.CZY.d` (Avârız ve Cizye) ve `TT.d / TK.GM.d` (15.–16. yy. Tapu Tahrir + bölgesel göç/boy/cemaat kayıtları) fonlarında önce **Fihrist (`Mi=1..5`)** kontrolü yaparak doğru defter ve poz (`Mi`) aralıklarını tespit et.{goc_ek}
3. Tahmin yürütmeden, her kritik hane ve şerh satırını 1:1 piksel kesitiyle doğrulayarak bulguları `[KESİN KANIT]`, `[GÜÇLÜ EŞLEŞME]`, `[İSİM İZİ]` ve `[BÖLGESEL GÖÇ & CEMAAT BAĞLAMI]` seviyeleriyle raporla."""


def build_ui() -> gr.Blocks:
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
    # Strip YAML frontmatter when rendering inside README tab
    if readme_text.startswith("---"):
        parts = readme_text.split("---", 2)
        if len(parts) == 3:
            readme_text = parts[2].strip()

    with gr.Blocks(title="Devlet Arşivleri Soy Kütüğü & Köy Tarihi AI Skill") as demo:
        gr.HTML(SUPPORT_BANNER_HTML)

        with gr.Tabs():
            with gr.Tab("✍️ Kişisel Prompt Üretici & Hata Çözümü"):
                gr.Markdown(
                    "### Google Antigravity / Claude İçin Hazır Araştırma İstemi Oluşturun\n"
                    "> **⚠️ `'Web Sayfasına Erişim Engellendi'` Hatası Alıyorsanız:** Antigravity'nin sağ paneldeki kendi yerleşik tarayıcısını kapatın; bilgisayarınızdaki **normal Google Chrome**'da `chrome://inspect/#remote-debugging` kutusunu işaretleyip Devlet Arşivleri'ne normal Chrome'dan giriş yapın."
                )
                with gr.Row():
                    in_il = gr.Textbox(label="İl / İlçe", placeholder="Örn: Konya / Bozkır veya Bursa / İnegöl")
                    in_koy = gr.Textbox(label="Bugünkü Köy / Mahalle Adı", placeholder="Örn: Hisarlık")
                    in_eski = gr.Textbox(label="Biliniyorsa Eski Köy Adı (İsteğe Bağlı)", placeholder="Örn: Asarlık")
                with gr.Row():
                    in_lakap = gr.Textbox(label="Bilinen Sülale Lakapları", placeholder="Örn: Hacıalioğulları, Mollagil...")
                    in_koken = gr.Dropdown(
                        label="Aile Köken / Göç Durumu",
                        choices=[
                            "Anadolu Yerleşik / Konar-Göçer Kök",
                            "1923–1925 Lozan Mübadili (Selanik, Drama, Girit, Kavala vb.)",
                            "93 Harbi / Balkan / Kafkasya / Kırım Göçmeni (Muhacir)",
                        ],
                        value="Anadolu Yerleşik / Konar-Göçer Kök",
                    )
                btn_prompt = gr.Button("🚀 Kopyala–Yapıştır Prompt Üret", variant="primary")
                out_prompt = gr.Code(label="Antigravity / Claude Sohbetine Yapıştıracağınız İstem", language="markdown")
                btn_prompt.click(
                    generate_custom_prompt,
                    inputs=[in_il, in_koy, in_eski, in_lakap, in_koken],
                    outputs=out_prompt,
                )

            with gr.Tab("🗓️ Osmanlıca Tarih & Kuşak Yaşı Hesaplayıcı"):
                with gr.Row():
                    with gr.Column():
                        gr.Markdown("### 3 Yönlü Hicrî ↔ Rûmî ↔ Milâdî Çevirici")
                        cal_type = gr.Dropdown(
                            label="Kaynak Takvim",
                            choices=["Hicrî Kamerî", "Rûmî Malî", "Milâdî"],
                            value="Hicrî Kamerî",
                        )
                        day_in = gr.Textbox(label="Gün (veya gurre / evail / evasit / evahir / selh)", value="10")
                        month_in = gr.Textbox(
                            label="Ay Adı, Numarası veya Arşiv Kısaltması (M, S, Ra, R, Ca, C, B, Ş, N, L, Za, Z)",
                            value="C",
                        )
                        year_in = gr.Number(label="Yıl", value=1261, precision=0)
                        btn_cal = gr.Button("Tarihi Çevir", variant="primary")
                        out_cal = gr.Markdown()
                        btn_cal.click(convert_calendar, inputs=[cal_type, day_in, month_in, year_in], outputs=out_cal)

                    with gr.Column():
                        gr.Markdown("### `+ΔYıl` Çapraz Sayım Kuşak Yaşı Hesaplayıcı")
                        birth_in = gr.Number(label="Atanın Milâdî Doğum Yılı (Örn: 1827)", value=1827, precision=0)
                        btn_age = gr.Button("Defterlerdeki Beklenen Yaşını Hesapla", variant="primary")
                        out_age = gr.Markdown()
                        btn_age.click(calculate_census_ages, inputs=birth_in, outputs=out_age)

            with gr.Tab("🔍 Varak Ayırma (Sağ/Sol) & 1:1 Piksel Kesiti"):
                gr.Markdown(
                    "İndirdiğiniz yüksek çözünürlüklü Osmanlıca defter sayfasını yükleyin; araç otomatik olarak **Sağ Varak (`vr. a`)** ve **Sol Varak (`vr. b`)** olarak ikiye ayırır ve seçtiğiniz koordinattan **1:1 piksel kanıt kesiti** alır."
                )
                with gr.Row():
                    in_img = gr.Image(type="pil", label="Arşiv Defteri Sayfası Yükle (.jpg / .png)")
                    with gr.Column():
                        s_x1 = gr.Slider(0.0, 1.0, value=0.52, step=0.01, label="Sol Sınır (x1)")
                        s_y1 = gr.Slider(0.0, 1.0, value=0.10, step=0.01, label="Üst Sınır (y1)")
                        s_x2 = gr.Slider(0.0, 1.0, value=0.95, step=0.01, label="Sağ Sınır (x2)")
                        s_y2 = gr.Slider(0.0, 1.0, value=0.35, step=0.01, label="Alt Sınır (y2)")
                        s_zoom = gr.Slider(1.0, 3.0, value=2.0, step=0.5, label="Piksel Keskin Yakınlaştırma (Zoom)")
                        btn_crop = gr.Button("✂️ Varakları Ayır ve 1:1 Kesit Al", variant="primary")
                with gr.Row():
                    out_r = gr.Image(label="Sağ Varak (Önce Okunur — a yüzü)")
                    out_l = gr.Image(label="Sol Varak (Sonra Okunur — b yüzü)")
                out_crop = gr.Image(label="1:1 Piksel Kanıt Kesiti")
                btn_crop.click(
                    split_and_crop,
                    inputs=[in_img, s_x1, s_y1, s_x2, s_y2, s_zoom],
                    outputs=[out_r, out_l, out_crop],
                )

            with gr.Tab("📦 Kurulum, Metodoloji & Tam Rehber"):
                gr.Markdown(readme_text)

        gr.HTML(
            """
            <div style="text-align: center; margin-top: 18px; padding: 14px; background: #faf7f0; border: 1px solid #e2dac9; border-radius: 10px;">
              <strong>Projeyi faydalı buldunuz mu?</strong> Açık kaynaklı Osmanlı arşivi ve dijital beşerî bilimler AI araçlarının gelişimine katkıda bulunmak için:
              <a href="https://buymeacoffee.com/shnfatih8" target="_blank" style="margin-left:8px; font-weight:700; color:#7a5200;">☕ Buy Me a Coffee (shnfatih8)</a> •
              <a href="https://github.com/sponsors/shnfatih-hash" target="_blank" style="margin-left:6px; font-weight:700; color:#b82578;">💖 GitHub Sponsors</a>
            </div>
            """
        )
    return demo


if __name__ == "__main__":
    app = build_ui()
    app.launch()
