#!/usr/bin/env python3
"""Implement sum_mixed_list to mix ints with floats """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sum_mixed_list take mixed list of float and int and return the sum """
    return float(sum(mxd_lst))
