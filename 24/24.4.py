import os
import random



# file = os.path.join('speakers.txt')
# speakers_file = open(file, 'r', encoding='utf8')
# sym_count = []
# for i_line in speakers_file:    # Файл читается построчно, и работать можно с файлом построчно.
#     print(i_line, end='')
#     sym_count.append(str(len(i_line)))
# sym_count_str = '\n'.join(sym_count)
# speakers_file.close()
#
#
# file_2 = os.path.join('sym_counts.txt') # Задание относительного пути до файла
# counts_file = open(file_2, 'w')         # Открытие файла для записи
# counts_file.write(sym_count_str)        # Запись результата в файл
# counts_file.close()                     # Закрытие файла





search_dir = os.path.join('E:', os.path.sep, 'school', 'Coding')
search_file = 'Bot_0.1.py'
print('Ищем в: {}'.format(search_dir))
print('Имя файла: {}'.format(search_file))
file_to_write = os.path.abspath(os.path.join('E:', os.path.sep, 'school', 'Coding', 'PyCharm', '24.4', '24.4_less.txt'))

def file_search(dir, file, write_file):

    temp_list = []

    if not os.path.isdir(dir):
        print(f'{os.path.isdir(dir)} - не является директорией.')

    def temp_func(dir, file, list):

        for i_elem in os.listdir(dir):
            if i_elem == file:
                list.append(os.path.join(dir, i_elem))
            elif os.path.isdir(os.path.join(dir, i_elem)):
                temp_func(os.path.join(dir, i_elem), file, list)

    temp_func(dir, file, temp_list)
    print(random.choice(temp_list))
    write = open(write_file, 'a', encoding='utf8')
    for i_str in temp_list:
        write.write(i_str)
        write.write('\n')
    write.close()

file_search(search_dir, search_file, file_to_write)




# '''
# Задача 1. Сумма чисел
# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке.
# Напишите программу, которая выводит их сумму в выходной файл answer.txt.
#
# Пример:
# Содержимое файла numbers.txt:
# 1
# 2
# 3
# 4
# 10
#
# Содержимое файла answer.txt
# 20
# '''
#
# numbers = open('numbers.txt', 'r', encoding='utf8')
# counter = 0
#
# for i_str in numbers:
#     counter += int(i_str)
#
# numbers.close()
#
# answer = open('answer.txt', 'w', encoding='utf8')
# answer.write(str(counter))
# answer.close()




'''
Задача 2. Всё в одном
Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком в другой город, 
и там у него случилась беда: его диск пришлось отформатировать, а доступ в интернет отсутствует. 
Остался только телефон с мобильным интернетом. Так как со связью (и с памятью) проблемы, друг попросил вас скинуть 
одним файлом все решения и скрипты, которые у вас сейчас есть.

Напишите программу, которая копирует код каждого скрипта в папке проекта python_basic в файл scripts.txt, 
разделяя код строкой из 40 символов *.

Пример содержимого файла scripts.txt:

import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
)
print(info)

with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)
****************************************

print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

print("Уравнение прямой, проходящей через эти точки:")
x_diff = x1 - x2
y_diff = y1 - y2
if x_diff == 0:
    print("x = ", x1)
elif y_diff == 0:
    print("y = ", y1)
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("y = ", k, " * x + ", b)
****************************************
'''

search_dir = os.path.join('E:', os.path.sep, 'school', 'Coding', 'PyCharm')
print('\nСоединяю все файлы из директории: {}\n В один текстовый файл projects.txt'.format(search_dir))

def file_search(dir, list):

    if not os.path.isdir(dir):
        print(f'{os.path.isdir(dir)} - не является директорией.')

    for i_elem in os.listdir(dir):
        if i_elem.endswith('.py'):
            list.append(os.path.join(dir, i_elem))

files_list = []
file_search(search_dir, files_list)

projects_txt = open(os.path.join('projects.txt'), 'w', encoding='utf8')

for i_elem in files_list:
    temp_file = open(os.path.abspath(i_elem), 'r', encoding='utf8')
    projects_txt.write('\nНачало файла: ' + i_elem + ' ->' + '\n\n')
    for i_str in temp_file:
        projects_txt.write(str(i_str))
    projects_txt.write('\n<- ' + 'Конец файла: ' + i_elem + '\n' +'*' * 40 + '\n\n')
    temp_file.close()

projects_txt.close()