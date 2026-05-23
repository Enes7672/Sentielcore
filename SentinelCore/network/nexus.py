import asyncio

class Nexus:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.server = None
        self._queue = asyncio.Queue()

    async def connect(self):
        self.server = await asyncio.start_server(
            self._handle_client, self.host, self.port
        )
        print(f"[NEXUS] {self.host}:{self.port} adresinde dinleniyor...")

    async def _handle_client(self, reader, writer):
        addr = writer.get_extra_info('peername')
        print(f"[NEXUS] Baglanti alindi: {addr}")
        try:
            while True:
                data = await reader.readline()
                if not data:
                    break
                await self._queue.put(data.decode().strip())
        finally:
            writer.close()

    async def izle(self) -> str:
        return await self._queue.get()
