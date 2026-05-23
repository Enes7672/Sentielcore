import asyncio
from confing import confing
from yoneticiler.yonetici import Yonetici


async def main():
    cfg = confing()
    print(f'Nexus hedef: {cfg.nexus_host}:{cfg.nexus_port}')
    yon = Yonetici(cfg)
    await yon.yonet()


if __name__ == '__main__':
    asyncio.run(main())
