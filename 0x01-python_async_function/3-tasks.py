#!/usr/bin/env python3
"""
Python module that orchestrates the basics of async concept """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutine with specified max_delay.
    Args:
        max_delay (int): Maximum delay in seconds (inclusive).
    Returns:
        Task[float]: asyncio.Task representing the execution of wait_random.
    """

    return asyncio.create_task(wait_random(max_delay))
