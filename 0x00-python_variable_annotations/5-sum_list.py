#!/usr/bin/env python3
"""
Python module that showcases complex type annotation """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Type-annotated function that returns the sum of
    floats in the given list """

    return sum(input_list)
