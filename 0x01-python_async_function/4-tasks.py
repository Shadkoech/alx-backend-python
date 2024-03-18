#!/usr/bin/env python3
"""
Python module that orchestrates the basics of async concept """

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that generates tasks using task_wait_random n times
    with specified max_delay.
    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay in seconds (inclusive).
    Returns:
        List[float]: List of all the delays in ascending order.
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delay = [await task for task in asyncio.as_completed(tasks)]
    return delay
