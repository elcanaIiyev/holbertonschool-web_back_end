#!/usr/bin/env python3
"""
This module provides a function for parallel comprehensions.
"""
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function will execute async_comprehension 4 times in parallel
    using asyncio.gather and return the total run time.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
