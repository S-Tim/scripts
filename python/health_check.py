#!/usr/bin/env python3

import asyncio
from aiohttp import ClientSession
import time

async def fetch_head(url, session):
    try:
        async with session.head(url) as response:
            return (url, response.status)
    except:
        print("URL:", url, "not reachable")

async def fetch(url, session):
    try:
        async with session.get(url) as response:
            return (url, response.status)
    except:
        print("URL:", url, "not reachable")

async def run(urls):
    tasks = []

    async with ClientSession() as session:
        for url in urls:
            tasks.append(fetch(url, session))

        responses = await asyncio.gather(*tasks)
        responses = [resp for resp in responses if resp is not None]

        for url, status in responses:
            print("URL:", url, "Status:", status)


urls = ["http://www.googlesdfkasdfljsdflkjssss.com"] * 5
urls += ["http://www.google.com"] * 5

start_time = time.time()
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(urls))
loop.run_until_complete(future)
print("Health check took", time.time() - start_time, "seconds to run")
