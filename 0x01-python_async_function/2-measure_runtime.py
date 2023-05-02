#!/usr/bin/env python3

"""
Measure the runtime
"""

import time
import asyncio
from typing import Union, List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for `wait_n(n, max_delay)`,
    and returns total_time / n.

    Args:
        n: The number of times to call `wait_n`.
        max_delay: The maximum delay value to
        use for each `wait_random` instance.

    Returns:
        The average time per call (float).
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
