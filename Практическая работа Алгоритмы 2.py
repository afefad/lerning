# Задача 1


def summa_n(a):
    summ = 0
    for i in range(1, a + 1):
        summ += i
    return summ


n = int(input('Введите число: '))
print(summa_n(n))


# Задача 2

def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


def neutral():
    print('Ноль не является ни положительным, ни отрицательным')


def test():
    number = int(input('Введите число: '))
    if number > 0:
        positive()
    elif number < 0:
        negative()
    else:
        neutral()


test()


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


# Задача 4

# Тело функции которая считает, сколько раз в тексте встречается любая выбранная буква или цифра.
def count_letters():
    text = input('Введите текст: ').lower()
    digit = input('Какую цифру ищем? ')
    while not digit.isdigit():
        print("Ошибка: введите одну цифру от 0 до 9.")
        digit = input('Какую цифру ищем? ')
    letter = input('Какую букву ищем? ').lower()

    digit_counter = 0
    letter_counter = 0

    for _ in text:
        if digit == _:
            digit_counter += 1
        if letter == _:
            letter_counter += 1

    print('Количество цифр ', {digit}, ': ', {digit_counter}, sep='')
    print('Количество букв ', {letter}, ': ', {letter_counter}, sep='')


# Вызов функции
count_letters()


# Задача 5


def rock_paper_scissors():
    # Здесь будет игра «Камень, ножницы, бумага»

    print('Вы выбрали игру "КАМЕНЬ, НОЖНИЦЫ, БУМАГА!"')
    print('Правила очень простые: Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.')
    print('Выберете камень, ножницы или бумагу.')
    print()

    while True:
        pc_number = 1
        print('1 - Камень')
        print('2 - Ножницы')
        print('3 - Бумага')
        print('0 - выход из игры')

        choice = int(input('Сделайте свой выбор: '))
        print()

        if choice == 0:
            print('Вы вышли из игры КАМЕНЬ, НОЖНИЦЫ, БУМАГА!')
            print()
            break
        elif not 0 < choice < 4:
            print('Введённое число должно быть от 0 до 3.')
            print()
            choice = int(input('Сделайте свой выбор: '))
        elif choice == pc_number:
            print('Ничья.')
        elif (choice == 1 and pc_number == 2) or (choice == 2 and pc_number == 3) or (choice == 3 and pc_number == 1):
            print('Вы победили!')
            print('У соперника был Камень')
        else:
            print('вы проиграли :(')
            print('У соперника был Камень')



        print()


def guess_the_number(user_name):
    # Здесь будет игра «Угадай число»

    print('Вы выбрали игру "Угадай число!"')
    print('Правила простые вам нужно угадать число от 1 до 10')
    print('0 - для выхода')
    print()

    random_number = 8
    user_input = int(input('Введите число: '))

    while user_input != random_number:
        if user_input == 0:
            print('Вы вышли из игры "Угадай число!"')
            print()
            break
        elif not 0 < user_input < 11:
            print('Введённое число должно быть от 1 до 10.')
            print()
            user_input = int(input('Введите число: '))

        print('Введённое число не совпадает с загаданным, попробуйте ещё раз.')
        print()
        user_input = int(input('Введите число: '))
    else:
        print('Поздравляем вас', user_name, 'вы угадали загаданное число!')


def main_menu():
    print()
    print('Рады вас видеть в нашей уютной игровой комнате!')
    user_name = input('Как вас зовут?\n')
    print()
    print('Приветствуем вас ', user_name, '!' , sep='')
    while True:
        print()
        print('Выберите игру.')
        print()
        print('1 - Камень, Ножницы, Бумага')
        print('2 - Угадай число')
        print()
        game = int(
            input('Выберите игру: '))
        if game == 1:
            print()
            rock_paper_scissors()
        elif game == 2:
            print()
            guess_the_number(user_name)
        elif game == 0:
            exit()
        else:
            print('Введённое число должно быть 1 или 2.')
            print()


main_menu()
