import asyncio
import random
import time
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from aiohttp import web
from aiohttp.test_utils import TestServer
from yarl import URL


async def calculate(bar_id: int, foo_id: int) -> str:
    print(f"bar: got request {foo_id} {bar_id}")
    await asyncio.sleep(3 + random.random())
    print(f"bar: end request {foo_id} {bar_id}")
    return f"bar {foo_id} {bar_id}: {time.time()}"


async def bar_route(request: web.Request) -> web.Response:
    bar_id = int(request.query.get("bar_id", 0))
    foo_id = int(request.query.get("foo_id", 0))
    result = await calculate(bar_id, foo_id)
    return web.Response(text=result)


@asynccontextmanager
async def start_bar_server() -> AsyncIterator[URL]:
    data_app = web.Application()
    data_app.add_routes([web.get("/bar", bar_route)])
    server = TestServer(data_app)
    await server.start_server()
    yield server.make_url("")
    await server.close()
