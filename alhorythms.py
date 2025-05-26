# print('''O(n) сложность алгоритма''')
# # Задаём исходные данные
# counter = 0
# target = "a"
# text = "mhtirogla"
#
# # Инициализируем переменную для проверки успеха поиска
# success = False
#
# # Запускаем цикл по каждому символу в тексте
# for letter in text:
#     counter += 1
#     # Сравниваем текущую букву с искомой
#     if letter == target:
#         # Если совпадение найдено, обновляем статус и прерываем цикл
#         success = True
#         break
#
# # Выводим результат поиска
# if success:
#     print("Буква была найдена в строке")
# else:
#     print("Буквы в строке нет")
#
# print(f'Потребовалось {counter} действий')
# from itertools import count
# from operator import index

# print('''O(main_length * sub_length) сложность алгоритма''')
# sub_string = 'ow'
# main_string = 'Hello world!'
# # Нам нужны будут длины строки и подстроки
# main_length = len(main_string)
# sub_length = len(sub_string)
# # И нужен будет указатель, который мы изменим, если строка будет найдена
# success = False
#
# # Мы можем проходить не по всей строке.
# # Например, если мы ищем подстроку из шести букв в слове из десяти букв,
# # то проверить нужно только первые четыре буквы, так как подстрока просто не поместится в остатке строки, если поиск будет начинаться с пятой буквы.
# # Пример:
# # “1122334455” — весь текст;
# # “123456” — подстрока, которую ищем.
# # Надо проверить следующие варианты:
# # начинаем с первого символа и проверяем шесть символов (столько, сколько их в подстроке)
# # “112233” == “123456”?
# # Строки не равны, берём второй символ
# # “122334” == “123456”?
# # Тоже нет
# # “223344” == “123456”?
# # “233445” == “123456”?
# # “334455” == “123456”?
# # А вот дальше двигаться нет смысла, так как в строке осталось всего пять символов и они точно не могут быть равны
# #   подстроке из шести символов:
# # “34455” != “123456”
# # Значит, наш цикл должен был пройти от 0 до 4 (10 − 6 = 4) включительно.
# # Тогда, чтобы найти количество итераций в коде, нам нужно посчитать:
# # (длина главной строки − длина подстроки + 1).
# # +1 нужен, чтобы range дошёл до полученного числа включительно
# count = main_length - sub_length + 1
# for i in range(count):
#     j = 0
#     # j — счётчик для подсчёта совпадений
#     while j < sub_length and main_string[i + j] == sub_string[j]:
#         # Цикл продолжается, пока:
#         # 1) количество совпадений меньше длины подстроки (если они будут равны, то дальше проверку делать нет смысла);
#         # 2) взятые символы равны (с помощью j мы перебираем символы в строке, i используем как сдвиг, чтобы брать из главной строки срез, начиная с текущего символа).
#         j += 1
#
#
#     # Если после вложенного цикла число j равно длине подстроки,
#     # это значит, что мы нашли подстроку в нашей строке, цикл можно прерывать
#     if j == sub_length:
#         success = True
#         break
#
# # После цикла мы проверяем success и делаем итоговый вывод
# if success:
#     print('Подстрока найдена!')
# else:
#     print('Такой подстроки в строке нет :(')


# print('''O(n) сложность алгоритма''')
# text = 'довод'
# reversed_text = ''
#
# # Проходим по всей строке
# for letter in text:
#     # Каждый символ строки добавляем В НАЧАЛО новой строки
#     reversed_text = letter + reversed_text
#
# # В итоге в reversed_text мы получим перевёрнутую строку.
# # Если строки равны, слово является палиндромом
# if text == reversed_text:
#     print('Это палиндром!')
# else:
#     print('Не палиндром!')


# print('''O(n//2) сложность алгоритма''')
# # Возьмём тот же текст
# text = 'довод'
# # Нам понадобится узнать его длину
# text_length = len(text)
# # И вспомогательный флаг
# success = True
# 
# # За одну итерацию мы будем проверять два символа (с начала и с конца),
# # поэтому итераций можно сделать в два раза меньше (text_length // 2):
# for i in range(text_length // 2):
#     # На каждой итерации сравниваем два символа:
#     # символ с начала text[i] с символом с конца text[-i - 1]
#     if text[i] != text[-i - 1]:
#         # Если хотя бы одна пара символов не совпадёт, то меняем флаг и завершаем цикл
#         success = False
#         break
#
# # Если все символы совпадают, то строка является палиндромом, иначе — нет
# if success:
#     print('Это палиндром!')
# else:
#     print('Не палиндром!')


