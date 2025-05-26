# numbers_list = [1, 5, 2, -7, 6]
#
# for _ in range(5):
#     new_num = int(input('Num: '))
#     numbers_list.append(new_num)
# for number in numbers_list:
#     print(number, "** 2 =", number ** 2)
# import random
# from itertools import count
# from distutils.dist import command_re
# from enum import member
# from idlelib.debugobj import myrepr
# from itertools import count
# from operator import index
# from os import times
# from random import random
# from math import trunc
# from operator import truediv
# from curses.ascii import islower
# from operator import truediv
# from sys import prefix

# books_ID = [50, 34, -1, -1, 2, 23, -1]
# new_books_ID = []
# returned = 0
#
# for _ in range(10):
#     id = random.randrange(1, 100)
#     if id in new_books_ID:
#         _ -= 1
#         continue
#     new_books_ID.append(id)
#
# for id in books_ID:
#     if id == -1:
#         returned += 1
#     else:
#         new_books_ID.append(id)
#
# print('Новый список выданных книг:', new_books_ID)
# print(f'Вернули за день {returned}')

# scores = [8, 5, 10, 7, 6]
# print(scores)
#
# new_scores = []
#
# #Не правильно!!!
# # for score in scores:
# #     if score == 5:
# #         score *= 3
# #     new_scores.append(score)
# # print(new_scores)
#
# scores[1] *= 3
#
# print(scores)


# monsters_count = int(input('Количество монстров: '))
# mage_index = int(input('Номер мага в списке: '))
# monsters_damage = []
#
# for monster in range(monsters_count):
#     print('Урон у', monster + 1, 'монстра:', end=' ')
#     damage=int(input())
#     monsters_damage.append(damage)
#
# print(monsters_damage)
#
# for i_monster in range(monsters_count):
#     if monsters_damage[i_monster] < 100 and i_monster != mage_index - 1:
#         monsters_damage[i_monster] += monsters_damage[mage_index - 1]
#
# print('Итоговый урон монстров: ', monsters_damage)


# # функция enumerate(*переменная*, start=0) для списков
# # В цикле for возвращает кортеж '*индекс элемента*, *элемент*'
# # Отчёт индекса ведёт с заданого числа в start
#
# nums_list = []
#
# for n in range(int(input('Кол-во чисел в списке: '))):
#     nums_list.append(int(input(f'Введите {n + 1} число: ')))
#
# k = int(input('Введите делитель: '))
#
# i_counter = 0
#
# for i, val in enumerate(nums_list, start=0):
#     if val % k == 0:
#         i_counter += i
#         print(f'Индекс числа {val}: {i}')
#
# print(f'Сумма индексов: {i_counter}')


# word = input('Введите слово: ')
# replace_num = int(input('Номер символа для замены: '))
# replace_sym = input('Чем заменяем: ')
#
# sym_list = list(word)
# sym_list[replace_num - 1] = replace_sym
# print(''.join(sym_list))


# words_list = []
# counts = [0, 0, 0]
# for i in range(3):
#     word = input(f'Введите {i + 1} слово: ')
#     words_list.append(word)
#
# text = input('Слово из текста: ')
# while text != 'end':
#     for index in range(3):
#         if words_list[index] == text:
#             counts[index] += 1
#     text = input('Слово из текста: ')
#
# print('\nПодсчёт слов в тексте')
# for i in range(3):
#     print(f'{words_list[i]}: {counts[i]}')


# text = input('Введите текст: \n')
# # Метод split разделяет строку по пробельным символам (пробелы, табуляции, перевод строки)
# text_list = text.split()
# print(text_list)


# text = input('Введите строку: ')
# text_list = list(text)
# counter = 0
#
# for i, var in enumerate(text_list, start=0):
#     if var == ':':
#         text_list[i] = ';'
#         counter += 1
# print(''.join(text_list))
# print(f'Кол-во замен: {counter}')


# import sys
#
# S = input('Введите строку: ')
# n = int(input('Номер символа: '))
# print('\n')
#
# S_list = list(S)
#
# if n >= len(S):
#     print("У символа нет соседа справа.", file=sys.stderr)
# elif n < 1:
#     print("У символа нет соседа слева.", file=sys.stderr)
#
# print(f'Символ слева: {S_list[n - 2]}')
# print(f'Символ справа: {S_list[n]}')
# print('\n')


# scores = [8, 5, 10, 7, 6]
# scores[1] += len(scores)
# scores.append(0)
# scores[2] += len(scores)
# print(scores)


