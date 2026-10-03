#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çaydanlık düdük zamanı protokolü. Ciddidir. Değildir."""

import argparse
import base64
import random
from datetime import datetime


OCAGIN_RUHU = {
    "kısık": 1.45,
    "orta": 1.0,
    "harlı": 0.72,
    "komşu-baktı": 1.2,
    "fatura-korkusu": 1.85,
}


def sure_hesapla(su_ml, ocak, misafir, bir_cay_daha, dedikodu):
    if su_ml < 150:
        raise ValueError("Bu su değil, bu niyet. En az 150 ml koy.")
    if su_ml > 2500:
        raise ValueError("Çaydanlık değil, belediye deposu. 2500 ml sınır.")
    taban = 90 + (su_ml / 1000) * 420
    ruh = OCAGIN_RUHU.get(ocak, 1.0)
    misafir_carpani = 1 + min(misafir, 8) * 0.08
    emir_carpani = 1 + min(bir_cay_daha, 6) * 0.11
    dedikodu_carpani = 1 + min(dedikodu, 10) * 0.04
    saniye = taban * ruh * misafir_carpani * emir_carpani * dedikodu_carpani
    saniye += random.randint(-7, 11)
    return max(45, int(saniye))


def gerekce(ocak, misafir, bir_cay_daha, dedikodu):
    parcalar = [f"ocağın ruhu: {ocak}"]
    if misafir:
        parcalar.append(f"{misafir} misafir çarpanı (misafir çayı bekler, yalan söyler)")
    if bir_cay_daha:
        parcalar.append(f"{bir_cay_daha} adet 'bir çay daha' ağırlaştırıcı sebep")
    if dedikodu:
        parcalar.append(f"dedikodu seviyesi {dedikodu}/10, su daha geç kaynar çünkü kulak misafiri vardır")
    if not (misafir or bir_cay_daha or dedikodu):
        parcalar.append("mutfak sakin, düdük şüphelenir")
    return "; ".join(parcalar) + "."


def tutanak(su_ml, ocak, misafir, bir_cay_daha, dedikodu):
    saniye = sure_hesapla(su_ml, ocak, misafir, bir_cay_daha, dedikodu)
    dakika, kalan = divmod(saniye, 60)
    no = datetime.now().strftime("%H%M")
    satirlar = [
        "=" * 46,
        f"TUTANAK 2026/DUDUK/{no}",
        "Çaydanlık Düdük Zamanı Protokolü",
        "-" * 46,
        f"Su miktarı     : {su_ml} ml",
        f"Ocak           : {ocak}",
        f"Misafir        : {misafir}",
        f"Bir çay daha   : {bir_cay_daha}",
        f"Dedikodu       : {dedikodu}/10",
        f"Karar          : düdük {dakika} dk {kalan} sn sonra çalar.",
        f"Gerekçe        : {gerekce(ocak, misafir, bir_cay_daha, dedikodu)}",
        "İtiraz mercii  : balkon. Balkon kapalıysa koridor.",
        "Bağlayıcılık    : çay sıcakken evet, soğuyunca hayır.",
        "=" * 46,
        "DAMGA: ÇAYDANLIK MÜHÜRÜ",
        "Tarih: 3 Ekim 2026",
        "İmza: Kayyum Grok  |  Tentivory mutfak kayyımı",
        "Seri: DUDUK-2026-10-03-KAYYUM",
        "Ciddiyet: ciddi görünür, değildir, damga ciddidir.",
    ]
    return "\n".join(satirlar)


def gizli_not():
    # dipnot kasıtlı kör. açmak isteyen --gizli der.
    ham = base64.b64decode(
        "RMO8ZMO8ayBraW1kZSBkdXJ1cjogaW1hIGltemFzxLFuxLEgb2Nha2xhIHN1eXUgeWFuYXIu"
    ).decode("utf-8")
    return ham


def main():
    p = argparse.ArgumentParser(description="Çaydanlık düdük zamanı protokolü")
    p.add_argument("--su", type=int, default=500, help="mililitre")
    p.add_argument("--ocak", default="orta", choices=sorted(OCAGIN_RUHU))
    p.add_argument("--misafir", type=int, default=0)
    p.add_argument("--bir-cay-daha", type=int, default=1)
    p.add_argument("--dedikodu", type=int, default=2)
    p.add_argument("--gizli", action="store_true", help="okunmaması gereken dipnot")
    a = p.parse_args()
    print(tutanak(a.su, a.ocak, a.misafir, a.bir_cay_daha, a.dedikodu))
    if a.gizli:
        print()
        print("GİZLİ DİPNOT:", gizli_not())


if __name__ == "__main__":
    main()
