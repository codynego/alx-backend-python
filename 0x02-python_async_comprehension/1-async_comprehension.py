#!/usr/bin/env python3

"""
async comprehension
"""

import asyncio


async def async_comprehension() -> List[float]:
    """
    async comprehension

    Returns:
        returns a list of random number
    """
    rand_num = [num async for num in async_generator()]
    return rand_num
