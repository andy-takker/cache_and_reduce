from abc import abstractmethod
from typing import Protocol


class IBarClient(Protocol):
    @abstractmethod
    async def get_bar(self, foo_id: int, bar_id: int) -> str: ...
