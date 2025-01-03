from aiohttp import ClientSession
from yarl import URL

from cache_and_reduce.interfaces.foo_client import IFooClient


class FooClient(IFooClient):
    def __init__(self, session: ClientSession, base_url: URL) -> None:
        self._session = session
        self._base_url = base_url

    async def get_foo(self, foo_id: int) -> str:
        async with self._session.get(
            self._base_url / "foo",
            params={"foo_id": foo_id},
        ) as response:
            return await response.text()
