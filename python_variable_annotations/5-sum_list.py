#!/usr/bin/env python3
"""
Module that provides a type-annotated function to sum a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list containing float numbers.

    Returns:
        float: The sum of the elements in input_list.
    """
    return sum(input_list)
