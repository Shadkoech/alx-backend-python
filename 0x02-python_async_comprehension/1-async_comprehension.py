#!/usr/bin/env python3
""" Python module that showcases the use of an Async Generator"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    Returns:
        list: A list of 10 random numbers."""

    # Collect 10 random numbers using async comprehension over async_generator
    random_numbers = [num async for num in async_generator()]

    return random_numbers
