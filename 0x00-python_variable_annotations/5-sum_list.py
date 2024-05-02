#!/usr/bin/env python3
""" Implement sum_list function to take list and return its sum """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sum_list take list of floats and return sum of them as float """
    sum: float = 0.0
    for i in input_list:
        sum += i
    return float(sum)
