#!/usr/bin/env python3
"""This module shall define the function of async_comprehension"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ This function shall take no arguments and return a list of floats"""
    return [x async for x in async_generator()]
