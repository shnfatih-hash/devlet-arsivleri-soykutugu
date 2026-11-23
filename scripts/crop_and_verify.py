#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Devlet Arşivleri Soy Kütüğü Becerisi — 1:1 Piksel Kesit ve Varak Ayırma Aracı
=============================================================================
Kullanıcının e-Satış sepetinden indirip klasöre koyduğu .zip veya .jpg/.png
uzantılı Osmanlıca defter görüntülerini:
  1) Otomatik olarak açar ve envanterini çıkarır (`inventory`),
  2) Çift sayfa (varak) taramaları Sağ Varak (`_R`) ve Sol Varak (`_L`) ile
     okunaklı yatay şeritlere (`_top`, `_mid`, `_bot`) ayırır (`split`),
  3) Kritik hane, isim, yaş veya şerh satırlarından 1:1 doğal piksel (veya 2x/3x
     piksel yakınlaştırmalı) kanıt kesiti (`crop`) üretir.

Gereksinim: Python 3.8+ ve Pillow (`pip install Pillow`)
"""

from __future__ import annotations

import argparse
import os
import sys
import zipfile
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Hata: 'Pillow' kütüphanesi kurulu değil. Kurmak için: pip install Pillow")

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp"}

# Zip bombası koruması: tek bir arşivden çıkarılacak en fazla toplam boyut ve dosya sayısı
MAX_ZIP_UNCOMPRESSED_BYTES = 4 * 1024 ** 3  # 4 GB
MAX_ZIP_MEMBERS = 5000


def extract_zips_if_needed(input_dir: Path, extract_root: Path) -> list[Path]:
    """Klasördeki .zip arşivlerini güvenli biçimde açar ve tüm görüntü yollarını döndürür."""
    images: list[Path] = []
    for root, _, files in os.walk(input_dir):
        for fn in sorted(files):
            fpath = Path(root) / fn
            ext = fpath.suffix.lower()
            if ext == ".zip":
                target = extract_root / fpath.stem
                if not target.exists():
                    target.mkdir(parents=True, exist_ok=True)
                    with zipfile.ZipFile(fpath, "r") as zf:
                        members = zf.infolist()
                        total_size = sum(m.file_size for m in members)
                        if len(members) > MAX_ZIP_MEMBERS or total_size > MAX_ZIP_UNCOMPRESSED_BYTES:
                            raise ValueError(
                                f"Arşiv çok büyük ({len(members)} dosya, {total_size} bayt): {fpath.name}"
                            )
                        base = target.resolve()
                        for member in members:
                            # Zip-slip güvenlik kontrolü (dizin sınırı ayırıcıyla birlikte karşılaştırılır)
                            dest = (target / member.filename).resolve()
                            if os.path.commonpath([str(base), str(dest)]) != str(base):
                                raise ValueError(f"Güvensiz zip yolu reddedildi: {member.filename}")
                            zf.extract(member, target)
                for zroot, _, zfiles in os.walk(target):
                    for zfn in sorted(zfiles):
                        zp = Path(zroot) / zfn
                        if zp.suffix.lower() in IMAGE_EXTS:
                            images.append(zp)
            elif ext in IMAGE_EXTS:
                images.append(fpath)

    # Tekrarları koruyarak benzersizleştir
    seen = set()
    unique_imgs = []
    for p in images:
        rp = p.resolve()
        if rp not in seen:
            seen.add(rp)
            unique_imgs.append(p)
    return unique_imgs


def cmd_inventory(args: argparse.Namespace) -> None:
    in_dir = Path(args.input)
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    imgs = extract_zips_if_needed(in_dir, out_dir / "_extracted")
    print(f"Toplam Görüntü Sayısı: {len(imgs)}")
    for idx, p in enumerate(imgs, 1):
        with Image.open(p) as im:
            w, h = im.size
        print(f"[{idx:03d}] {p.name}  ({w}x{h} px)  ->  {p}")


def cmd_split(args: argparse.Namespace) -> None:
    img_path = Path(args.image)
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(img_path) as im:
        im = im.convert("RGB")
        w, h = im.size
        stem = img_path.stem

        # Osmanlı defterlerinde sağ sayfa önce (a yüzü), sol sayfa sonra (b yüzü) okunur.
        halves = [
            ("R", im.crop((int(w * 0.47), 0, w, h))),
            ("L", im.crop((0, 0, int(w * 0.53), h))),
        ]
        for side, sub in halves:
            sw, sh = sub.size
            full_side = out_dir / f"{stem}_{side}_full.jpg"
            sub.save(full_side, quality=92)
            print(f"Kaydedildi: {full_side} ({sw}x{sh})")

            if args.bands:
                bands = [
                    ("1_top", (0, 0, sw, int(sh * 0.37))),
                    ("2_mid", (0, int(sh * 0.31), sw, int(sh * 0.69))),
                    ("3_bot", (0, int(sh * 0.63), sw, sh)),
                ]
                for bname, box in bands:
                    bp = out_dir / f"{stem}_{side}_{bname}.png"
                    sub.crop(box).save(bp)
                    print(f"  Şerit: {bp}")


def cmd_crop(args: argparse.Namespace) -> None:
    img_path = Path(args.image)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    vals = [float(v.strip()) for v in args.box.split(",")]
    if len(vals) != 4:
        sys.exit("Hata: --box parametresi 'x1,y1,x2,y2' formatında 4 sayı olmalıdır (0.0-1.0 oran veya piksel).")

    with Image.open(img_path) as im:
        im = im.convert("RGB")
        w, h = im.size
        if all(0.0 <= v <= 1.0 for v in vals):
            x1, y1, x2, y2 = int(vals[0] * w), int(vals[1] * h), int(vals[2] * w), int(vals[3] * h)
        else:
            x1, y1, x2, y2 = [int(v) for v in vals]

        crop = im.crop((x1, y1, x2, y2))
        if args.zoom and args.zoom > 1:
            resample = Image.Resampling.NEAREST if args.nearest else Image.Resampling.LANCZOS
            crop = crop.resize((int(crop.width * args.zoom), int(crop.height * args.zoom)), resample)

        crop.save(out_path)
        print(f"1:1 Kanıt Kesiti Kaydedildi: {out_path} ({crop.width}x{crop.height} px, kaynak kutu=({x1},{y1},{x2},{y2}))")


def main() -> None:
    parser = argparse.ArgumentParser(description="Osmanlıca arşiv defteri varak ayırma ve 1:1 piksel kesit aracı.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_inv = sub.add_parser("inventory", help="Klasördeki .zip ve görüntü dosyalarını açıp boyutlarıyla listeler.")
    p_inv.add_argument("--input", required=True, help="İndirilen arşiv dosyalarının bulunduğu klasör")
    p_inv.add_argument("--output", required=True, help="Açılan dosyaların ve kesitlerin yazılacağı klasör")
    p_inv.set_defaults(func=cmd_inventory)

    p_spl = sub.add_parser("split", help="Çift varaklı defter pozunu Sağ (R) ve Sol (L) sayfalara ve yatay okuma şeritlerine böler.")
    p_spl.add_argument("--image", required=True, help="Kaynak defter görüntüsü (.jpg/.png)")
    p_spl.add_argument("--output", required=True, help="Çıktı klasörü")
    p_spl.add_argument("--bands", action="store_true", help="Her sayfayı üst/orta/alt 3 okuma şeridine de böl")
    p_spl.set_defaults(func=cmd_split)

    p_crp = sub.add_parser("crop", help="Belirli bir hane veya satırdan 1:1 (veya büyütülmüş) kanıt kesiti alır.")
    p_crp.add_argument("--image", required=True, help="Kaynak görüntü dosyası")
    p_crp.add_argument("--box", required=True, help="'x1,y1,x2,y2' (0.0-1.0 oran veya piksel koordinatı)")
    p_crp.add_argument("--output", required=True, help="Kaydedilecek kesit dosya yolu (.png/.jpg)")
    p_crp.add_argument("--zoom", type=float, default=1.0, help="Büyütme katsayısı (örn. 2.0 veya 3.0)")
    p_crp.add_argument("--nearest", action="store_true", help="Harf noktalarını keskin görmek için piksel (NEAREST) büyütme kullan")
    p_crp.set_defaults(func=cmd_crop)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
