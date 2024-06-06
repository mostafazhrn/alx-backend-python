#!/usr/bin/env python3
"""This module shall return the values iwth the appropriate types"""
from typing import List, Union, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ This function shall take list of seqs and return a lst of tuples"""
    return [(x, len(x)) for x in lst]
