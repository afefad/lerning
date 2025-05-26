# class User:
#     user_name = 'Admin'
#     password = 'qwerty'
#     is_banned = False
#     friends = []
#
#     def print_info(self):
#         print('Name: {}\nPassword: {}\nBan status: {}\nFriends: {}'.format(
#             self.user_name, self.password, self.is_banned, self.friends))
#
#     def add_friend(self, friend):
#         if isinstance(friend, User):
#             self.friends.append(friend.user_name)
#         else:
#             self.friends.append(friend)
#
#
# user_1 = User()
# user_1.add_friend('Bob')
#
# user_2 = User()
# user_2.user_name = 'Alina'
#
# user_1.add_friend(user_2)
#
# user_1.print_info()




# class Family:
#     surname = 'Common family'
#     money = 100000
#     have_a_house = False
#
#     def info(self):
#         print(f'Family name {self.surname}\n'
#               f'Family funds: {self.money}\n'
#               f'Having a house: {self.have_a_house}\n')
#
#     def earn_money(self, amount):
#         self.money += amount
#         print(f'Earn {amount} money! Current money: {self.money}')
#
#     def buy_house(self, house_price, discount=0):
#         house_price -= house_price * discount / 100
#         if self.money >= house_price:
#             self.money -= house_price
#             self.have_a_house = True
#             print(f'House Purchased! Current money: {self.money}\n')
#         else:
#             print('Not enough money!\n')
#
# my_family = Family()
# my_family.surname = 'Zelentsovy'
# my_family.info()
#
# print('Try to buy a house')
# my_family.buy_house(10 ** 6)
#
# if not my_family.have_a_house:
#     my_family.earn_money(800000)
#     print('Try to buy a house again')
#     my_family.buy_house(10 ** 6, 10)
#
# my_family.info()




# Практика
# """
# Задача 1. Машина 2.
# Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
#
# Цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
#
# Добавьте два метода класса:
#
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Проверьте работу этих методов.
# """
#
# class Toyota:
#     color = 'red'
#     price = 1000000
#     max_speed = 200
#     current_speed = 0
#
#     def __init__(self):
#         from random import randint
#         self.randint = randint
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
# car_1 = Toyota()
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
