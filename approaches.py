# Asyncio

import asyncio
import aiohttp
import threading
import math
import requests
import time

async def asyncio_io_bound_task(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def asyncio_cpu_bound_task(n):
    return sum([i**2 for i in range(n**2)])

async def asyncio_blocking_task(f):
    with open('large_file.txt', "r", encoding="utf-8") as f:
        data = f.read()

# Threading

def threading_io_bound_task(url):
    response = requests.get(url)
    return response.text

def threading_cpu_bound_task(n):
    return sum([i**2 for i in range(n**2)])

def threading_blocking_task(f):
    with open('large_file.txt', "r", encoding="utf-8") as f:
        data = f.read()

# Multiprocessing
from multiprocessing import Pool

def multiprocessing_io_bound_task(url):
    response = requests.get(url)
    return response.text

def multiprocessing_cpu_bound_task(n):
    return sum([i**2 for i in range(n**2)])

def multiprocessing_blocking_task(f):
    with open('large_file.txt', "r", encoding="utf-8") as f:
        data = f.read()