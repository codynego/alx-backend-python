#!/usr/bin/env python3

"""
a function that takes a list and return its sum
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    a function that takes a list and return its sum

    Args:
        input_list: (list) - a list of floats

    Return:
        returns the sum of the list
    """
    list_sum: float = 0
    for i in input_list:
        list_sum += i
    return (list_sum)
