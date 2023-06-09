#!/usr/bin/env python3

"""
a function that calls another function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    """
    a function that calls another function

    Args:
        multiplier: (float)

    Returns:
        A function
    """

    def inner(n: float) -> float:

        """ multiplies the float with the multiplier"""

        new_n = n * multiplier

        return new_n
    return inner