# menu = 'утиное филе;фланк-стейк;банановый пирог;плов'
# print('На данный момент в меню есть:', ', '.join([dish.strip().title() for dish in menu.split(';')]))


# def text_coding(text):
#     count, result = 0, ""
#     for index, symbol in enumerate(text):
#         count += 1
#         if index == len(text) - 1 or symbol != text[index + 1]:
#             result += f'{symbol}{count}'
#             count = 0
#     return result
#
# user_text = input('Введите строку: ')
# print('Закодированная строка:', text_coding(user_text))


## Поиск сдвига в строчках
# def shift_check(first, second):
#     first *= 2
#     index = first.find(second)
#
#     if index != -1:
#         result = f"Первая строка получается из второй со сдвигом {index}"
#     else:
#         result = "Первую строку нельзя получить из второй с помощью циклического сдвига."
#     return result
#
# first_string = input('Первая строка: ')
# second_string = input('Вторая строка: ')
#
# if len(first_string) != len(second_string):
#     print('Разная длинна строк.\nПервую строку нельзя получить из второй с помощью циклического сдвига.\nВыход из программы')
#     exit()
#
# print(shift_check(first_string, second_string))


## Моё решение задачи
# data = [
#     ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
#     ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
#     ["128.0.0.255", ["file_1.txt 1document_2024.docx notes2022.txt"]],
#     ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
#     ["192.168.1.10", ["file_432.txt  important_info.txt notes1900.txt"]],
#     ["192.c8.1.10", ["file_432.xt  &meeting_notes.docx notes1995.txt"]],
#     ["10.20.30.40", ["file_432.txt  analysis_results.txt notes1998.txt"]],
# ]
#
# correct_data = []
# correct_ip = []
# # Проверка IP адреса на корректность в базе
# for i_obj in data:
#
#     if len(i_obj[0].split('.')) == 4:
#         for i_num in i_obj[0].split('.'):
#             if not i_num.isnumeric():
#                 break
#             elif not 0 <= int(i_num) <= 255:
#                 break
#         else:
#             correct_ip.append(i_obj)
#
# # Проверка правильности названий файлов в базе
# resolutions = ('.txt', '.docx')
# for i_obj in correct_ip:
#     files_list = ''.join(i_obj[1]).split()
#
#     for i_file in files_list:
#         # проверка начала файла.
#         if i_file[0].isalpha() or i_file[0].isnumeric():
#             # проверка окончания файла
#             if not i_file.endswith(resolutions):
#                 break
#         else:
#             break
#     else:
#         correct_data.append(i_obj)
#
# for i in range(len(correct_data)):
#     print(correct_data[i])


# # Решение задачи от нейросети
# def is_valid_ip(ip_addr):
#     parts = ip_addr.split('.')
#     if len(parts) != 4:
#         return False
#     for part in parts:
#         if not part.isdigit():
#             return False
#         num = int(part)
#         if not 0 <= num <= 255:
#             return False
#     return True
#
# def is_valid_filename(filename):
#     invalid_symbols = "@№$%^&*()"
#     valid_extensions = (".txt", ".docx")
#     if not filename:  # Проверка на пустую строку
#         return False
#     if filename[0] in invalid_symbols:
#         return False
#     if not filename.endswith(valid_extensions):
#         return False
#     return True
#
# data = [
#     ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
#     ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
#     ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.txt"]],
#     ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
#     ["192.168.1.10", ["file_432.txt  important_info.txt notes1900.txt"]],
#     ["192.c8.1.10", ["file_432.xt  &meeting_notes.docx notes1995.txt"]],
#     ["10.20.30.40", ["file_432.txt  analysis_results.txt notes1998.txt"]],
# ]
#
# correct_data = []
#
# for item in data:
#     ip_address = item[0]
#     filenames = item[1]
#
#     if is_valid_ip(ip_address):
#         valid_files = []
#         for file in filenames[0].split():
#
#             if not is_valid_filename(file):
#                 break
#             else:
#                 valid_files.append(file)
#
#             if valid_files == filenames[0].split():
#                 correct_data.append([ip_address, [' '.join(valid_files)]])
#
# print("Новая структура данных:")
# for item in correct_data:
#     print(item)


# scores = [54, 67, 48, 99, 27]
# for i_player, i_score in enumerate(scores):
#     print(i_player + 1, i_score)