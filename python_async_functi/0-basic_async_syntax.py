#!/usr/bin/env python3
"""Module for asynchronous random wait utilities."""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously waits for a random delay and returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
