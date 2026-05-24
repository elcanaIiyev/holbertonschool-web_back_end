#!/usr/bin/env python3
"""
Module that provides a type-annotated function to sum a mixed list.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of mixed numbers.

    Returns:
        float: The sum of the numbers in mxd_lst as a float.
    """
    return float(sum(mxd_lst))
