#!/usr/bin/env python3
""" Implement make_multiplier return function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make_multiplier take float number and return function """
    return lambda n: n * multiplier
