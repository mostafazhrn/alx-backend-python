#!/usr/bin/env python3
"""This module shall define the function of async_generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ This function shall take an integer and return a float"""
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
