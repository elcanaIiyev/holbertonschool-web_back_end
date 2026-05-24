#!/usr/bin/env python3
"""
Module that provides a type-annotated function to calculate the floor.
"""
import math


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    Args:
        n (float): The floating-point number to find the floor of.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
