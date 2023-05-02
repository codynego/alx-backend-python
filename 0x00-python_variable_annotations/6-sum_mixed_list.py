#!/usr/bin/env python3

"""
a function that takes a mix of integars and float
and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    a function that takes a mix of integars and float
    and returns their sum as a float

    Args:
        mxd_lst: (list) - a list of floats and integers

    Return:
        returns the sum of the list
    """
    sum_list = 0
    for i in mxd_lst:
        sum_list += i
    return (sum_list)
