#!/usr/bin/env python3

"""
a function that takes a mix of integars and float
and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    sum_list = 0
    for i in mxd_lst:
        sum_list += i
    return (sum_list)
