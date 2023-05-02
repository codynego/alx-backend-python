#!/usr/bin/env python3


"""
execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List, Union
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[Union[int, float]]:
    """
    Spawns `n` instances of `wait_random` with the specified
    `max_delay` and returns a sorted list
    of the resulting delays.

    Args:
        n: The number of times to spawn `task_wait_random`.
        max_delay: The maximum delay value to use for each
        `wait_random` instance.

    Returns:
        A sorted list of the resulting delays (float values).
    """
    # Create a list to hold the delay values
    delays: Union[int, float] = []

    # Create a list to hold the coroutines for wait_random
    tasks: Union[int, float] = [task_wait_random(max_delay) for _ in range(n)]

    # Use asyncio.gather() to run all the task concurrently
    results = await asyncio.gather(*tasks)

    # Sort the resulting delay values in ascending order
    delays = sorted(results)

    # Return the sorted list of delays
    return (delays)
