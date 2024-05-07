#!/usr/bin/env python3
""" Create async_generator function """
import random
import typing
import asyncio


async def async_generator() -> typing.Generator[float, None, None]:
    """ Wait one second and yield random number """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
