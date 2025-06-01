# class User:
#     user_name = 'Admin'
#     password = 'qwerty'
#     is_banned = False
#
# user_1 = User() # Экземпляр класса User
# user_2 = User()
# user_2.user_name = 'Tom'
# print(user_1.user_name, user_2.user_name)
# User.user_name = 'Noname'
# print(user_1.user_name, user_2.user_name)




# Практика
# """
# Задача 1. Машина
# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
#
# Цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости
# на случайное число от нуля до 200.
# """
#
# import random
#
#
# class Toyota:
#     color = 'red'
#     price = 1000000
#     max_speed = 200
#     current_speed = 0
#
# car_1 = Toyota()
# car_1.current_speed = random.randint(1, 201)
# car_2 = Toyota()
# car_2.current_speed = random.randint(1, 201)
# car_3 = Toyota()
# car_3.current_speed = random.randint(1, 201)
#
# print(car_1.current_speed,
#       car_2.current_speed,
#       car_3.current_speed,
#       sep='\n')




"""
Задача 2. Однотипные объекты
В офис заказали небольшую партию из четырёх мониторов и трёх наушников.
У монитора есть четыре характеристики: название производителя, матрица,
разрешение и частота обновления экрана. Все четыре монитора отличаются только частотой.

У наушников три характеристики: название производителя, чувствительность и наличие микрофона.
Отличие только в наличии микрофона.
"""

class Monitor:
    manufacturer = 'Samsung'
    type_of_matrix = 'VA'
    resolution = 'WQHD'
    frequency = '60'

class Headphones:
    manufacturer = 'Sony'
    sensitivity = '108'
    microphone = False

monitor_1 = Monitor()
monitor_2 = Monitor()
monitor_2.frequency = 144
monitor_3 = Monitor()
monitor_3.frequency = 70
monitor_4 = Monitor()

headphones_1 = Headphones()
headphones_2 = Headphones()
headphones_2.microphone =  True
headphones_3 = Headphones()
headphones_3.microphone =  True
