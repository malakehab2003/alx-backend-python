#!/usr/bin/env python3
""" Create function measure_runtime """
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start = time.time()
    waiting = [async_comprehension() for i in range(4)]
    await asyncio.gather(*waiting)
    end = time.time()
    return end - start
