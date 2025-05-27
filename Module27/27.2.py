# class Person:
#     __count = 0     #Сокрытие данных "__" <- Инкопсуляция
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.set_age(age)
#         Person.__count += 1
#
#     def __str__(self):
#         return f"Имя: {self.__name}\tВозраст: {self.__age}"
#
#     def get_count(self):    #Геттер
#         return self.__count
#
#     def set_age(self, age): #Сеттер
#         if age in range(1, 90):
#             self.__age = age
#         else:
#             raise Exception("Недопустимый возраст")
#
#     def get_age(self):    #Геттер
#         return self.__age
#
#
#
# misha = Person("Misha", 20)
# tom = Person("Tom", 25)
# print(misha)
# print(misha.get_count())
# new_age = 80
# misha.set_age(new_age)
# print(misha.get_age())

# Задача 1. Координаты точки
# В одной из практик предыдущего модуля была задача на реализацию класса «Точка».
# Модернизируйте класс по следующему условию: объект «Точка» на плоскости имеет координаты x и y;
# при создании новой точки могут передаваться пользовательские значения координат, по умолчанию x = 0, y = 0.
#
# Реализуйте класс, который будет представлять эту точку, и напишите следующие методы:
#     1. Предоставление информации о точке (используйте магический метод str).
#     2. Геттер и сеттер для x.
#     3. Геттер и сеттер для y.
#
# Для сеттеров реализуйте проверку на корректность входных данных: координаты должны быть числом.

class Dot:

    def __init__(self, x = 0, y = 0):
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x):
        if isinstance(x, int):
            self.__x = x
        else:
            raise Exception('Координаты должны быть числом')

    def set_y(self, y):
        if isinstance(y, int):
            self.__y = y
        else:
            raise Exception('Координаты должны быть числом')

    def __str__(self):
        return f'x = {self.__x}, y = {self.__y}'

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

dot1 = Dot()
print(dot1)
dot2 = Dot(32, -1)
print(dot2)
dot3 = Dot('df', 6)
print(dot3)