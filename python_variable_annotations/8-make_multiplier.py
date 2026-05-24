#!/usr/bin/env python3
"""
Module that provides a function that returns a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns a float.
    """
    def multiply(n: float) -> float:
        """ Returns the product of n and multiplier """
        return n * multiplier

    return multiply
