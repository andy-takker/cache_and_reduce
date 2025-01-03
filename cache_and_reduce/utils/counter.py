import abc
import time
from collections import defaultdict
from collections.abc import Awaitable, Callable
from functools import wraps
from typing import Concatenate, ParamSpec, TypeVar


class Counter:
    def __init__(self) -> None:
        self._count = 0
        self._total_time = 0.0

    @property
    def count(self) -> int:
        return self._count

    @property
    def total_time(self) -> float:
        return self._total_time

    def add_count(self) -> None:
        self._count += 1

    def add_time(self, result_time: float) -> None:
        self._total_time += result_time


class ICountered(abc.ABC):
    _counter: defaultdict[str, Counter]

    def calculate_total_time(self) -> None:
        total_time = 0.0
        for counter in self._counter.values():
            total_time += counter.total_time
        print("Total execution time:", total_time)

    def calculate_total_count(self) -> None:
        total_count = 0
        for counter in self._counter.values():
            total_count += counter.count
        print("Total execution count:", total_count)


P = ParamSpec("P")
RT = TypeVar("RT")


def countered(key_func: Callable[..., str] | None = None) -> Callable:
    def decorator(
        func: Callable[Concatenate[ICountered, P], Awaitable[RT]],
    ) -> Callable[Concatenate[ICountered, P], Awaitable[RT]]:
        @wraps(func)
        async def wrapped(self: ICountered, *args: P.args, **kwargs: P.kwargs) -> RT:
            key = (
                key_func(*args, **kwargs)
                if key_func
                else f"{self.__class__.__name__}:{func.__name__}:{args}:{kwargs}"
            )
            start_time = time.monotonic()
            result = await func(self, *args, **kwargs)
            end_time = time.monotonic()
            self._counter[key].add_count()
            self._counter[key].add_time(end_time - start_time)
            return result

        return wrapped

    return decorator
