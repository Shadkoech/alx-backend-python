#!/usr/bin/env python3
""" Python module that showcases the use of an Async comprehension in
a number of instances """

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine measuring total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.
    Returns:
        float: Total runtime in seconds.
    """

    # Record the starting time
    start_time = time.time()
    # Execute async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = time.time()

    # Calculate the total runtime
    total_runtime = end_time - start_time

    return total_runtime
