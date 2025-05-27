# class Pet:
#     legs = 4
#     has_tail = True
#
#     def __str__(self):
#         tail = 'да' if self.has_tail else 'нет'
#         return 'Всего ног: {legs}\nХвост присутствует - {has_tail}'.format(
#             legs=self.legs,
#             has_tail=tail
#         )
#
# class Cat(Pet):
#
#     def sound(self):
#         print('Мяу!')
#
#
# class Dog(Pet):
#
#     def sound(self):
#         print('Гав!')
#
# class Frog(Pet):
#
#     has_tail = False
#     def sound(self):
#         print('Ква!')
#
#
# cat = Cat()
# dog = Dog()
# frog = Frog()
# print(cat)
# print(dog)
# print(frog)
# cat.sound()
# dog.sound()
# frog.sound()

#
# ------------------------------------//------------------------------------
#
# class Ship:
#     def __init__(self, model):
#         self.__model = model
#
#     def __str__(self):
#         return "\nМодель коробля {}.".format(
#             model = self.__model
#         )
#
#     def sail(self):
#         print('\nКорабль куда-то по плыл!')
#
# class WarShip(Ship):
#     def __init__(self, model, gun):
#         super().__init__(model)
#         self.gun = gun
#
#     def attack(self):
#         print('\nКорабль атакует с помощью оружия "{}"'.format(self.gun))
#
# class CargoShip(Ship):
#
#     def __init__(self, model):
#         super().__init__(model)
#         self.tonnage_load = 0
#
#     def load(self):
#         print('\nЗагружаем корабль.')
#         self.tonnage_load += 100
#         print(f'Текущая загруженность {self.tonnage_load} тонн')
#
#     def unload(self):
#         print('\nРазгружаем корабль.')
#         if self.tonnage_load >= 100:
#             self.tonnage_load -= 100
#         elif 0 < self.tonnage_load < 100:
#             self.tonnage_load = 0
#         else:
#             print('Корабль уже разгружен!')
#
#         print('\nТекущая загруженность {} тонн'.format(
#             self.tonnage_load
#         ))
#
# warship = WarShip('Крёсный-2', 'Эрекция')
# warship.attack()
# warship.sail()
#
# cargoship = CargoShip('qwe3')
# cargoship.load()



# Практика
# Задача 1. Автомобили
# Даны два класса автомобилей: грузовой и легковой. У каждого из этих автомобилей есть своя модель,
# и каждый может сделать два действия: сообщить свою модель и поехать.
#
# Грузовой автомобиль имеет такой атрибут, как заполненность багажника, изначально он равен нулю.
# У него есть ещё два действия: загрузить и разгрузить багажник.
#
# У легкового автомобиля нет багажника, но есть навигационная система, которая передаётся вместе с моделью.
# Также вместо загрузки и разгрузки у него есть другое действие — включить навигацию.
#
# Реализуйте классы грузового и легкового автомобилей. Для этого выделите общие атрибуты и
# методы в отдельный класс «Автомобиль» и используйте наследование.
# Не забудьте о функции super в дочерних классах.

class Car:

    def __init__(self, model):
        self.model = model

    def info(self):
        print(f'\nМодель: {self.model}')

    def drive(self):
        print(f'\n{self.model} куда то поехал.')

class CargoCar(Car):

    def __init__(self, model):
        super().__init__(model)
        self.tonnage_load = 0

    def load(self):
        print('\nЗагружаем Кузов.')
        self.tonnage_load += 100
        print(f'Текущая загруженность {self.tonnage_load}Кг')

    def unload(self):
        print('\nРазгружаем кузов.')
        if self.tonnage_load >= 100:
            self.tonnage_load -= 100
        elif 0 < self.tonnage_load < 100:
            self.tonnage_load = 0
        else:
            print('Кузов уже разгружен!')

        print('\nТекущая загруженность {}Кг'.format(
            self.tonnage_load
        ))
    def __str__(self):
        return f'\nГрузовой автомобиль.\nМодель: {self.model}\nЗагрузка: {self.tonnage_load}'

class Auto(Car):

    __navigation = False
    def __init__(self, model, navigation):
        super().__init__(model)
        self.navigation = navigation

    def turn_on_navigation(self):
        if self.__navigation == False:
            self.__navigation = True
        else:
            print('\nНавигация уже включена!')

    def turn_off_navigation(self):
        if self.__navigation == True:
            self.__navigation = False
        else:
            print('\nНавигация уже выключена!')

    def __str__(self):

        return f'\nЛегковой автомобиль.\nМодель: {self.model}\nМодель навигации: {self.navigation}' + '\nНавигация: {}'.format(self.__navigation)


cargocar1 = CargoCar('Камаз')

cargocar1.info()
cargocar1.load()
print(cargocar1)

normalcar = Auto('LADA', 'Navitel')

normalcar.drive()
normalcar.turn_on_navigation()
print(normalcar)
normalcar.turn_off_navigation()
print(normalcar)