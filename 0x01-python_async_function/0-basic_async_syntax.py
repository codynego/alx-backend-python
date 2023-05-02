#!/usr/bin/env python3

"""
asyncio basic
"""

import asyncio
from typing import Union
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and
    max_delay (inclusive) seconds and returns it.

    Args:
        max_delay: The maximum delay in seconds (inclusive).

    Returns:
        The delay value in seconds.
    """
    delay: Union[int, float] = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
