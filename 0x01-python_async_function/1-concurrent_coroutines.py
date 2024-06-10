#!/usr/bin/env python3
"""This module shall define the function of wait_n"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """ This function shall take an integer and return a float"""
    delays: List[float] = []
    all_del: List[float] = []
    for x in range(n):
        delays.append(wait_random(max_delay))
    for x in asyncio.as_completed(delays):
        earl_res = await x
        all_del.append(earl_res)
    return all_del
