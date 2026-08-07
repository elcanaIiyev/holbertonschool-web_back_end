#!/usr/bin/env python3
"""Module for concurrent coroutines."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return delays in ascending order."""
    delays = []

    async def add_delay():
        delay = await wait_random(max_delay)
        i = 0
        while i < len(delays) and delays[i] < delay:
            i += 1
        delays.insert(i, delay)

    await asyncio.gather(*[add_delay() for _ in range(n)])
    return delays
