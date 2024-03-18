#!/usr/bin/env python3
"""
Python module that orchestrates the basics of async concept """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine spawning wait_random n times with specified max_delay.
    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay in seconds (inclusive).
    Returns:
        List[float]: List of all the delays in ascending order.
    """

    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Gather the results without sorting and append them to list delay
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
