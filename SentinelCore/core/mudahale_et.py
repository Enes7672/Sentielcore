def mudahale_et(data, dosya_yolu='raporlar.txt'):
    with open(dosya_yolu, 'a') as f:
        f.write(f"[MUDAHALE] Tehlike: {data}\n")
    print(f"[MUDAHALE] Veri engellendi ve kaydedildi: {data.get('ham_veri', data)}")
