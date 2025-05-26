# import random
#
# numbers_list = [random.randint(1,4) for _ in range(10)]
# # new_list = []
# # for i in numbers_list:
# #     if i not in new_list:
# #         new_list.append(i)
# # print(numbers_list)
# # print(new_list)
# # А вот как сделать это всё проще
#
# unic = set(numbers_list)
# print(numbers_list)
# print(unic)
from numpy.ma.extras import unique

# sym_list = set(".,;:!?")
# string_1 = input('Введите строку: ')
# count = sum(1 for char in string_1 if char in sym_list)
# print('Количество знаков пунктуации:', count)

# import random
#
# def process_nums(nums):
#     new_set = set(nums)
#     new_set.remove(min(new_set))
#     new_set.add(random.randint(100, 200))
#     return new_set
#
# nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
# nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
#
# new_nums_1 = process_nums(nums_1)
# new_nums_2 = process_nums(nums_2)
#
# print(new_nums_2 | new_nums_1)
# print(new_nums_2 & new_nums_1)
# print(new_nums_2 - new_nums_1)


# data = [
#     {'id':10, 'user': 'Bob'},
#     {'id':11, 'user': 'Misha'},
#     {'id':12, 'user': 'Anton'},
#     {'id':10, 'user': 'Bob'},
#     {'id':11, 'user': 'Misha'}
# ]
#
# unique_data = []
#
# for i_dict in data:
#     data_exists = False
#     for uniq_dict in unique_data:
#         if uniq_dict['id'] == i_dict['id']:
#             data_exists = True
#             break
#     if not data_exists:
#         unique_data.append(i_dict)
#
# print(unique_data, '\n')
#
# unique_data_dict = {i_dict['id']: i_dict for i_dict in data }
# print(unique_data_dict.values())


# scores_dict = {
#     'vanya': 33,
#     'petya': 60,
#     'lena': 45
# }
#
# for i_name, i_score in scores_dict.items():
#     print(i_name, i_score)

# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# for i_fruit, i_price in incomes.items():
#     print(f'{i_fruit.capitalize()} -- {i_price}')


# server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
# }
#
# for i_item, i_inner in server_data.items():
#     print(f'{i_item.capitalize()}:')
#     for i_stat, i_result in i_inner.items():
#         print(f'    {i_stat}: {i_result}')
#     print()

# # Улучшение кода, был такой:
# print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19} if i_key % 2 == 0])
# # Стал такой:
# print([i_item for i_key, i_item in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])


# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678'
# }
#
# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},              # Результаты работы программы
#     ],                                              # Лампа - 27 шт, стоимость 1134 руб.
#     '23456': [                                      # Стол - 54 шт, стоимость 27860 руб.
#         {'quantity': 22, 'price': 510},             # Диван - 3 шт, стоимость 3550 руб.
#         {'quantity': 32, 'price': 520},             # Стул - 105 шт, стоимость 10311 руб.
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150},
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97},
#     ],
# }
#
# for i_title, i_code in goods.items():
#     total_quantity = 0
#     total_cost = 0
#     for j_good in store[i_code]:
#         total_quantity += j_good['quantity']
#         total_cost += j_good['price'] * j_good['quantity']
#     print('{title} - {quantity} шт, стоимость {cost} руб.'.format(
#         title = i_title,
#         quantity = total_quantity,
#         cost = total_cost
#     ))