# nums = [4, 9, 7, 6, 3, 2]
# print(f'Неотсортированный список: {nums}')
#
# # Можно так
# for i in range(len(nums)):
#     for index in range(i, len(nums)):
#         if nums[i] > nums[index]:
#             nums[i], nums[index] = nums[index], nums[i]
#
# # Или можно так
# # nums.sort()
#
# print(f'Отсортированый список: {nums}')


# langs = ['Python', 'Java', 'JS', 'SQL']
# user_lang = input('После чего вставить: ')
# i_lang = langs.index(user_lang)
#
# # Вставка элемента в список курильщика
# # new = []
# # for i_lang in range(2):
# #     new.append(langs[i_lang])
# # new.append('C++')
# # for i_lang in range(2, len(langs)):
# #     new.append(langs[i_lang])
# # print(new)
#
# # Вставка элемента в список здорового человека
# langs.insert(i_lang + 1, 'C++')
# print(langs)


# def is_film_exist(movie, films_list):
#     for i_movie in films_list:
#         if i_movie.lower() == movie.lower():
#             return True
#     return False
#
# films = [
#     'Крепкий орешек', 'Назад в будущее', 'Таксист',
#     'Леон', 'Богемская рапсодия', 'Город грехов',
#     'Мементо', 'Отступники', 'Деревня',
#     'Проклятый остров', 'Начало', 'Матрица'
# ]
#
# my_list = []
#
# while True:
#     print(f'\nВаш текущий топ фильмов: {my_list}')
#     new_movie = input('Название фильма: ')
#     if is_film_exist(new_movie, films):
#         print('Комманды: Добавить, Удалить, Вставить')
#         command = input('Введите команду: ')
#
#         if command.lower() == 'добавить':
#             my_list.append(new_movie)
#         elif command.lower() == 'удалить':
#             if is_film_exist(new_movie, my_list):
#                 my_list.remove(new_movie)
#             else:
#                 print('Такого фильма в вашей подборке нет.')
#         elif command.lower() == 'вставить':
#             for i, val in enumerate(my_list, start=0):
#                 print(f'{i}: {val}')
#             place = int(input('Каким по счёту вы хотите вставить данный фильм: '))
#             my_list.insert(place - 1, new_movie)
#
#     else:
#         print('Такого фильма нет на сайте')


# pack = []
# decode = []
# bad_packs = 0
#
# pack_amt = int(input('Количество пакетов: '))
#
# for i_pack_num in range(pack_amt):
#     print('\nПакет номер', i_pack_num + 1)
#     for i_bit in range(4):
#         num = int(input(f'{i_bit + 1} бит: '))
#         pack.append(num)
#     if pack.count(-1) <= 1:
#         decode.extend(pack)
#     else:
#         print('Много ошибок в пакете.')
#         bad_packs += 1
#     pack = []
#
# print(f'\nПолученое ообщение: {decode}')
# print(f'Количество ошибок в сообщении: {decode.count(-1)}')
# print(f'количество потеряный пакетов: {bad_packs}')


# n = int(input('Введите количество участников: '))
# members = list(range(1, n + 1))
# print(members)
#
# n = int(input('Введите количество участников: '))
# members = []
# for _ in range(n//3):
#     members.append(list(range(1, 4)))
# print(members)

# words_list = [['', 0], ['', 0], ['', 0]]
# counts = []
# for i in range(3):
#     word = input(f'Введите {i + 1} слово: ')
#     words_list[i][0] = word
#
# text = input('Слово из текста: ')
# while text != 'end':
#     for index in range(3):
#         if words_list[index][0] == text:
#             words_list[index][1] += 1
#     text = input('Слово из текста: ')
#
# print('\nПодсчёт слов в тексте')
# for i in range(3):
#     print(f'{words_list[i][0]}: {words_list[i][1]}')

# matrix = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]
# for i in matrix:
#     for j in i:
#         print(j, end=' ')
#     print()


# members = []
# N = int(input('Введите количество участников: '))
# M = int(input('Введите количество человек в комманде: '))
# count = 1
#
# if N % M != 0:
#     print(f'{N} участников невозможно поделить на команды по {M} человек!')
#     exit()
#
# for i in range(N//M):
#     command = []
#     for j in range(count, count + M):
#             command.append(j)
#     count += M
#     members.append(command)
#
# print(f'Общий список команд: {members}')


# goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
#
# tax = 0.08
#
# new_fruit = []
# fruit = input('Новый фрукт: ')
# price = int(input('Цена: '))
# new_fruit.append(fruit)
# new_fruit.append(price)
#
# goods.append(new_fruit)
#
# for i in range(len(goods)):
#     goods[i][1] += goods[i][1] * tax
#
# print(goods)


