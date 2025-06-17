import functools
from datetime import datetime, timezone
import time
from typing import Callable

def createtime(cls):
    """Декоратор выводит время создания инстанта класса"""
    @functools.wraps(cls)
    def wrapper(*args, **kwargs) -> any:
        instance = cls(*args, **kwargs)
        print('Время создания инстанса класса:', datetime.now(timezone.utc))
        return instance
    return wrapper

def timer(func: Callable) -> Callable:
    """
    Декоратор выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> any:
        """Вложенная функция для замера времени, возвращает результат выполнения функции"""
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print('Функция работала: {} секунды.'.format(run_time))
        return result
    return wrapped_func


def for_all_methoods(decorator: Callable) -> Callable:
    """Декоратор класса.
    Получает другой декоратор и
    применяет его ко всем методам класса"""
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_methood = decorator(cur_method)
                setattr(cls, i_method_name, decorated_methood)
        return cls
    return decorate


@createtime
@for_all_methoods(timer)
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(self.max_num)])
        return result

    def cubes_sum(self, number: int) -> int:
        result = 0
        for _ in range(number):
            result += sum([i_num ** 3 for i_num in range(self.max_num)])
        return result

my_funcs_1 = Functions(max_num=1000)
# time.sleep(1)
# my_funcs_2 = Functions(max_num=2000)
# time.sleep(1)
# my_funcs_3 = Functions(max_num=3000)
my_funcs_1.squares_sum()
my_funcs_1.cubes_sum(number=2000)

