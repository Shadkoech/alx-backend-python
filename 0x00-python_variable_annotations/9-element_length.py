#!/usr/bin/env python3
"""
Module that performes annotation """

import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """function that returns a list of tuples containing elements
    and their lengths."""

    return [(i, len(i)) for i in lst]
