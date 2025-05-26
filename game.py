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