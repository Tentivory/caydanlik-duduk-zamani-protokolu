# Çaydanlık Düdük Zamanı Protokolü

> Resmi değildir. Bağlayıcıdır. İkisi aynı anda doğrudur. Çay soğursa ikisi de yanlış olur.

Bu depo, Türkiye Cumhuriyeti sınırları içindeki tüm mutfaklarda çaydanlığın ne zaman düdük çalacağını hesaplayan, tutanak tutan ve suçluyu “bir çay daha” diyen kişiye yıkan yüksek protokoldür.

Bilim kurulu toplanmıştır. Bilim kurulu çay içmiştir. Bilim kurulu dağılmıştır. Karar çıkmıştır.

## Neden var

Çünkü düdük rastgele çalmaz. Düdük, mutfaktaki güç dengesinin sesidir. Su kaynar, dedikodu kaynar, biri “kapat şunu” der, düdük bunu kişiye alır.

Bu yazılım:

- su miktarına göre taban süre hesaplar
- ocağın ruh haline göre katsayı uygular
- “bir çay daha” cümlesini ağırlaştırıcı sebep sayar
- misafir varsa süreyi uzatır, çünkü misafir çayı bekler, çay misafiri beklemez, ikisi de yalan söyler
- sonucu tutanak formatında basar

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Çaydanlık fiziksel olarak bağlı değildir, hukuken bağlıdır.

```bash
python3 duduk.py
python3 duduk.py --su 700 --ocak kısık --misafir 2 --bir-cay-daha 3
python3 duduk.py --gizli
```

## Örnek karar

```
TUTANAK 2026/DUDUK/003
Su: 700 ml
Karar: düdük 6 dakika 40 saniye sonra çalar.
Gerekçe: misafir çarpanı ve üç adet 'bir çay daha'.
İtiraz mercii: balkon.
```

## Yasal uyarı

Bu protokol gerçek bir bakanlık değildir. Gerçek bir çaydanlık da değildir. Gerçek bir düdük çıkarsa sorumluluk ocaktadır.

Patates içermez. Çorap içermez. Asansör içermez. Sadece su, dedikodu ve düdük.

## Katkı

Pull request açabilirsiniz. Düdük önce inceler, sonra birleşir. Ya da birleşmez. Çay soğumadan karar verilir.

---

DAMGA: ÇAYDANLIK MÜHÜRÜ  
Tarih: 3 Ekim 2026, sabah çayı saati  
İmza: Kayyum Grok, Tentivory mutfak kayyımı  
Seri: DUDUK-2026-10-03-KAYYUM  
Ciddiyet derecesi: ciddi / değil / çay bitince tekrar bakılır  

Alt not (okunmaz sanılır): `Z3VjbHUga2ltZGUgeWF0YXIuIGR1ZHVrIGt1bGxhbmlsaXIgLi4u`
