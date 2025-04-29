#!/usr/bin/env python3
import math
from typing import Union

"""
This script defines a function to compute the floor of a number.
"""


def floor(n: Union[int, float]) -> int:
    """
    Computes the floor of a number.

    Args:
        n (Union[int, float]): The number to compute the floor of.

    Returns:
        int: The floor of the number.
    """
    return int(math.floor(n))
