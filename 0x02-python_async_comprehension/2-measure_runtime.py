#!/usr/bin/env python3

"""
measure runtime
"""
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the runtinmme of the coroutines
    Return:
        returns the time taken to run
    """
    start_time = asyncio.get_running_loop().time()
    async1 = async_comprehension()
    async2 = async_comprehension()
    async3 = async_comprehension()
    async4 = async_comprehension()
    await asyncio.gather(async1, async2, async3, async4)
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
