#!/usr/bin/env python3
"""This module shall define the function of wait_random"""
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ This function shall take an integer and return a float"""
    import random
    late = random.uniform(0, max_delay)
    await asyncio.sleep(late)
    return late
