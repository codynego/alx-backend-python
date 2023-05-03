#!/usr/bin/env python3

"""
async comprehension
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async comprehension

    Returns:
        returns a list of random number
    """
    rand_num = [num async for num in async_generator()]
    return rand_num
