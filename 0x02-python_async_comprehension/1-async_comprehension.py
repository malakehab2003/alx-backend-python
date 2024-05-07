#!/usr/bin/env python3
""" Create async function """
import typing


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """ return list of generated numbers """
    return [num async for num in async_generator()]
