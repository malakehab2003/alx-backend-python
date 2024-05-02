#!/usr/bin/env python3
""" Implement to_kv function which returned parameters as tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ to_kv take str and float or int and return tuple """
    return (k, float(v ** 2))
