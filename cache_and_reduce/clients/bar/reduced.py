from cache_and_reduce.interfaces.bar_client import IBarClient
from cache_and_reduce.utils.reduce import AsyncReducer, IReduced, reduced


class ReducedBarClient(IReduced, IBarClient):
    def __init__(self, bar_client: IBarClient) -> None:
        self._client = bar_client
        self._reducer = AsyncReducer()

    @reduced()
    async def get_bar(self, foo_id: int, bar_id: int) -> str:
        return await self._client.get_bar(foo_id=foo_id, bar_id=bar_id)
