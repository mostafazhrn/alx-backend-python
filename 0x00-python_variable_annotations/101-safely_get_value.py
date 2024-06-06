#!/usr/bin/env python3
"""This module shall return the values with the correct type annotations"""
from typing import Any, Union, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """ This function shall take a dict, key & a valu & return val of key"""
    if key in dct:
        return dct[key]
    else:
        return default
