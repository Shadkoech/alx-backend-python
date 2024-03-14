#!/usr/bin/env python3
"""
Module that performes annotation """

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """function that returns a list of tuples containing elements
    and their lengths."""

    return [(i, len(i)) for i in lst]
