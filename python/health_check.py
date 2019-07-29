#!/usr/bin/env python3

import asyncio
from aiohttp import ClientSession
import time

async def fetch_head(url, session):
    async with session.head(url) as response:
        return (url, response.status)

async def fetch(url, session):
    async with session.get(url) as response:
        return (url, response.status)

async def run(urls):
    tasks = []

    async with ClientSession() as session:
        for url in urls:
            tasks.append(fetch_head(url, session))

        responses = await asyncio.gather(*tasks)

        for url, status in responses:
            print("URL:", url, "Status:", status)


urls = ["http://www.google.com"] * 50

start_time = time.time()
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(urls))
loop.run_until_complete(future)
print("Health check took", time.time() - start_time, "seconds to run")
