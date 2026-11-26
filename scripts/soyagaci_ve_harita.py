#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
soyagaci_ve_harita.py — GEDCOM İçe Aktarma, Kuşak Doğrulama ve İnteraktif HTML Göç Haritası Üretici
====================================================================================================
Sıfır dış Python bağımlılığı (yalnızca Python 3 standart kütüphanesi) ile çalışır.

Kullanım:
  1) GEDCOM (.ged) dosyasını standart JSON'a çevirme:
     python scripts/soyagaci_ve_harita.py import-gedcom aile.ged --out familytree.json

  2) Kuşak ve yaş tutarlılığını denetleme:
     python scripts/soyagaci_ve_harita.py validate familytree.json

  3) İnteraktif HTML Göç Haritası ve Zaman Çizelgesi üretme:
     python scripts/soyagaci_ve_harita.py render-map examples/ornek_aile_verisi.json --out goc_haritasi.html
"""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path


YEAR_RE = re.compile(r"\b(1[4-9]\d{2}|20\d{2})\b")


def esc(text: str | None) -> str:
    return html.escape(str(text or ""), quote=True)


def extract_year(val: str | int | None) -> int | None:
    if val is None:
        return None
    if isinstance(val, int):
        return val
    m = YEAR_RE.search(str(val))
    return int(m.group(1)) if m else None


def parse_gedcom(ged_text: str) -> dict:
    """MyHeritage / Ancestry / FamilySearch GEDCOM (.ged) dosyasını standart familytree.json şemasına çevirir."""
    individuals: dict[str, dict] = {}
    families: dict[str, dict] = {}
    cur_rec: dict | None = None
    cur_type: str | None = None
    cur_event: str | None = None

    for raw in ged_text.splitlines():
        line = raw.strip()
        if not line:
            continue
        parts = line.split(" ", 2)
        level = int(parts[0])
        tag_or_id = parts[1] if len(parts) > 1 else ""
        val = parts[2].strip() if len(parts) > 2 else ""

        if level == 0:
            cur_event = None
            if tag_or_id.startswith("@") and val in ("INDI", "FAM"):
                cur_type = val
                cur_rec = {"id": tag_or_id}
                if val == "INDI":
                    individuals[tag_or_id] = cur_rec
                else:
                    families[tag_or_id] = cur_rec
            else:
                cur_rec = None
                cur_type = None
            continue

        if cur_rec is None:
            continue

        if cur_type == "INDI":
            if level == 1:
                cur_event = tag_or_id
                if tag_or_id == "NAME":
                    cur_rec["ad"] = val.replace("/", "").strip()
                elif tag_or_id == "SEX":
                    cur_rec["cinsiyet"] = val
            elif level == 2 and cur_event == "BIRT":
                if tag_or_id == "DATE":
                    cur_rec["dogum_yili"] = extract_year(val)
                    cur_rec["dogum_tarihi"] = val
                elif tag_or_id == "PLAC":
                    cur_rec["dogum_yeri"] = val
            elif level == 2 and cur_event == "DEAT":
                if tag_or_id == "DATE":
                    cur_rec["olum_yili"] = extract_year(val)
        elif cur_type == "FAM" and level == 1:
            if tag_or_id == "HUSB":
                cur_rec["baba_id"] = val
            elif tag_or_id == "WIFE":
                cur_rec["anne_id"] = val
            elif tag_or_id == "CHIL":
                cur_rec.setdefault("cocuklar", []).append(val)

    for fam in families.values():
        baba = fam.get("baba_id")
        anne = fam.get("anne_id")
        for cid in fam.get("cocuklar", []):
            if cid in individuals:
                if baba:
                    individuals[cid]["baba_id"] = baba
                if anne:
                    individuals[cid]["anne_id"] = anne

    kisiler = []
    for ind in individuals.values():
        kisiler.append({
            "id": ind["id"],
            "ad": ind.get("ad", "Bilinmeyen"),
            "dogum_yili": ind.get("dogum_yili"),
            "dogum_yeri": ind.get("dogum_yeri", ""),
            "baba_id": ind.get("baba_id"),
            "anne_id": ind.get("anne_id"),
            "kanit": "KESİN KANIT",
        })

    return {
        "baslik": "GEDCOM İçe Aktarılan Aile Soy Ağacı",
        "not": "Kişisel veriler yerel makinede tutulur; dış aramalarda yalnızca yer ve yıl kullanılır.",
        "kisiler": kisiler,
        "yerler": [],
        "rotalar": [],
        "olaylar": [],
    }


def validate_tree(data: dict) -> list[str]:
    """Ebeveyn-çocuk yaş farkı ve bağlantı tutarlılığını kontrol eder."""
    warnings: list[str] = []
    kisiler = data.get("kisiler", [])
    by_id = {k.get("id"): k for k in kisiler if k.get("id")}

    for k in kisiler:
        kid = k.get("id", "?")
        ad = k.get("ad", kid)
        cy = extract_year(k.get("dogum_yili"))
        for role_key, role_label in (("baba_id", "Baba"), ("anne_id", "Anne")):
            pid = k.get(role_key)
            if not pid:
                continue
            if pid not in by_id:
                warnings.append(f"[HATA] {ad} ({kid}) için {role_label} kaydı bulunamadı: {pid}")
                continue
            py = extract_year(by_id[pid].get("dogum_yili"))
            if cy is not None and py is not None:
                diff = cy - py
                if diff < 13:
                    warnings.append(f"[UYARI] {ad} ({cy}) ile {role_label} {by_id[pid].get('ad')} ({py}) yaş farkı çok küçük: {diff} yıl (kütük yuvarlama/hata kontrolü önerilir).")
                elif diff > 65:
                    warnings.append(f"[UYARI] {ad} ({cy}) ile {role_label} {by_id[pid].get('ad')} ({py}) yaş farkı yüksek: {diff} yıl (arada eksik kuşak olabilir).")
    return warnings


def build_map_html(data: dict) -> str:
    title = data.get("baslik", "Aile Göç Haritası ve Soy Kütüğü Zaman Çizelgesi")
    alt_baslik = data.get("alt_baslik", "Birincil Osmanlı Arşivleri & Sözlü Tarih Katmanlı İnteraktif Rapor")
    kisiler = data.get("kisiler", [])
    yerler = data.get("yerler", [])
    rotalar = data.get("rotalar", [])
    olaylar = data.get("olaylar", [])

    badge_colors = {
        "KESİN KANIT": "#166534",
        "GÜÇLÜ EŞLEŞME": "#92400e",
        "İSİM / SÜLALE İZİ": "#475569",
        "BÖLGESEL GÖÇ BAĞLAMI": "#1e40af",
        "AİLE ANLATISI": "#7c2d12",
    }

    def badge_html(level: str) -> str:
        lv = (level or "KESİN KANIT").upper()
        col = badge_colors.get(lv, "#334155")
        return f'<span class="ev-badge" style="background:{col};">{esc(lv)}</span>'

    person_rows = ""
    for k in sorted(kisiler, key=lambda x: extract_year(x.get("dogum_yili")) or 9999):
        person_rows += f"""
        <tr>
          <td><strong>{esc(k.get('ad'))}</strong><br><span class="muted">{esc(k.get('kol', ''))}</span></td>
          <td>{esc(k.get('dogum_yili', '—'))}</td>
          <td>{esc(k.get('dogum_yeri', '—'))}</td>
          <td>{badge_html(k.get('kanit', 'KESİN KANIT'))}</td>
          <td>{esc(k.get('kaynak', '—'))}</td>
        </tr>
        """

    timeline_cards = ""
    for ev in sorted(olaylar, key=lambda x: extract_year(x.get("yil")) or 9999):
        timeline_cards += f"""
        <div class="tl-item">
          <div class="tl-year">{esc(ev.get('yil'))}</div>
          <div class="tl-body">
            <div class="tl-head"><strong>{esc(ev.get('baslik'))}</strong> {badge_html(ev.get('kanit', 'KESİN KANIT'))}</div>
            <p>{esc(ev.get('aciklama'))}</p>
            {f'<div class="muted">Kaynak: {esc(ev.get("kaynak"))}</div>' if ev.get("kaynak") else ''}
          </div>
        </div>
        """

    places_json = json.dumps(yerler, ensure_ascii=False)
    routes_json = json.dumps(rotalar, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin="">
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>
<style>
  :root {{ --bg:#f7f4ec; --card:#fff; --ink:#1d242b; --muted:#5a6570; --navy:#1b2838; --gold:#9a6b2f; --border:#dfd7c6; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; font-family:"Segoe UI",system-ui,sans-serif; background:var(--bg); color:var(--ink); line-height:1.6; }}
  header {{ background:linear-gradient(135deg,#1b2838,#2b3e50); color:#fff; padding:24px 20px; border-bottom:4px solid #ffdd00; }}
  .wrap {{ max-width:1120px; margin:0 auto; padding:0 16px; }}
  header h1 {{ margin:0 0 6px; font-family:Georgia,serif; font-size:1.6rem; }}
  header p {{ margin:0; opacity:.9; font-size:.94rem; }}
  .card {{ background:var(--card); border:1px solid var(--border); border-radius:12px; padding:18px 20px; margin:16px 0; }}
  #map {{ height:440px; width:100%; border-radius:10px; border:1px solid var(--border); }}
  table {{ width:100%; border-collapse:collapse; font-size:.92rem; }}
  th,td {{ padding:9px 10px; border-bottom:1px solid var(--border); text-align:left; vertical-align:top; }}
  th {{ background:#f3ede0; }}
  .ev-badge {{ display:inline-block; color:#fff; padding:2px 8px; border-radius:99px; font-size:.74rem; font-weight:700; letter-spacing:.02em; }}
  .muted {{ color:var(--muted); font-size:.85rem; }}
  .tl-item {{ display:flex; gap:14px; padding:12px 0; border-bottom:1px solid var(--border); }}
  .tl-year {{ min-width:86px; font-weight:800; color:var(--navy); font-family:Georgia,serif; font-size:1.05rem; }}
  .tl-body p {{ margin:5px 0 4px; }}
  .tl-head {{ display:flex; flex-wrap:wrap; gap:8px; align-items:center; }}
</style>
</head>
<body>
<header>
  <div class="wrap">
    <h1>🗺️ {esc(title)}</h1>
    <p>{esc(alt_baslik)}</p>
  </div>
</header>
<main class="wrap">
  <section class="card">
    <h2 style="margin-top:0;color:var(--navy);">1. İnteraktif Göç Haritası</h2>
    <p class="muted">Noktalı çizgiler arşiv veya sözlü tarihle tespit edilen temsilî göç güzergâhlarını gösterir. İşaretlere tıklayarak dönem notlarını görebilirsiniz.</p>
    <div id="map"></div>
  </section>

  <section class="card">
    <h2 style="margin-top:0;color:var(--navy);">2. Kuşak ve Kanıt Seviyesi Tablosu ({len(kisiler)} Kişi)</h2>
    <table>
      <thead><tr><th>Ad / Kol</th><th>Doğum Yılı</th><th>Doğum Yeri</th><th>Kanıt Seviyesi</th><th>Arşiv / Kaynak</th></tr></thead>
      <tbody>{person_rows or '<tr><td colspan="5">Kişi kaydı bulunamadı.</td></tr>'}</tbody>
    </table>
  </section>

  <section class="card">
    <h2 style="margin-top:0;color:var(--navy);">3. Tarihsel Olaylar &amp; Aile Göç Zaman Çizelgesi</h2>
    {timeline_cards or '<p class="muted">Zaman çizelgesi olayı eklenmemiş.</p>'}
  </section>
</main>
<script>
const PLACES = {places_json};
const ROUTES = {routes_json};
const map = L.map('map').setView([39.5, 32.0], 5);
L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
  maxZoom: 18,
  attribution: '&copy; OpenStreetMap'
}}).addTo(map);

const bounds = [];
const placeById = {{}};
PLACES.forEach(p => {{
  placeById[p.id] = p;
  if (typeof p.lat === 'number' && typeof p.lon === 'number') {{
    bounds.push([p.lat, p.lon]);
    const mk = L.circleMarker([p.lat, p.lon], {{
      radius: 8, color: '#1b2838', weight: 2, fillColor: p.renk || '#d97706', fillOpacity: 0.9
    }}).addTo(map);
    mk.bindPopup(`<strong>${{p.ad}}</strong><br><em>${{p.donem || ''}}</em><br>${{p.not || ''}}`);
  }}
}});

ROUTES.forEach(r => {{
  const a = placeById[r.from], b = placeById[r.to];
  if (a && b) {{
    L.polyline([[a.lat, a.lon], [b.lat, b.lon]], {{
      color: r.renk || '#1d4e89', weight: 3, dashArray: '8, 7', opacity: 0.85
    }}).addTo(map).bindPopup(`<strong>${{r.etiket || ''}}</strong><br>${{r.yil || ''}} (${{r.kanit || ''}})`);
  }}
}});

if (bounds.length > 0) map.fitBounds(bounds, {{ padding: [40, 40] }});
</script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="GEDCOM içe aktarma, kuşak doğrulama ve İnteraktif HTML Göç Haritası aracı.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ged = sub.add_parser("import-gedcom", help="GEDCOM (.ged) dosyasını familytree.json şemasına çevirir.")
    p_ged.add_argument("input_ged", help="Kaynak .ged dosyası")
    p_ged.add_argument("--out", default="familytree.json", help="Çıktı JSON dosyası")

    p_val = sub.add_parser("validate", help="familytree.json kuşak ve yaş tutarlılığını denetler.")
    p_val.add_argument("input_json", help="Doğrulanacak JSON dosyası")

    p_map = sub.add_parser("render-map", help="JSON verisinden tek dosyalık İnteraktif HTML Göç Haritası üretir.")
    p_map.add_argument("input_json", help="Aile ve göç rotası JSON dosyası")
    p_map.add_argument("--out", default="goc_haritasi_ve_rapor.html", help="Çıktı HTML dosyası")

    args = parser.parse_args()
    if args.cmd == "import-gedcom":
        text = Path(args.input_ged).read_text(encoding="utf-8", errors="replace")
        data = parse_gedcom(text)
        out = Path(args.out).resolve()
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"GEDCOM içe aktarıldı ({len(data['kisiler'])} kişi): {out}")
    elif args.cmd == "validate":
        data = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
        issues = validate_tree(data)
        if not issues:
            print("OK: Kuşak bağlantıları ve yaş farkları tutarlı.")
        else:
            for item in issues:
                print(item)
    elif args.cmd == "render-map":
        data = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
        out = Path(args.out).resolve()
        out.write_text(build_map_html(data), encoding="utf-8")
        print(f"İnteraktif HTML Göç Haritası oluşturuldu: {out}")


if __name__ == "__main__":
    main()
