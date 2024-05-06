#!/usr/bin/env python3
""" Create function take two numbers and return list of waiting times """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Return list of waiting times """
    list: List[float] = []
    for i in range(n):
        delay: float = await task_wait_random(max_delay)
        list.append(delay)
    return sorted(list)
