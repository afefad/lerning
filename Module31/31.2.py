from collections.abc import Iterator
from contextlib import contextmanager
import time

@contextmanager
def next_num(num: int) -> Iterator[int]:
    print('Входим в функцию')
    try:
        yield num + 1
    except ZeroDivisionError as exc:
        print('Обнаружена ошибка:', exc)
    finally: print('Здесь код выполнится в любом случае')
    print('Выход из функции')


with next_num(-1) as next:
    print(f'Следующее число = {next}')
    print(10 / next)


class Timer:
    def __init__(self) -> None:
        print('Время работы кода')
        self.start = None

    def __enter__(self) -> 'Timer':
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        print(time.time() - self.start, 'секунд')
        if exc_type is TypeError:
            return True

@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as ex:
        print(ex)
    finally:
        print(time.time() - start)

with timer() as t1:
    print('первая часть')
    val_1 = 100 ** 100 ** 2
    val_1 += 'abc'
    '''Ещё какой то код'''

with timer() as t2:
    print('вторая часть')
    val_2 = 200 ** 200 ** 2
    '''Ещё какой то код'''

with timer() as t3:
    print('третья часть')
    val_3 = 300 ** 300 ** 2
    '''Ещё какой то код'''