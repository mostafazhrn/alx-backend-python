#!/usr/bin/env python3
"""This module shall return the values with the correct type annotations"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ This function shall take a sequence and return its first element"""
    if lst:
        return lst[0]
    else:
        return None
