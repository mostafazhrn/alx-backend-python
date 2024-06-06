#!/usr/bin/env python3
"""This module shall define the function of to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ This function shall take str and int or float and return a tuple"""
    return (k, v * v)
