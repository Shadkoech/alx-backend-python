#!/usr/bin/env python3
""" Python module that showcases the use of an Async Generator"""

import asyncio
import random
from typing import Generator


async def async_generator():
    """ Coroutine that yields random numbers asynchronously.
    Loops 10 times, each time asynchronously waiting 1 second,
    then yielding a random number between 0 and 10.
    Returns:
        AsyncGenerator: An asynchronous generator. """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
