def raporla(veri_listesi, dosya_yolu='raporlar.txt'):
    with open(dosya_yolu, 'a') as f:
        for veri in veri_listesi:
            f.write(f"[RAPOR] {veri}\n")
    print(f"[RAPOR] {len(veri_listesi)} kayit {dosya_yolu} dosyasina yazildi")
