# nums_sum = 0
# nums_count = 0
#
# try:
#     numbers_file = open('numbers1.txt', 'r', encoding='utf8')
#     for i_line in numbers_file:
#         nums_count += 1
#         nums_sum += int(i_line)
#     numbers_file.close()
#     print(f'Среднее арифметическое: {nums_sum / nums_count}')
# except FileNotFoundError:
#     print('Такого файла не существует.')
# except ValueError:
#     print('Нельзя преобразовать данные в целое число!')




# def divide(number):
#     return 10 / number
#
# def sum_of_devided(left, right):
#     div_sum = 0
#     for i_num in range(left, right + 1):
#         try:
#             div_sum += divide(i_num)
#             print(div_sum)
#         except ZeroDivisionError:
#             print('На ноль делить нельзя!')
#     return div_sum
#
# total = 0
#
# try:
#     numbers_file = open('numbers.txt', 'r')
#     for i_line in numbers_file:
#         num_list = i_line.split()
#         first_num = int(num_list[0])
#         second_num = int(num_list[1])
#
#         total += sum_of_devided(first_num, second_num)
#     print(f'Общая сумма: {total}')
#
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')



# # Практика
# """
# Задача 1. Пятый элемент
# В курсе по программированию студенту дали простую задачу: умножить константу (число 42) на пятый элемент строки,
# введённой пользователем.
#
# Модифицируйте этот код, обработав исключения для произвольных входных параметров:
#
# - ValueError — невозможно преобразовать к числу,
# - IndexError — выход за границы списка,
# - остальные исключения.
# Для каждого типа исключений выведите на консоль соответствующее сообщение.
# """
# BRUCE_WILLIS = 42
#
# try:
#     input_data = input('Введите строку: ')
#     leeloo = int(input_data[4])
#     result = BRUCE_WILLIS * leeloo
#
#     print(f'- Leeloo Dallas! Multi-pass № {result}!')
# except ValueError:
#     print('Пятый элемент строки невозможно преобразовать к числу.')
# except IndexError:
#     print('Короткая строка.')
# except:
#     print('Ошибка!')


# Задача 2. Возраст
"""
Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.

Напишите программу, которая считывает файл, даёт имя для каждого возраста (можно просто использовать буквы алфавита)
и выводит результат в новый файл result.txt в формате «имя — возраст».
Программа должна обрабатывать следующие ошибки и выводить сообщение на экран:

Попытка создания файла, который уже существует.
На чтение ожидался файл, но это оказалась директория.
Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.
"""

try:
    names = ['Иван', 'Люда', 'Гриша', 'Roberto']
    ages = []
    ages_list = open('ages.txt', 'r', encoding='utf8')
    for i_line in ages_list:
        try:
            ages.append(int(i_line))
        except ValueError:
            print('В заданом файле находятся не только числа. Агрумент нельзя преобразовать к числу.')
        except:
            print('Неожиданная ошибка.')
    ages_list.close()

    characters_file = open('result.txt', 'w', encoding='utf8')
    for i in range(4):
        characters_file.write(f'{names[i]}: {ages[i]}\n')
    characters_file.close()

    print('Файл result.txt успешно сохранён.')
except IndexError:
    print('list index out of range')
except FileExistsError:
    print('Попытка создания файла или директории, которая уже существует.')
except (ValueError, LookupError):
    print('Некорректное значение')
except IsADirectoryError:
    print('Ожидался файл, но это директория.')