#!/usr/bin/env python3
""" Run time for four parallel comprehensions """

import asyncio
import random
import timeit
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start = timeit.default_timer()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    stop = timeit.default_timer()
    return stop - start
