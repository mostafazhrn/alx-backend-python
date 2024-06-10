#!/usr/bin/env python3
"""This module shall define the function of task_wait_random"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(n: int) -> asyncio.Task:
    """ This function shall take an integer and return a task"""
    return asyncio.create_task(wait_random(n))
