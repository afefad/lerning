# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def print_info(self):
#         print(
#             f'Name: {self.name}\nSalary: {self.salary}\n'
#         )
#
# em_1 = Employee('Tom', 10000)
# em_1.print_info()
# em_2 = Employee('Bob', 20000)
# em_2.print_info()




# class Potato:
#     states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}
#
#     def __init__(self, index):
#         self.index = index
#         self.state = 0
#
#     def grow(self):
#         if self.state < 3:
#             self.state += 1
#         self.print_state()
#
#     def is_ripe(self):
#         if self.state == 3:
#             return True
#         return False
#
#     def print_state(self):
#         print(
#             f'Картошка {self.index} сейчас {Potato.states[self.state].lower()}'
#         )
# class PotatoGarden:
#
#     def __init__(self, count):
#         self.potatos = [Potato(index) for index in range(1, count + 1)]
#
#     def grow_all(self):
#         print(
#             'Картошка прорастает!'
#         )
#         for i_potato in self.potatos:
#             i_potato.grow()
#
#     def are_all_ripe(self):
#         if not all([i_potato.is_ripe() for i_potato in self.potatos]):
#             print('Картошка ещё не созрела!\n')
#         else:
#             print('Вся картошка созрела! Можно собирать\n')
#
#
# my_garden = PotatoGarden(5)
# my_garden.are_all_ripe()
#
# for _ in range(3):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()


# # Задача 1. Машина 3
# """
# Вам предстоит снова немного видоизменить класс Toyota из прошлого урока.
# На всякий случай вот описание класса.
#
# Четыре атрибута:
#
# Цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Два метода:
#
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса
# (то есть передаваться в init). Реализуйте такое изменение класса.
# """
# class Car:
#
#     def __init__(self, color: str, price: (int, float), max_speed: int =200, current_speed: int =0):
#         """
#         Создание новой машины
#
#         :param color: Цвет машины
#         :param price: Цена машины
#         :param max_speed: Максимальная скорость
#         :param current_speed: Текущая скорость
#         """
#         from random import randint
#         self.randint = randint
#
#         self.color = color
#         self.price = price
#         self.max_speed = max_speed
#         self.current_speed = current_speed
#
#     def info(self):
#         print(f'Car color: {self.color}\n'
#               f'Car price: {self.price}\n'
#               f'Car max speed: {self.max_speed}\n'
#               f'Car current speed: {self.current_speed}\n')
#
#     def acceleration(self):
#         if self.current_speed < self.max_speed - 10:
#             self.current_speed += self.randint(self.current_speed, self.max_speed) - self.current_speed
#             print('The acceleration was successfully completed.\n'
#                   f'Current car speed: {self.current_speed}\n')
#         else:
#             print('Acceleration is not required.\n'
#                   'The car is already going very fast!\n')
#
#     def braking(self):
#         if self.current_speed > 0:
#             self.current_speed -= self.randint(0, self.current_speed)
#             print('The braking was successfully completed.\n'
#                   f'Current car speed: {self.current_speed}\n')
#         else:
#             print('braking is not required.\n'
#                   'The car is already standing!\n')
#
# car_1 = Car('Blue', 120000)
#
# car_1.info()
#
# car_1.acceleration()
# car_1.acceleration()
# car_1.acceleration()
#
# car_1.braking()
# car_1.braking()
# car_1.braking()
# car_1.braking()

"""
Задача 2. Координаты точки
Объект «Точка» на плоскости имеет координаты X и Y.
При создании новой точки могут передаваться пользовательские значения координат, по умолчанию x = 0, y = 0.

Реализуйте класс, который будет представлять эту точку.
И напишите метод, который предоставляет информацию о ней.
Также внутри класса пропишите счётчик, который будет отвечать за количество созданных точек.

Подсказка: счётчик можно объявить внутри самого класса и увеличивать его в методе __init__.
"""

class Dot:
    counter = 0

    def __init__(self, x: (int, float) = 0, y: (int, float) = 0):
        self.x = x
        self.y = y
        Dot.counter += 1

    def info(self):
        print(
            f'x: {self.x}\n'
            f'y: {self.y}\n'
        )

    def dot_count(self):
        print(
            f'{self.counter} точек создано!\n'
        )

dot_1 = Dot(1, 3)
dot_2 = Dot(y=2)
dot_3 = Dot()

dot_1.info()
dot_3.info()
dot_1.dot_count()