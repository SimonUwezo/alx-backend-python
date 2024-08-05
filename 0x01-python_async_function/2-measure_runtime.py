#!/usr/bin/env python3
"""Function that measures elapsed time from async functions"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Module that measures appropriate elapsed time"""

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    elapsed = end - start
    return elapsed / n
