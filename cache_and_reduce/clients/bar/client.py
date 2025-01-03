from aiohttp import ClientSession
from yarl import URL

from cache_and_reduce.interfaces.bar_client import IBarClient


class BarClient(IBarClient):
    def __init__(self, session: ClientSession, base_url: URL) -> None:
        self._base_url = base_url
        self._session = session

    async def get_bar(self, foo_id: int, bar_id: int) -> str:
        async with self._session.get(
            self._base_url / "bar",
            params={"bar_id": bar_id, "foo_id": foo_id},
        ) as response:
            return await response.text()
