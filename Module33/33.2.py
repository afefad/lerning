import re

text = 'AV - Analytics Vidhya AV'

result = re.match(r'AV', text)   # Поиск в начале строки по заданному шаблону
print('Поиск в начале строки по заданному шаблону', result)
print(result.group(0))
print(result.start())
print(result.end())

result = re.match(r'Analytics', text)
print(result)

print("=" * 40, end='\n\n')

result = re.search(r'Analytics', text)  # Поиск в строке по шаблону
print('Поиск в строке по шаблону', result)
print(result.group(0))

result = re.findall(r'AV', text)  # Все совпадения по шаблону
print('Все совпадения по шаблону', result)
# print(result.group(0))
print("=" * 40, end='\n\n')

text_2 = 'AV is largest Analytics community of India. India!'
result = re.sub(r'India', 'the World', text_2)    # Замена всех найденный шаблонов
print('Замена всех найденный шаблонов', result)

print("=" * 40, end='\n\n')

pattern = re.compile(r'AV')
result = pattern.findall(text)
print(result)
result2 = pattern.findall(text_2)
print(result2)

# Практика
# Задача 1. Скороговорка
# Дан текст вот такой английской скороговорки:
#
# How much wood would a woodchuck chuck if a woodchuck could chuck wood?
#
# С помощью модуля re реализуйте программу, которая выполняет следующие действия по порядку:
#
#  - Определить, начинается ли текст с шаблона wo.
#  - Найти первое упоминание шаблона wo в тексте.
#  - Определить содержимое найденной по шаблону подстроки из пункта 2.
#  - Найти позицию, с которого начинается первое упоминание шаблона wo.
#  - Найти позицию, на которой заканчивается первое упоминание шаблона wo.
#  - Получить список из каждого упоминания шаблона wo в тексте.
#  - Заменить в тексте все совпадения по шаблону wo на слово «ЗАМЕНА».
#
# По каждому действию вывести соответствующий результат. Не используйте методы строк.
# Не забывайте использовать приписку r в шаблонах.

text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

pattern = re.compile(r'wo')

result = pattern.match(text)
print(f'Поиск в начале строки по заданному шаблону {pattern}.\n{result}' if result else 'В начале строки не найден шаблон.')

result = pattern.search(text)
print(f'Поиск первого упоминания по заданному шаблону {pattern}.\n{result}' if result else 'В начале строки не найден шаблон.')
print(f'Определить содержимое найденной по шаблону подстроки - {result.group(0)}')
print(f'Найти позицию, с которого начинается первое упоминание шаблона wo - {result.start()}')
print(f'Найти позицию, на которой заканчивается первое упоминание шаблона wo - {result.end()}')

result = pattern.findall(text)
print(f'Поиск всех упоминаний по заданному шаблону {pattern}.\n{result}' if result else 'В начале строки не найден шаблон.')

result = pattern.sub('ЗАМЕНА', text)
print(f'Заменить в тексте все совпадения по шаблону {pattern} на слово «ЗАМЕНА»..\n{result}')

print('\n\n' + "=" * 40, end='\n\n\n')

# Задача 2. Экранирование спецсимволов
# В уроке при написании шаблона мы брали только обычные строки,без всяких специальных знаков.
# Часть из этих спецсимволов является неотъемлемой частью регулярных выражений (о чём мы поговорим уже в следующем уроке),
# они даже выделяются своими цветами при написании паттернов.
# Например:
# exm = re.search(r'\w\d+?.', text)
#
# Поэтому если мы хотим найти в тексте спецсимвол, а не использовать его как часть паттерна,
# то нужно его дополнительно экранировать — добавить обратный слеш перед этим знаком.
# Например, если нам нужно будет найти шаблон wd+?. в виде полноценного текста,
# то это будет выглядеть так:
# exm = re.search(r'\\w\\d\+\?\.', text)
#
# А теперь сама задача. Дан немного изменённый текст скороговорки:
# How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,
# Напишите программу, которая выводит список из всех упоминаний подстроки \wwood+?,

text = 'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?'

pattern = re.compile(r'\\wwood\+\?')
print(pattern)

result = pattern.findall(text)
print(result)