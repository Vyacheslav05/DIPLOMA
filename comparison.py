import time
import psutil
from memory_profiler import memory_usage
import time

from memory_profiler import memory_usage
import time

def measure_performance(func, *args):
    start_time = time.time()
    mem_usage = memory_usage((func, args), interval=0.1, timeout=1)
    end_time = time.time()

    return {
        "time": end_time - start_time,
        "memory": max(mem_usage) - min(mem_usage),
    }