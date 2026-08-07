#!/usr/bin/env python3
"""
This module provides async_comprehension function.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This function takes no argument and collects 10 random numbers using
    async comprehesing over async_generator, returns 10 random numbers.
    """
    result = [i async for i in async_generator()]
    return result
