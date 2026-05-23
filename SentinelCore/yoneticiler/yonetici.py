from core.anlik_izleme import AnlikIzleme


class Yonetici:
    def __init__(self, config):
        self.config = config
        self.izleyici = AnlikIzleme(config)

    async def yonet(self):
        print('yonetici calisiyor')
        await self.izleyici.baslat()
