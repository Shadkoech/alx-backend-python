#!/usr/bin/env python3
"""
Python module that showcases basic type annotation """

import math


def floor(n: float) -> int:
    """
    Type-annotated function that takes a float and returns
    the floor of that float """

    result = math.floor(n)

    return result
