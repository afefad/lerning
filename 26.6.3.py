"""
Задача 3. Отцы, матери и дети
Что нужно сделать
Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:

имя,
возраст,
список детей.
И он может:

сообщить информацию о себе,
успокоить ребёнка,
покормить ребёнка.

У ребёнка есть:

имя,
возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
состояние спокойствия,
состояние голода.
Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг», и словарь состояний, и что-то поинтереснее.

Что оценивается
Результат вычислений корректен.
Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.
"""

class Parent:

    def __init__(self, name: str, age: int, child_list: list):
        self.name = name
        self.age = age
        self.child_list = child_list

    def info(self):
        print(f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Childrens:\n{self.child_list}\n')

    def feed_the_child(self, child):

    def calm_the_child(self, child):

class Child:
    calm_states = ['Спокоен', 'Возбуждён', 'Реактивный']
    hunger_states = ['Голоден', 'Сыт', 'Переел']

    def __init__(self, name: str, age: int, state_of_calm = calm_states[0], state_of_hunger = hunger_states[1]):
        self.name = name
        self.age = age
        self.state_of_calm = state_of_calm
        self.state_of_hunger = state_of_hunger