# squares = []
# for x in range(10):
#     squares.append(x ** 2)
#
# print(squares)
#
# squares = [x ** 2 for x in range(10)]
# print(squares)

# def get_higher_price (tax, price):
#     return round(price + price * tax, 2)
#
# prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]
#
# first_year_tax = 0
# second_year_tax = 0.1
#
# prices_first_year = [get_higher_price(first_year_tax, i_price) for i_price in prices_now]
# prices_second_year = [get_higher_price(second_year_tax, i_price) for i_price in prices_first_year]
#
# print(round(sum(prices_now), 2), round(sum(prices_first_year), 2), round(sum(prices_second_year), 2), sep='\n')


# squares = []
# for x in range(10):
#     if x % 2 != 0:
#         squares.append(x ** 2)
#
# squares_odds = [x ** 2 for x in range(10) if x % 2 != 0]
# squares_cubes = [(x ** 2 if x % 2 != 0 else x ** 3) for x in range(10)]
# print(squares_odds)
# print(squares_cubes)


# import random
#
# first_squad = [random.randint(40, 75) for _ in range(10)]
# second_squat = [random.randint(30, 50) for _ in range(10)]
#
# squad_3_condition = [('Погиб' if first_squad[i_damage] + second_squat[i_damage] >= 100 else 'Выжил')
#                      for i_damage in range(10)]
#
# print(first_squad)
# print(second_squat)
# print(squad_3_condition)
# nums = [x for x in range(1, 101) if x % 10 == 0]
#
# new_nums = nums[:]
# new_nums[3] = 0
#
# print(new_nums[2:8])


# def is_palyndrome(num_list):
#     reverse_list = num_list[::-1]
#     if num_list == reverse_list:
#         return True
#     else:
#         return False
#
#
# nums = [1, 2, 3, 4, 5]
# answer = []
#
# for i in range(0, len(nums)):
#     if is_palyndrome(nums[i: len(nums)]):
#         answer = nums[:i]
#         answer.reverse()
#         break
#
# print(nums)
# print()
# print(len(answer))
# print()
# print(answer)

# import random
# original_prices = [random.randint(-50, 200) for _ in range(random.randint(2, 20))]
# new_prices = original_prices [:]
#
# for i in range(len(original_prices)):
#     if new_prices[i] < 0:
#         new_prices[i] = 0
# print("Мы потеряли: ",  (sum(new_prices) - sum(original_prices)))


# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
# print('В первой строке выведите первые пять элементов списка.')
# print(nums[:5])
# print('Во второй строке выведите весь список, кроме последних двух элементов.')
# print(nums[:-2])
# print('В третьей строке выведите все элементы с чётными индексами.')
# print(nums[0::2])
# print('В четвёртой строке выведите все элементы с нечётными индексами.')
# print(nums[1::2])
# print('В пятой строке выведите все элементы в обратном порядке.')
# print(nums[::-1])
# print('В шестой строке выведите все элементы списка через один в обратном порядке, начиная с последнего.')
# print(nums[-1::-2])

# import random
# r = random.randint(10, 20)
# n = [random.randint(-50, 200) for _ in range(r)]
# print(r)
# print(n)
# A = random.randint(1, r - 7)
# print(A)
# B = random.randint(A, r - 1)
# print(B)
# n = n[:A - 1] + n[B:]
# print(n)


# word = 'Привет'
#
# first_part = word[:len(word) // 2]
# print(first_part)
# second_part = word[len(word) // 2:]
# print(second_part)
# print(first_part[::-1] + second_part[::-1])


# nice_list = [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]
#
# output = [k for i in nice_list for j in i for k in j]
# print(output)

# punctuation_marks = [' ', '.', ',', '!', '?', ')', '(', '"', "'", '`', '/', '_', '-', ':', ';', '@']
# letters = [chr(i) for i in range(1072, 1104)]
## print(letters)
# k = int(input('Введите шаг шифра: '))
#
# while k < 1:
#     print('Шаг шифра не может быть меньше 1.')
#     k = int(input('Введите шаг шифра: '))
#
# text = input('Введите текст: ').lower()
# crypt_text = ''.join([i if i in punctuation_marks else letters[(k - 1) - (31 - letters.index(i)) if letters.index(i) > 31 - k else letters.index(i) + k] for i in text])
#
# print(crypt_text)


