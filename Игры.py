# Задача 5. Недоделка
import random


def rock_paper_scissors(user_name):
    # Здесь будет игра «Камень, ножницы, бумага»

    print(f'\n{user_name}, вы выбрали игру "КАМЕНЬ, НОЖНИЦЫ, БУМАГА!"')
    print('Правила очень простые: Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.\nВы играете против нашего суперсовременного ИИ способного предугадывать ваши действия.\nА для игры достаточно выбрать камень, ножницы или бумагу.\n')

    while True:
        random_number = random.randint(1, 3)
        print('1 - Камень\n2 - Ножницы\n3 - Бумага\n0 - выход из игры')

        choice = int(
            input('\nСделайте свой выбор: '))
        print()
        if choice == 0:
            print('Вы вышли из игры "КАМЕНЬ, НОЖНИЦЫ, БУМАГА!"\n')
            break
        elif not 0 < choice < 4:
            print('Введённое число должно быть от 0 до 3.')
            choice = int(input('\nСделайте свой выбор: '))
        elif choice == random_number:
            print('Ничья.')
        elif random_number == choice + 1 or random_number == choice - 2:
            print('Вы победили!')
        else:
            print('вы проиграли :(')

        if random_number == 1:
            print('У соперника был Камень')
        elif random_number == 2:
            print('У соперника были Ножницы')
        else:
            print('У соперника была Бумага')
        print()


def guess_the_number(user_name):
    # Здесь будет игра «Угадай число»

    print(f'\n{user_name}, вы выбрали игру "Угадай число!"')
    print('Правила очень простые: Наш ИИ запрашивает у пользователя число от 1 до 10 до тех пор, пока он не угадает загаданное.\n')
    print(f'0 - для выхода')
    # Генерация случайного числа от 1 до 10 (включительно)

    random_number = random.randint(1, 10)
    user_input = int(input('Введите число: '))

    while user_input != random_number:
        if user_input == 0:
            print('Вы вышли из игры "Угадай число!"\n')
            break
        elif not 0 < user_input < 11:
            print('Введённое число должно быть от 1 до 10.\n')
            user_input = int(input('Введите число: '))

        print('Введённое число не совпадает с загаданным, попробуйте ещё раз.\n')
        user_input = int(input('Введите число: '))
    else:
        print(f'Поздравляем вас {user_name}, вы угадали загаданное число!')


def main_menu():
    print('\nРады вас видеть в нашей уютной игровой комнате!')
    user_name = input('Как вас зовут?\n')
    print(f'\nПриветствуем вас {user_name}!')
    while True:
        print('На выбор пока что есть только 2 игры.')
        print('\n1 - Камень, Ножницы, Бумага\n2 - Угадай число\n')
        game = int(
            input('Выберите игру: '))
        if game == 1:
            rock_paper_scissors(user_name)
        elif game == 2:
            guess_the_number(user_name)


main_menu()
