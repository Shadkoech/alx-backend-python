#!/usr/bin/env python3
"""
Python module that orchestrates the basics of async concept """

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.
    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay in seconds (inclusive).
    Returns:
        float: Average execution time per call to wait_random.
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time/n)
