#!/usr/bin/env python3
"""
Python module that showcases complex type annotation """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Type-annotated function that returns the sum of
    a mixed list """

    return sum(mxd_lst)
