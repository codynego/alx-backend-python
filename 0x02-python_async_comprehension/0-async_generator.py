#!/usr/bin/env python3

"""
Async Generator
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> None:
    """
    a coroutine that loops 10 times wait for 1 seconds
    and yield a random number

    Returns:
        no returrs
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
