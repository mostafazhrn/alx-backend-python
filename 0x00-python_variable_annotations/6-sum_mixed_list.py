#!/usr/bin/env python3
"""This module shall define the function of sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ This function shall take lst floats and ints and return their sum"""
    res: float = 0
    for i in mxd_lst:
        res += i
    return res
