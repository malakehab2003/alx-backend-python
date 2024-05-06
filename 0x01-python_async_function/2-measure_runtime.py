#!/usr/bin/env python3
""" Create a function to sum the total wait """
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Run wait_n function and return the sum of the waiting time """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total = end - start
    return float(total / n)
