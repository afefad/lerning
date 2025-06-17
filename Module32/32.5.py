from itertools import count
from typing import List



my_nums: List[int] = [3,1,4,1,5,9,2,6]
other_nums: List[int] = [2,9,1,8,2,8,1,8]

result: List[int] = list(map(lambda x, y: x + y, my_nums, other_nums))

print(result)
print(list(map(lambda x, y: 1, [1,2], [2,3,4])))

result_even: List[int] = list(filter(lambda x: x % 2 == 0, result))
print(result_even)

result2: List[int] = list(map(lambda num: num * 3, filter(lambda num: num % 2, my_nums)))
print(result2)

result3: List[int] = sum(list(map(lambda num: num * 3, filter(lambda num: num % 2, my_nums))))
print(result3)

animals: List[str] = ['cat', 'dog', 'cow']

new_animals = list(map(lambda x: x.capitalize(), animals))
# or
new_animals2 = [elem.capitalize() for elem in animals]
print(new_animals)
print(new_animals2)
print('\n\n')


# # Практика
#
# Задача 1. Однострочный код
# Пользователь вводит неопределённое количество чисел.
# Напишите код, который запрашивает эти числа и сортирует их по возрастанию.
# Реализуйте решение в одну строку.
#
# Пример работы консоли:
#
# Введите числа: 5 8 4 1 0 3
#
# [0, 1, 3, 4, 5, 8]

# print(sorted(list(map(int, input('Введите числа: ').split()))))



# Задача 2. Однострочный код 2
# Пользователь вводит строку, состоящую из любых символов.
# Напишите код, который выводит на экран список этих символов,
# исключая цифры и буквы в верхнем регистре.
#
# Пример работы консоли:
#
# Введите строку: qWe456rtY
#
# ['q', 'e', 'r', 't'

# print(list(filter(lambda x: x.islower() and x.isalpha(), input('Введите строку: '))))
# # or
# print(list(filter(lambda x: not (x.isupper() or x.isdigit()), input('Введите строку: '))))



# Задача 3. Функция reduce
# Помимо map и filter, в Python есть ещё одна функция — reduce.
# Она применяет указанную двухаргументную функцию к элементам последовательности,
# сводя её к единственному значению. Однако используют reduce довольно редко.
# Начиная с третьей версии Python, эту функцию даже вынесли из встроенных функций в модуль functools.
#
# Пример кода с reduce:

from functools import reduce
from typing import List

def my_add(a: int, b: int) -> int:
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


numbers: List[int] = [0, 1, 2, 3, 4]
print(reduce(my_add, numbers))

# Используя функцию reduce, реализуйте код, который считает,
# сколько раз слово 'was' встречается в списке:
def was_counter(first_str: (str, int), next_str: str):
    """
    Функция для reduce. Считает, сколько раз слово 'was' встречается в списке сток:
    :param first_str: Первая строка
    :param next_str: Вторая строка
    :return:
    """
    if isinstance(first_str, str):
        counter_1 = first_str.lower().count('was')
    elif isinstance(first_str, int):
        counter_1 = first_str

    counter_2 = next_str.lower().count('was')

    result = counter_1 + counter_2
    print(f"Количество слов 'was' = {result}")
    return result

sentences: List[str] = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic", "because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic", "or had been"]

print(reduce(was_counter, sentences))