import time
from typing import Callable
#
#
# def timer(func: Callable) -> Callable:
#     """
#     Декоратор выводящий время, которое заняло
#     выполнение декорируемой функции.
#     """
#
#     def wrapped_func(*args, **kwargs) -> any:
#         """Вложенная функция для замера времени, возвращает результат выполнения функции"""
#         started_at = time.time()
#         result = func(*args, **kwargs)
#         ended_at = time.time()
#         run_time = round(ended_at - started_at, 4)
#         print('Функция работала: {} секунды.'.format(run_time))
#         return result
#
#     return wrapped_func
#
# @timer
# def squares_sum() -> int:
#     number = 100
#     result = 0
#     for _ in range(number + 1):
#         result += sum([i_num ** 2 for i_num in range(10000)])
#
#     return result
#
# @timer
# def cubes_sum(number: int) -> int:
#     result = 0
#     for _ in range(number + 1):
#         result += sum([i_num ** 3 for i_num in range(10000)])
#
#     return result
#
# my_sum = squares_sum()
# print(my_sum)
# print()
#
# my_cubes_sum = cubes_sum(200)
# print(my_cubes_sum)

# # Практика
#
# Задача 1. Двойной вызов.
# Реализуйте декоратор do_twice,
# который дважды вызывает декорируемую функцию.
# Не забывайте про документацию и аннотации типов.
# Пример декорируемой функции:
#
# def greeting(name):
#     print('Привет, {name}!'.format(name=name))
#
# Основной код:
#
# greeting('Tom')
#
# Результат:
# Привет, Tom!
# Привет, Tom!

def do_twice(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Callable:
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapped_func

@do_twice
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))

greeting('Tom')