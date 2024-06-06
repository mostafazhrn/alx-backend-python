#!/usr/bin/env python3
"""This module shall define the function of sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ This function shall take a list of floats and return their sum"""
    res: float = 0
    for i in input_list:
        res += i
    return res
