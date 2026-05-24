#!/usr/bin/env python3
"""
Module that provides a type-annotated function to create a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of a number.

    Args:
        k (str): The string key.
        v (Union[int, float]): The number to square (int or float).

    Returns:
        Tuple[str, float]: A tuple where the first element is k and
        the second element is the square of v as a float.
    """
    return (k, float(v**2))