# user_name = 'afefad'
# file_name = 'poopy'
#
# path = 'C:/{user}/docs/folder/{new_file}.txt'.format(
#     user=user_name,
#     new_file=file_name
# )
#
# path_2 = 'C:/{0}/docs/{0}/folder/{1}.txt'.format(
#     user_name,
#     file_name
# )
#
# path_3 = f'C:/{user_name}/docs/folder/{file_name}.txt'
#
# print(path)
# print(path_2)
# print(path_3)


# while True:
#     grats_template = input('Введите шаблон поздравления, в шаблоне нужно использовать конструкцию '
#                            '{name} и {age}: ')
#     if '{name}' in grats_template and '{age}' in grats_template:
#         break
#     print('Ошибка: Отсутствует одна или две конструкции.')
#
#
# names_list = input('Список людей через запятую: ').split(', ')
# ages_str = input('Возраст людей через пробел: ')
# ages = [int(i_number) for i_number in ages_str.split()]
#
# for i_man in range(len(names_list)):
#     print(grats_template.format(
#         name=names_list[i_man],
#         age=ages[i_man]
#     ))
#
# people = [
#     ' - '.join([names_list[i_man], str(ages[i_man])])
#     for i_man in range(len(names_list))
# ]
#
# people_str = ', '.join(people)
# print('\nИменинники:', people_str)


# text = input('Содержимое файла: ')
# new_text = '---'.join(text.split())
#
# print(new_text)


# words_str = [input(f'Введите {i + 1} слово: ') for i in range(3)]
# words_list = [[words_str[i], 0] for i in range(len(words_str))]
#
# text = input('текст: ').split()
#
# print('\nПодсчёт слов в тексте')
# for i in range(len(words_list)):
#     count = 0
#     for j in range(len(text)):
#         if words_list[i][0] == text[j]:
#             count +=1
#     words_list[i][1] = count
#     print(f'Слово {words_list[i][0]} встречено в тексте {words_list[i][1]} раз.')


# text = ' '.join(input('Введите текст: ').split())
# print(text)


# user_name = 'afefad'
# file_name = 'poopy.txt'
#
# path = 'C:/{user}/docs/folder/{new_file}'.format(
#     user=user_name,
#     new_file=file_name
# )
#
# if not path.endswith('.txt'):
#     print('Не правильное расширение.')
# elif not path.startswith('C:/'):
#     print('Неверно указан диск')
# else:
#     print(path)

# print('''Подсчёт слов в тексте''')
# words_list = [input(f'Введите {i + 1} слово: ').lower() for i in range(3)]
#
# text = input('текст: ').lower().split()
#
# print('\nПодсчёт слов в тексте')
# for index in range(3):
#     print(words_list[index], ':', text.count(words_list[index]))


# print('''Шифр Цезаря!''')
# punctuation_marks = [' ', '.', ',', '!', '?', ')', '(', '"', "'", '`', '/', '_', '-', ':', ';', '@']
# letters = [chr(i) for i in range(1072, 1104)]
#
# k = input('Введите шаг шифра: ')
#
# while True:
#     if not k.isnumeric() :
#         print('Шаг шифра может быть только числом от 1 до 31')
#         k = input('Введите шаг шифра: ')
#     elif int(k) < 1 or int(k) > 31:
#         print('Шаг шифра может быть только числом от 1 до 31')
#         k = input('Введите шаг шифра: ')
#     else:
#         k = int(k)
#         break
#
# text = input('Введите текст: ').lower()
# crypt_text = ''.join([i if i in punctuation_marks else letters[(k - 1) - (31 - letters.index(i)) if letters.index(i) > 31 - k else letters.index(i) + k] for i in text])
#
# print(crypt_text.capitalize())


# file = input('Введите путь к файлу: ')
# disk = input('На каком диске должен лежать файл: ')
# resolution = input('Требуемое расширение файла:')
#
# if not file.startswith(disk):
#     print('Задан неверный диск.')
# elif not file.endswith(resolution):
#     print('Задано неверное разрешение файла.')
# else:
#     print('Путь корректен!')


# text = input('Введите текст: ')
# letters = [0, 0]
#
# for i_letter in text:
#     if i_letter.islower():
#         letters[0] += 1
#     else:
#         letters[1] += 1
# else:
#     print(text.upper() if letters[1] > letters[0] else text.lower())


# details = 500000000
# price = 23.8589578
# indexation = 0.045678
#
#
# print('На складе {:,d} деталей'.format(details))
# print('Каждая деталь стоит {:.2f} рублей'.format(price))
# print('Цена увеличелась на {:.1%}'.format(indexation))