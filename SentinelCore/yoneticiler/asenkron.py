import asyncio
from services.raporla import raporla


async def asenkron_raporlama(veri_listesi, dosya_yolu='raporlar.txt'):
    print('asenkron raporlama islemi basladi')
    raporla(veri_listesi, dosya_yolu)
    await asyncio.sleep(1)
    print('asenkron raporlama islemi tamamlandi')
