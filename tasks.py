import time
import requests
import math

# I/O-bound задача: загрузка данных с веб-сайта
def io_bound_task(url):
    response = requests.get(url)
    return response.text

# CPU-bound задача: вычисление суммы квадратов чисел
def cpu_bound_task(n):
    return sum([i**2 for i in range(n**2)])

# Блокирующая задача: чтение файла
def blocking_task(f):
    with open('large_file.txt', "r", encoding="utf-8") as f:
        data = f.read()