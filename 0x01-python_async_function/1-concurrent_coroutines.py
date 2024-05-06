#!/usr/bin/env python3
""" Create function take two numbers and return list of waiting times """
import asyncio
from typing import List


wait_rdm = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Return list of waiting times """
    list: List[float] = []
    for i in range(n):
        delay: float = await wait_rdm(max_delay)
        list.append(delay)
    return sorted(list)
