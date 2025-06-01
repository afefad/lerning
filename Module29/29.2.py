import time
from typing import Callable


def timer(func: Callable, *args, **kwargs) -> any:
    """Функция таймер выводит время работы функции и возвращает её результат."""
    started_at = time.time()
    result = func(*args, **kwargs)
    ended_at = time.time()
    run_time = round(ended_at - started_at, 4)
    print('Функция работала: {} секунды.'.format(run_time))

    return result


def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])

    return result

def qubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])

    return result

my_result = timer(squares_sum)
print(my_result)
my_qubes_sum = timer(qubes_sum, 200)
print(my_qubes_sum)

# # Практика
# Задача 1. Функции
# Дана функция func_1, которая принимает число и возвращает результат его сложения с числом 10:
#
# def func_1(x):
#     return x + 10
#
# Реализуйте функцию высшего порядка func_2, которая будет возвращать перемножение двух результатов
# переданной функции.
# Пример основного кода:
#
# print(func_2(func_1, 9))
#
# Результат: 361.

def func_1(x):
    return x + 10

def func_2(func: Callable, *args, **kwargs) -> any:
    result = func_1(*args, **kwargs) * func_1(*args, **kwargs)
    return result

print(func_2(func_1, 9))