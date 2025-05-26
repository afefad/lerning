# Задача 3

# Функция для нахождения суммы цифр
def summ_of_digits(a):
    summ = 0
    while a > 0:
        last_digit = a % 10
        summ += last_digit
        a = a // 10
    return summ


# Функция для нахождения максимальной цифры
def max_digit(a):
    mx_digit = 0
    while a > 0:
        if a % 10 > mx_digit:
            mx_digit = a % 10
        a = a // 10
    return mx_digit


# Функция для нахождения минимальной цифры
def min_digit(a):
    mn_digit = 9
    while a > 0:
        if a % 10 < mn_digit:
            mn_digit = a % 10
        a = a // 10
    return mn_digit


# Блок ввода информации    

while True:
    num = int(input('Введите число (или 0 для выхода): '))
    if num == 0:
        print('Выход из программы.')
        break
    print('Введите номер действия:')
    print('1 - сумма цифр')
    print('2 - максимальная цифра')
    print('3 - минимальная цифра: ', end='')
    choose = int(input())
    if choose == 1:
        print('\nСумма цифр:', summ_of_digits(num))
        print()
    elif choose == 2:
        print('\nМаксимальная цифра:', max_digit(num))
        print()
    elif choose == 3:
        print('\nМинимальная цифра:', min_digit(num))
        print()