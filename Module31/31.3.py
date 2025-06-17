import time
import functools
from typing import Callable, Optional

# def timer_with_precision(_func: Optional[Callable] = None, *, precision: int = 2) -> Callable:
#     def timer_decorator(func: Callable) -> Callable:
#         """
#         Декоратор выводящий время, которое заняло
#         выполнение декорируемой функции.
#         """
#         @functools.wraps(func)
#         def wrapped_func(*args, **kwargs) -> any:
#             """Вложенная функция для замера времени, возвращает результат выполнения функции"""
#             started_at = time.time()
#             result = func(*args, **kwargs)
#             ended_at = time.time()
#             run_time = round(ended_at - started_at, precision)
#             print('Функция работала: {} секунды.'.format(run_time))
#             return result
#         return wrapped_func
#
#     if _func is None:
#         return timer_decorator
#     return timer_decorator(_func)
#
#
# @timer_with_precision
# def squares_sum() -> int:
#     number = 100
#     result = 0
#     for _ in range(number + 1):
#         result += sum([i_num ** 2 for i_num in range(10000)])
#
#     return result
#
# @timer_with_precision(precision=4)
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

# Задача 1. Повторение кода
# В одной из практик вы уже писали декоратор do_twice,
# который повторяет вызов декорируемой функции два раза.
# В этот раз реализуйте декоратор repeat,
# который повторяет задекорированную функцию уже n раз.

def repeater_with_counter(_func: Optional[Callable] = None, *, repeat_count: int = 1) -> Callable:
    def repeater(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> any:
            for _ in range(repeat_count):
                func(*args, **kwargs)
        return wrapped_func

    if _func is None:
        return repeater
    return repeater(_func)

def func_delay_with_param(_func: Optional[Callable] = None, *, delay: int = 1) -> Callable:
    def func_delay(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> any:
            time.sleep(delay)
            func(*args, **kwargs)
        return wrapped_func

    if _func is None:
        return func_delay
    return func_delay(_func)


@repeater_with_counter(repeat_count=4)
def say_hello(username) -> None:
    print(f'Привет {username}, Давно тебя не было в уличных гонках!')

@func_delay_with_param
def say_hello_2(username) -> None:
    print(f'Привет {username}, Давно тебя не было в уличных гонках!')

@repeater_with_counter(repeat_count=3)
@func_delay_with_param(delay=2)
def say_hello_3(username) -> None:
    print(f'Привет {username}, Давно тебя не было в уличных гонках!')

say_hello('Mike')
say_hello_2('Nataly')
say_hello_3('Jopa')
