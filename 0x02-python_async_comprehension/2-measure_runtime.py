#!/usr/bin/env python3
"""This module shall define the function of measure_runtime"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ This function shall take no arguments and return a float"""
    start = time.perf_counter()
    tsk = [async_comprehension() for x in range(4)]
    await asyncio.gather(*tsk)
    end = time.perf_counter()
    return end - start
