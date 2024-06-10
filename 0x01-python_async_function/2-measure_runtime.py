#!/usr/bin/env python3
"""This module shall define the function of measure_time"""
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """ This function shall take an integer and return a float"""
    start = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    end = time.perf_counter() - start
    sum = end / n
    return sum
