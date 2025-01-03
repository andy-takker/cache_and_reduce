from collections import defaultdict

from cache_and_reduce.interfaces.bar_client import IBarClient
from cache_and_reduce.utils.counter import Counter, ICountered, countered


class CounteredBarClient(ICountered, IBarClient):
    def __init__(self, bar_client: IBarClient) -> None:
        self._client = bar_client
        self._counter = defaultdict(Counter)

    @countered()
    async def get_bar(self, foo_id: int, bar_id: int) -> str:
        return await self._client.get_bar(foo_id=foo_id, bar_id=bar_id)
