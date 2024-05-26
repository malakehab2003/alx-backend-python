#!/usr/bin/env python3
""" Create function take number and wait with this number and 0 """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Wait from zero to max_delay n's seconds """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay