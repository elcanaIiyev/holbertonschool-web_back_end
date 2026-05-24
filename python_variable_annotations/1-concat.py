#!/usr/bin/env python3
"""
Module that provides a type-annotated function to concatenate strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the resulting string.

    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The result of concatenating str1 and str2.
    """
    return str1 + str2
