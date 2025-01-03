from abc import abstractmethod
from typing import Protocol


class IFooClient(Protocol):
    @abstractmethod
    async def get_foo(self, foo_id: int) -> str: ...
