# Класс как контекст-менеджер. Методы enter и exit
import time

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

class File:

    def __init__(self, file: str, literal: str) -> None:
        self.__file = file
        self.__type = literal
        self.temp_file = None

    def __enter__(self):
        self.temp_file = open(self.__file, self.__type)
        return self

    def __iter__(self):
        return self.temp_file

    def __next__(self):
        return self.temp_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.temp_file.close()
        if exc_type is FileNotFoundError:
            print('Такого Файла не существует.')
            return True


# with Timer() as t1:
#     print('первая часть')
#     val_1 = 100 ** 100 ** 2
#     val_1 = 'abc'
#     '''Ещё какой то код'''
#
# with Timer() as t2:
#     print('вторая часть')
#     val_2 = 200 ** 200 ** 2
#     '''Ещё какой то код'''
#
# with Timer() as t3:
#     print('третья часть')
#     val_3 = 300 ** 300 ** 2
#     '''Ещё какой то код'''

with File('example.txt', 'r') as my_file:
    for i in my_file:
        print(i, end='')