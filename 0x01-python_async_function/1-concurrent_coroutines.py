#!/usr/bin/env python3

import asyncio
from typing import List, Union
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `n` instances of `wait_random` with the specified
    `max_delay` and returns a sorted list
    of the resulting delays.

    Args:
        n: The number of times to spawn `wait_random`.
        max_delay: The maximum delay value to use for each
        `wait_random` instance.

    Returns:
        A sorted list of the resulting delays (float values).
    """
    # Create a list to hold the delay values
    delays: Union[int, float] = []

    # Create a list to hold the coroutines for wait_random
    coroutines: Union[int, float] = [wait_random(max_delay) for _ in range(n)]

    # Use asyncio.gather() to run all the coroutines concurrently
    results = await asyncio.gather(*coroutines)

    # Sort the resulting delay values in ascending order
    delays = sorted(results)

    # Return the sorted list of delays
    return (delays)
