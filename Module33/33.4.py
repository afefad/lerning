import requests
import json

# my_req = req.get('https://www.google.com')
# print(my_req.text)

response = requests.get('https://swapi.py4e.com/api/people/3/')
print(response.text)

data = json.loads(response.text) # Десериализация JSON
print(data)
data['name'] = 'R10-D10'
print(data)

data2 = json.dumps(data, indent=4) # Сериализация JSON в консоли
print(data2)

with open('my_test.json', 'w') as file:
    json.dump(data, file, indent=4) # Сериализация JSON в файл
    print('Данные записаны')

with open('my_test.json', 'r') as file:
    data3 = json.load(file)
    print(data3)


# # Практика
# Задача 1. Звёздные войны
# Повторите пример парсинга, разобранный в уроке: перейдите на сайт с API,
# посвящённый вселенной Star Wars.
#
# После этого сгенерируйте реквест-ссылку на данные о человеке под номером 3 (people/3/).
#
# Затем напишите программу, которая парсит данные об этом человеке,
# изменяет его имя на ваше собственное и сохраняет результат в виде JSON-файла.
#
# Дополнительно: обратите внимание на значение ключа homeworld — там также хранится ссылка.
# В том же коде спарсите эту ссылку и посмотрите, что там.
#
# Примечание: API тоже пишут люди, а значит, время от времени его могут как-то менять
# и усовершенствовать, поэтому будьте внимательны: может быть, ссылка уже хранится в другом ключе.

result = requests.get('https://swapi.py4e.com/api/planets/8/')
print(json.dumps(result.json(), indent=4))
