import asyncio
from network.nexus import Nexus
from core.core import core_islemi


class AnlikIzleme:
    def __init__(self, config):
        self.config = config
        self.nexus = Nexus(config.nexus_host, config.nexus_port)

    async def baslat(self):
        await self.nexus.connect()
        print("[SISTEM] Anlik izleme ve analiz nobeti basladi...")
        try:
            while True:
                data = await self.nexus.izle()
                sonuc = await core_islemi(data, self.config)
                print(f"[RAPOR]: {sonuc}")
        except asyncio.CancelledError:
            print("[SISTEM] Anlik izleme durduruluyor...")
