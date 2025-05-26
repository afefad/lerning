import os
import random



file = os.path.join('E:', os.path.sep, 'school', 'Coding', 'PyCharm', 'speakers.txt')
speakers_file = open(file, 'r', encoding='utf8')
# print(speakers_file.read())   # Файл считывается целиком - может забить память, обьект становится пустым.
for i_line in speakers_file:    # Файл читается построчно, и работать можно с файлом построчно.
    print(i_line, end='')
print('\n\n')
speakers_file.close()           # Обязательно закрываем файл после использования



'''
Задача 1. Результаты
Одному программисту дали задачу для обработки неких результатов тестирования двух групп людей. Файл первой группы 
(group_1.txt) находится в папке task, файл второй группы (group_2.txt) — в папке Additional_info.

Содержимое файла group_1.txt
Бобровский Игорь 10
Дронов Александр 20
Жуков Виктор 30

Содержимое файла group_2.txt
Павленко Геннадий 20
Щербаков Владимир 35
Marley Bob 15

На экран нужно было вывести сумму очков первой группы, 
затем разность очков опять же первой группы 
и напоследок — произведение очков уже второй группы. 
Программист оказался не очень опытным, писал код наобум и даже не стал его проверять. 
И оказалось, этот код просто не работает. Вот что он написал:

file = open('E:\\task\group_1.txt', 'read')
summa = 0

for i_line in file:
    info = i_line.split()
    summa += info[2]

file = open('E:\\task\group_1.txt', 'read')
diff = 0

for i_line in file:
    info = i_line.split()
    diff -= info[2]

file_2 = open('E:\\task\group_2.txt', 'read')
compose = 0

for i_line in file:
    info = i_line.split()
    compose *= info[2]

print(summa)
print(diff)
print(compose)

Исправьте код для решения поставленной задачи. Для проверки результата создайте необходимые папки
(task, Additional_info, Dont touch me) на своём диске в соответствии с картинкой и также добавьте файлы group_1.txt и group_2.txt.
'''
group_1 = os.path.join('task', 'group_1.txt')
file = open(group_1, 'r', encoding='utf8')

summa = 0
for i_line in file:
    info = i_line.split()
    summa += int(info[2])
print(summa)
file.close()

file = open(group_1, 'r', encoding='utf8')
diff = 0

for i_line in file:
    info = i_line.split()
    if info[2].isnumeric():
        diff -= int(info[2])
print(diff)
file.close()

group_2 = os.path.join('task', 'Additional_info', 'group_2.txt')
file_2 = open(group_2, 'r', encoding='utf8')
compose = 1

for i_line in file_2:
    info = i_line.split()
    if info[2].isnumeric():
        compose *= int(info[2])
print(compose)
file_2.close()
print('\n\n')
'''
Задача 2. Поиск файла 2
Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только программисту. 
Таким образом, с ними можно работать точно так же, как и с обычными текстовыми файлами.

Используя функцию поиска файла из предыдущего урока, реализуйте программу, 
которая находит внутри указанного пути все файлы с искомым названием и выводит на экран текст одного из них 
(выбор можно сгенерировать случайно).

Подсказка: можно использовать, например, список для сохранения найденного пути.
'''

# search_dir = input('Ищем в: ')
search_dir = os.path.join('E:', os.path.sep, 'school', 'Coding')
# search_file = input('Имя файла: ')
search_file = 'Bot_0.1.py'

def file_search(dir, file):

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

file_search(search_dir, search_file)
