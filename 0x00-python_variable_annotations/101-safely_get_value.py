#!/usr/bin/env python3
""" Add type annotations to a function """
from typing import Union, Any, Mapping, TypeVar


T = TypeVar('T')
r = Union[Any, T]
d = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: d = None) -> r:
    """ Implement annotations to this function """
    if key in dct:
        return dct[key]
    else:
        return default
