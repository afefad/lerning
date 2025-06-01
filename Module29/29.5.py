import time
import functools
from typing import Callable


def timer(func: Callable) -> Callable:
    """
    Декоратор выводящий время, которое заняло
    выполнение декорируемой функции.
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> any:
        # """Вложенная функция для замера времени, возвращает результат выполнения функции"""
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print('Функция работала: {} секунды.'.format(run_time))
        return result

    return wrapped_func

@timer
def squares_sum() -> int:
    """
    Функция нахождения суммы квадратов
    для каждого N от 0 до 10000,
    где 0 <= N <= 100

    :return: Сумма квадратов
    """

    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])

    return result


print(squares_sum.__doc__)
print(squares_sum.__name__)