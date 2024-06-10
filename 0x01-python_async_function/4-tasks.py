#!/usr/bin/env python3
"""This module shall define the function of task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ This function shall take an integer and return a list of floats"""
    delays: List[float] = []
    all_del: List[float] = []
    for x in range(n):
        delays.append(task_wait_random(max_delay))
    for x in asyncio.as_completed(delays):
        all_del.append(await x)
    return all_del
