# def ask_user(question,
#              complaint = "Пожалуйста, введите 'да' или 'нет'",
#              retries = 4):
#     while True:
#         answer = input(question).lower()
#         if answer == 'да':
#             return 1
#         if answer == 'нет':
#             return 0
#         retries -= 1
#         if retries == 0:
#             print('Количество попыток истекло.')
#             break
#         print(complaint)
#         print(f'Осталось попыток: {retries}')
#
# ask_user('Вы действительно хотите выйти?\n>>> ')
# ask_user('Удалить файл?\n>>> ', retries=10)
# ask_user('Записать файл?\n>>> ')
from imaplib import IMAP4_SSL


# def add_num (num: int,
#              lst: list | None = None) -> None:
#     '''
#     В теле функции в список lst добавляется число num
#     и сам список выводится на экран.
#     :param num: Позиционный аргумент.
#     :param lst: Список lst, по умолчанию он пустой.
#     :return: Выводит список на экран.
#     '''
#     lst=list()
#     lst.append(num)
#     print(id(lst))
#     print(lst)
#
# some_list = list()
#
# add_num()


# def create_dict(data):
#     if isinstance(data, dict):
#         return data
#     if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
#         return {data: data}
#
#
# def data_preparation(old_list):
#     new_list = []
#     for i_element in old_list:
#         result = create_dict(i_element)
#         print(result)
#         if result is not None:
#             new_list.append(result)
#     return new_list
#
#
# data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
# data = data_preparation(data)
# print(data)

# def print_tax_document(tax: int, *args: int, **kwargs) -> None:
#     '''
#     Велечина налога
#     Функция с параметрами:
#         Налог
#         Цены
#         Доп.информация.
#
#     Входные данные:
#     Сумма с учётом налога и доп информация
#     '''
#     price_sum = 0
#     for i_price in args:
#         price_sum = price_sum + i_price + i_price * tax / 100
#     print('Сумма цен с учётом налога: {}'.format(price_sum))
#
#     for i_info, i_value in kwargs.items():
#         print('{}: {}'.format(i_info, i_value))
#
# tax = int(input('Величина налога: '))
#
# print_tax_document(tax, 1000, 950, 880, 920, 990,
#                    year=1997,
#                    doc_type='report',
#                    operation_id=1110034)


# def factorial(number):
#     if number == 1:
#         # Если number равно 1, то возвращаем 1, так как факториал 1 равен 1.
#         return 1
#     else:
#         # Если number больше 1, то вычисляем факториал (number - 1) и умножаем на number.
#         return number * factorial(number - 1)
#
# num = int(input('Введите число: '))
# print(f'Факториал числа {num} = {factorial(num)}')

import random


def binary_search(arr, x, start, end):
    # arr — список всех элементов;
    # x — элемент, который мы ищем;
    # start — первый индекс;
    # end — последний индекс;
    # то есть start/end — границы поиска внутри списка.
    if start > end:
        # Если начальный индекс больше конечного, то элемент не найден, возвращаем -1.
        # Это будет значить, что мы не нашли нужное число.
        return - 1
    # Иначе находим индекс среднего элемента.
    mid = (start + end) // 2
    if arr[mid] == x:
        # Если средний элемент равен искомому элементу, то возвращаем его индекс.
        return mid
    elif arr[mid] < x:
        # Если средний элемент меньше искомого элемента, то ищем элемент во второй половине списка (после среднего элемента).
        return binary_search(arr, x, mid + 1, end)
    else:
        # Если средний элемент больше искомого элемента, то ищем элемент в первой половине списка (до среднего элемента).
        return binary_search(arr, x, start, mid - 1)

arr = [random.randint(5, 15) for _ in range(30)]
print(arr)
x = random.randint(5, 15)
print(x)
result = binary_search(arr, x, 0, len(arr) - 1)
if result != -1:
    print(f"Элемент найден в индексе {result}")
else:
    print("Элемент не найден")