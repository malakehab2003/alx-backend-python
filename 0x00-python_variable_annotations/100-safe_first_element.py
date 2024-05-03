#!/usr/bin/env python3
""" Augment safe_first_element function """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ function return the first element of list """
    if lst:
        return lst[0]
    else:
        return None
