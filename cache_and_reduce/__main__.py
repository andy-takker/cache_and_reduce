import asyncio

import aiohttp
from aiocache import Cache

from cache_and_reduce.clients.bar.cached import CachedBarCLient
from cache_and_reduce.clients.bar.client import BarClient
from cache_and_reduce.clients.bar.countered import CounteredBarClient
from cache_and_reduce.clients.bar.reduced import ReducedBarClient
from cache_and_reduce.clients.foo import FooClient
from cache_and_reduce.servers.bar import start_bar_server
from cache_and_reduce.servers.foo import start_foo_server


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        async with start_bar_server() as bar_url:
            bar_client = BarClient(session=session, base_url=bar_url)
            countered_bar_client = CounteredBarClient(bar_client=bar_client)
            reduced_bar_client = ReducedBarClient(bar_client=countered_bar_client)
            cached_bar_client = CachedBarCLient(
                bar_client=reduced_bar_client, cache=Cache()
            )
            async with start_foo_server(cached_bar_client) as foo_url:
                foo_client = FooClient(session=session, base_url=foo_url)
                print("URL:", foo_url)
                foo_ids = [1, 1, 2, 3, 5, 8, 8, 7, 7, 10, 10, 11]
                await asyncio.gather(*[foo_client.get_foo(foo_id=i) for i in foo_ids])
                countered_bar_client.calculate_total_time()
                countered_bar_client.calculate_total_count()
                await asyncio.gather(*[foo_client.get_foo(foo_id=i) for i in foo_ids])
                countered_bar_client.calculate_total_time()
                countered_bar_client.calculate_total_count()


if __name__ == "__main__":
    asyncio.run(main())
