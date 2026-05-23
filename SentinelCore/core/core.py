import asyncio
from core.analiz_etme import LogAnalyzer
from core.mudahale_et import mudahale_et
from yoneticiler.asenkron import asenkron_raporlama


async def core_islemi(data, config):
    print('core islemi basladi')

    analyzer = LogAnalyzer(keywords=config.analiz_kritik_kelime)
    sonuc = analyzer.analiz_et(data)

    rapor = {
        'ham_veri': data,
        'log_analizi': sonuc
    }

    print(f'core islemi icin alinan veri: {data}')

    if sonuc['durum'] == 'TEHLIKE':
        mudahale_et(rapor, config.raporlama_dosyasi)
        asyncio.create_task(asenkron_raporlama([rapor], config.raporlama_dosyasi))

    print('core islemi tamamlandi')
    return rapor
