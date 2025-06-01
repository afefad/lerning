# def fibonacci(number):
#     cur_val = 0
#     next_val = 1
#     for _ in range(number):
#         yield cur_val
#         cur_val, next_val = next_val, cur_val + next_val
#         if cur_val > 10 ** 6:
#             return cur_val
#
# def square(nums):
#     for num in nums:
#         yield num ** 2
#
# fib_iterator = fibonacci(number=10000000)
#
# for _ in fib_iterator:
#     print(_)
# print('\n')
#
# # Генератор от генератора.
# print(sum(square(fibonacci(number=5000))))
#
# print()
# cubes_gen = (num ** 2 for num in range(10))
# for i_num in cubes_gen:
#     print(i_num, end=' ')
#
# # Задача 1. Бесконечный генератор
# # По аналогии с бесконечным итератором из практики предыдущего урока,
# # реализуйте свой счётчик-генератор, который также в цикле будет бесконечно выдавать значения.
# #
# # Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.
#
# def infinity_gen():
#     counter = -1
#     while True:
#         counter += 1
#         yield counter
#
# my_counter = infinity_gen()
# for i in my_counter:
#     print(i)
#
# Задача 2. Очень большой файл
# Вам на обработку пришёл огромнейший файл с данными.
# Настолько огромный, что при его открытии компьютер просто зависает,
# так как данные не помещаются в оперативной памяти вашего суперкомпьютера (не очень-то и «супер»).
#
# В файле numbers.txt есть N чисел, разделённых пробелами и литералом пропуска строки.
# Напишите программу, которая подсчитает общую сумму чисел в файле.
# Для считывания файла реализуйте специальный генератор.


from collections.abc import Iterable

def nums_gen(quantity_of_numbers: int = 10 ** 2,
             min_num: int = 1,
             max_num: int = 10 ** 3,
             numbers_in_line: int =10):
    """
    Генератор случайных чисел в файл numbers.txt
    создаёт файл numbers.txt и записывает в него рандомно числа от min_num до max_num
    в строчки по numbers_in_line цифр

    :param quantity_of_numbers: Количество цифр (quantity_of_numbers=10 ** 2)
    :param min_num: минимальное число (min_num=1)
    :param max_num: максимальное число (max_num=10 ** 3)
    :param numbers_in_line: количество цифр в строке (numbers_in_line=10)
    :return:
    """
    from random import randint
    for j in range(quantity_of_numbers):
        for _ in range(numbers_in_line - 1):
            num = str(randint(min_num, max_num)) + ' '
            yield num
        num = str(randint(min_num, max_num)) + '\n'
        yield num

def lazy_open(file: str) -> Iterable[str]:

    def lazy_line(file: str) -> Iterable[str]:
        with open(file, 'r') as num_file:
            for i_line in num_file:
                yield i_line

    num_file = lazy_line(file)
    for i_line in num_file:
        nums = i_line.split()
        for i_num in nums:
            if i_num.isnumeric():
                yield int(i_num)
            else:
                continue

try:
    with open('numbers.txt', 'w') as numbers:
        my_counter = nums_gen()
        for i in my_counter:
            numbers.write(i)
    print(sum(lazy_open('numbers.txt')))

except FileNotFoundError:
    print('Файл не найден.')
finally:
    print('')