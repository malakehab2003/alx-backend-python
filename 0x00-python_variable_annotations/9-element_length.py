#!/usr/bin/env python3
""" Implement element_length to return len of elements in list """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element_length take list and return each element with its size """
    return [(i, len(i)) for i in lst]
