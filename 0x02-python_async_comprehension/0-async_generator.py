#!/usr/bin/env python3

"""
Async Generator
"""

import asyncio
import random


async def async_generator():
    """
    a coroutine that loops 10 times wait for 1 seconds
    and yield a random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)