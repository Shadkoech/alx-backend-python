#!/usr/bin/env python3
"""
Python module that showcases complex type annotation """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function that returns a function that
    multiplies a float by the given multiplier."""

    def multiplier_function(x: float) -> float:
        """Function returning float multiplier """
        return x * multiplier
    return multiplier_function
