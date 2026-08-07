#!/usr/bin/env python3
"""Module for task-based concurrent coroutines."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return delays in ascending order."""
    delays = []

    async def add_delay():
        delay = await task_wait_random(max_delay)
        i = 0
        while i < len(delays) and delays[i] < delay:
            i += 1
        delays.insert(i, delay)

    await asyncio.gather(*[add_delay() for _ in range(n)])
    return delays
