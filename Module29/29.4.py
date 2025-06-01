import time
from typing import Callable

# def logging(func: Callable) -> Callable:
#     """
#     Декоратор, логирующий работу кода.
#     """
#
#     def wrapped_func(*args, **kwargs) -> any:
#         """"""
#         print('\nВызывается функция {func}\n'
#               'Позицонные аргументы: {args}\n'
#               'Именованные аргументы: {kwargs}'.format(
#             func=func.__name__,
#             args=args,
#             kwargs=kwargs
#         ))
#         result = func(*args, **kwargs)
#         print('Функция успешно завершила работу')
#         return result
#
#     return wrapped_func
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
# @logging
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
# @logging
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
# Задача 1. Сэндвич
# Есть функция, которая выводит начинку сэндвича.
# Сверху и снизу от начинки идут различные ингредиенты вроде салата,
# помидоров и других. Всё это в свою очередь содержится между двух половинок булочки.
# Реализуйте такую функцию и два соответствующих декоратора — ингредиенты и хлеб.
#
# Пример результата работы программы при вызове функции sandwich:
#
# </----------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>

# def bon_bon(func: Callable) -> Callable:
#
#     def wrapped_func(*args, **kwargs):
#         print('</----------\\>'.center(14))
#         func(*args, **kwargs)
#         print('<\\______/>'.center(14))
#     return wrapped_func
#
# def vegetables(func: Callable) -> Callable:
#     def wrapped_func(*args, **kwargs):
#         print('#помидоры#'.center(14))
#         func(*args, **kwargs)
#         print('~салат~'.center(14))
#
#     return wrapped_func
#
# @bon_bon
# @vegetables
# def sandwich(ingredient: str) -> any:
#     print('--{}--'.format(ingredient).center( len(ingredient) + 4))

# while True:
#     sandwich(input('Введите основной ингредиент: '))
#     print()