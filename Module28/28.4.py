import random
from itertools import count


# class RandomNumbers:
#     def __init__(self, limit):
#         self.__limit = limit
#         self.__counter = 0
#
#     def __next__(self):
#         if self.__counter < self.__limit:
#             self.__counter += 1
#             return random.randint(0, 10)
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         return self
#
# my_iter = RandomNumbers(limit=3)
# for num in my_iter:
#     print(num)
#
#


# # Стандартная функция
# def ficonacci(number):
#     result = []
#     cur_val = 0
#     next_val = 1
#     for _ in range(number):
#         result.append(cur_val)
#         cur_val, next_val = next_val, cur_val + next_val
#
#     return result
#
# print(ficonacci(10))

# class Fibonacci:
#     '''
#     Итератор последовательности фибоначчи из N элементов
#     '''
#
#     def __init__(self, number):
#         self.counter = 0
#         self.cur_val = 0
#         self.next_val = 1
#         self.number = number
#
#     def __iter__(self):
#         self.counter = 0
#         self.cur_val = 0
#         self.next_val = 1
#         return self
#
#     def __next__(self):
#         self.counter += 1
#         if self.counter > 1:
#             if self.counter > self.number:
#                 raise StopIteration
#             self.cur_val, self.next_val = self.next_val, self.next_val + self.cur_val
#
#         return self.cur_val
#
# fib_iterator = Fibonacci(10)
#
# for _ in fib_iterator:
#     print(_)
# print(7 in fib_iterator)

# Практика
# # Задача 1. Бесконечный итератор
# # Реализуйте итератор-счётчик, который не принимает никаких атрибутов и
# # имеет только один статический атрибут — счётчик.
# # Итератор увеличивает счётчик и возвращает предыдущее значение.
# # У вас должен получиться бесконечный итератор.
# #
# # То есть при вызове такого кода в основной программе
# #
# # my_iter = СountIterator()
# # for i_elem in my_iter:
# #     print(i_elem)
# #
# # значения будут выдаваться бесконечно.
#
# class СountIterator:
#
#     def __init__(self):
#         self.__counter = 0
#
#     def __iter__(self):
#         self.__counter = 0
#         return self
#
#     def __next__(self):
#         self.__counter += 1
#         return self.__counter - 1
#
# my_iter = СountIterator()
#
# for i_elem in my_iter:
#     print(i_elem)



# # Задача 2. Случайная сумма
# # Алексею по работе необходимо обрабатывать огромные массивы данных из миллионов элементов.
# # Каждый новый элемент — это сумма случайного вещественного числа от 0 до 1
# # и предыдущего элемента (первый элемент — просто случайное вещественное число от 0 до 1).
# # Алексею нельзя хранить в памяти весь этот список, а со значениями работать как-то надо.
# #
# # Помогите Алексею, реализуйте такой класс-итератор и проверьте его работу.
# # Также сделайте, чтобы при каждом новом вызове итератора в цикле значения считались заново.
# #
# # Пример работы программы:
# #
# # Кол-во элементов: 5
# # Элементы итератора:
# # 0.74
# # 1.13
# # 1.95
# # 2.2
# # 2.55
# # Новое кол-во элементов: 6
# # Элементы итератора:
# # 0.79
# # 1.58
# # 2.55
# # 2.81
# # 3.06
# # 3.34
#
# class InfinityAlexIterator(count):
#
#     def __init__(self, count):
#         self.__counter = 0
#         self.__count = count
#         self.__cur_num = round(random.random(), 2)
#         self.__next_num = round(random.random(), 2)
#
#     def __iter__(self):
#         self.__counter = 0
#         self.__cur_num = round(random.random(), 2)
#         self.__next_num = round(random.random(), 2)
#         return self
#
#     def __next__(self):
#         self.__counter += 1
#         if self.__counter > 1:
#             if self.__counter > self.__count:
#                 raise StopIteration
#             self.__cur_num += self.__next_num
#
#         return self.__cur_num
#
# try:
#     print('Кол-во элементов: ', end='')
#     while True:
#         my_iterator = InfinityAlexIterator(int(input()))
#         for _ in my_iterator:
#             print(_)
#         print('Новое кол-во элементов: ', end='')
# finally:
#     print('Bye!')

# Задача 3. Простые числа
# Реализуйте класс-итератор Primes, который принимает максимальное число N
# и выдаёт все простые числа от 1 до N.
#
# Основной код:
# prime_nums = Primes(50)
#
# for i_elem in prime_nums:
#     print(i_elem, end=' ')
#
# Ожидаемый результат кода:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

class Primes:

    def __init__(self, number):
        self.__number = number
        self.__cur_num = 0

    def __iter__(self):
        self.__cur_num = 1
        return self

    def __next__(self):
        while True:
            self.__cur_num += 1
            if self.__cur_num > self.__number:
                raise StopIteration

            is_prime = True
            if self.__cur_num < 2:
                is_prime = False
            else:
                for i in range(2, int(self.__cur_num ** 0.5) + 1):
                    if self.__cur_num % i == 0:
                        is_prime = False
                        break

            if is_prime:
                return self.__cur_num



prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')