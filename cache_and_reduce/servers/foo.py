import asyncio
from collections.abc import AsyncIterator, Callable
from contextlib import asynccontextmanager

from aiohttp import web
from aiohttp.test_utils import TestServer
from yarl import URL

from cache_and_reduce.interfaces.bar_client import IBarClient


def get_foo_route(bar_client: IBarClient) -> Callable:
    async def foo_route(request: web.Request) -> web.Response:
        foo_id = int(request.query.get("foo_id", 0))
        print(f"foo {foo_id}: start request")
        bars = await asyncio.gather(
            *[bar_client.get_bar(foo_id=foo_id, bar_id=i + 1) for i in range(5)]
        )
        print(f"foo {foo_id}: end request")
        return web.Response(text=f"foo {foo_id}: {bars}")

    return foo_route


@asynccontextmanager
async def start_foo_server(bar_client: IBarClient) -> AsyncIterator[URL]:
    main_app = web.Application()
    main_app.add_routes([web.get("/foo", get_foo_route(bar_client))])
    server = TestServer(main_app)
    await server.start_server()
    yield server.make_url("")
    await server.close()
