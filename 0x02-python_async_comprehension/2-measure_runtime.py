#!/usr/bin/env python3
""" Run time for four parallel comprehensions """

import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure total runtime of async_comprehension() 4 times in parallel
    Returns
    -------
    float
        total runtime in seconds
    """
    start = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end = time()
    return (end - start)
