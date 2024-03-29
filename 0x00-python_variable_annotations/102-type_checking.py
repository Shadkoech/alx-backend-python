#!/usr/bin/env python3
"""
Module that showcases the appication of mypy to make any
necessary changes """

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Function that Zooms in on the elements of the input
    tuple by replicating each element a specified number of times"""

    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
