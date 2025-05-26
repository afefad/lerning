# def add_num(seq, number: int):
#     seq = list(seq)
#     for i_num in range(len(seq)):
#         seq[i_num] += number
#     return seq
#
# origin_tuple = (3, 1, 4, 1, 5)
# changed_list = add_num(origin_tuple, 5)
#
# print(origin_tuple)
# print(changed_list)
from itertools import count
from tkinter.font import names

# phonebook_dict = {
#     ('Петров', 'Ваня'): 88005553535,
#     ('Егоров', 'Ваня'): 88003333333,
#     ('Ульянов', 'Петя'): 88006663636,
#     ('Сидорова', 'Лена'): 88007773737
# }
#
# phonebook_dict[('Сидорова', 'Алёна')] = 109090
# for i_person in phonebook_dict:
#     if 'Сидорова' in i_person:
#         print(i_person[1], phonebook_dict[i_person])


# data = {
#     (5000, 123456): ('Иванов', 'Василий'),
#     (6000, 111111): ('Иванов', 'Петр'),
#     (7000, 222222): ('Медведев', 'Алексей'),
#     (8000, 333333): ('Алексеев', 'Георгий'),
#     (9000, 444444): ('Георгиева', 'Мария')
# }
#
# ser_pas, num_pas = int(input('Введите серию паспорта: ')), int(input('Введите номер паспорта: '))
#
# for i_num, i_data in data.items():
#     if ser_pas in i_num:
#         if num_pas in i_num:
#             print('{name} {surname}'.format(
#                 name = i_data[1],
#                 surname = i_data[0]
#             ))


# phone_book = {}
#
# while True:
#
#     print("Введите нового пользователя")
#     name = input('Имя: ')
#     if name.lower() == 'exit':
#         exit(1)
#     surname = input('Фамилия: ')
#     if surname.lower() == 'exit':
#         exit(1)
#     phone = int(input('Телефон: '))
#     phone_book[(name.capitalize(), surname.capitalize())] = phone
#     print()
#     print(phone_book)


# names_list = ['Tom', 'Bob', 'Albert']
# ages = [20, 45, 70]
#
# peoples = tuple(zip(names_list, ages))
# print(peoples)
#
# peoples_2 = {
#     iname.lower(): iage + 10
#     for iname, iage in zip(names_list, ages)
# }
# print(peoples_2)


# Алгоритм поиска рабина картпа
# def rabin_karp_search(text, pattern):
#     # Проверяем случаи, когда текст или подстрока пустые
#     if not text or not pattern:
#         return []
#
#     # Вычисляем хеш-значение для подстроки и первого окна текста
#     pattern_hash = hash(pattern)
#     window_hash = hash(text[:len(pattern)])
#
#     matches = [] # Список индексов совпадений
#
#     # Проходим по тексту с помощью скользящего окна
#     for i in range(len(text) - len(pattern) + 1):
#         # Если хеш-значения совпадают, сравниваем каждый символ окна с подстрокой
#         if pattern_hash == window_hash and text[i:i + len(pattern)] == pattern:
#             # Стоит уточнить, что благодаря ленивому выполнению Python, если первое условие в связке AND вернёт False, то второе не будет запускаться вообще
#             matches.append(i)
#
#         # Обновляем хеш-значение для следующего окна
#         window_hash = hash(text[i + 1:i + len(pattern) + 1])
#
#     return matches
#
# # Пример использования
# text = "abracadabra"
# pattern = "cad"
# matches = rabin_karp_search(text, pattern)
# print(f"Совпадения найдены на позициях: {matches}")
