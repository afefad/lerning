# phonebook_dict = {
#     'Ваня': 88005553535,
#     'Петя': 88006663636,
#     'Лена': 88007773737
# }
#
# name = input('Введите имя: ')
# if name in phonebook_dict:
#     print(phonebook_dict[name])
# else:
#     print('Error! человек с именем "{0}" не найден!'.format(name))



# def add_stud():
#     stud_str = input('Information about student\n'
#                      '(name, lastname, city, university, assessment):\n')
#     stud_info = stud_str.split()
#
#     student = dict()
#     student['Имя'] = stud_info[0]
#     student['Фамилия'] = stud_info[1]
#     student['Город'] = stud_info[2]
#     student['Место учебы'] = stud_info[3]
#     student['Оценки'] = stud_info[4:]
#
#     print('В список добавлен студент:')
#
#     for i_info in student:
#         print('{0} - {1}'.format(i_info, student[i_info]))
#
#     students.append(student)
#
# students = list()
# add_stud()
#
# print(students)


# def histogram(string :str):
#     sym_dict = dict()
#     for sym in string:
#         if sym == ' ':
#             continue
#         elif sym in sym_dict:
#             sym_dict[sym] += 1
#         else:
#             sym_dict[sym] = 1
#
#     return sym_dict
#
# text = input('Введите текст: ').lower()
# hist = histogram(text)
#
# for i_sym in sorted(hist.keys()):
#     print(f'{i_sym} : {hist[i_sym]}')
#
# print(f'Максимальная частота: {max(hist.values())}')


# phonebook = {
#     'Ваня' : 100,
#     'Петя' : 200,
#     'Алиса' : 300
# }
#
# other_phonebook = {
#     'Игорь' : 1000,
#     'Петя' : 800,
#     'Алена' : 2000
# }
#
# phonebook.update(other_phonebook)
# print(phonebook)
#
# phonebook['Гоша'] = phonebook.pop('Игорь')
# print(phonebook)
# print(phonebook.get('Степан'))


# # {
# #     "server": {
# #         "host": "127.0.0.1",
# #         "port": "10"
# #     },
# #     "configuration": {
# #         "ssh": {
# #             "access": "true",
# #             "login": "Ivan",
# #             "password": "qwerty"
# #         }
# #     }
# # }
# data = dict()
# # До этого что-то происходит
# print(data.get('server'))
#
# data['server'] = {
#         'host': '127.0.0.1',
#         'port': "10"
# }
# # До этого что-то происходит
# if data.get('configuration', {}).get('ssh', {}).get('login', {}):
#     print('В структуре уже есть логин!')
#
# data['configuration'] = {
#     'ssh': {
#         'access': 'true',
#         'login': 'Ivan',
#         'password': 'qwerty'
#     }
# }
#
# print(data)
# # print(data['server']['port'])
# #
# # data['configuration']['ssh']['login'] = 'Gennadiy'
# # print(data['configuration']['ssh'])
# # print()
# #
# # for i_value in data.values():
# #     for j_key in i_value:
# #         print(f'{j_key}: {i_value[j_key]}')


# player_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
#
# team_a_members = [
#     player['name']
#     for player in player_dict.values()
#     if player['team'] == 'A' and player['status'] == 'Rest'
# ]
#
# print(team_a_members)


# order = {
#     'apple': 2,
#     'banana': 3,
#     'pear': 1,
#     'watermelon': 10,
#     'chocolate': 5
# }
#
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# total = 0
# for i_fruit in order:
#     if incomes.get(i_fruit, {}):
#         total += incomes.get(i_fruit) * order[i_fruit]
# print(f'Сумма заказа: {total}')


player_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

team_a_members = [
    player['name']
    for player in player_dict.values()
    if player['team'] == 'A' and player['status'] == 'Rest'
]
print(team_a_members)

team_b_members = [
    player['name']
    for player in player_dict.values()
    if player['team'] == 'B' and player['status'] == 'Training'
]
print(team_b_members)

team_c_members = [
    player['name']
    for player in player_dict.values()
    if player['team'] == 'C' and player['status'] == 'Travel'
]
print(team_c_members)