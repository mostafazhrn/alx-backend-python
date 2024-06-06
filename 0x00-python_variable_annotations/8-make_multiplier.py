#!/usr/bin/env python3
"""This module shall define the function of make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This function shall take a float and return a function"""
    def multi(n: float) -> float:
        return n * multiplier
    return multi
