# TODO здесь писать код
def print_all_nums(num: int) -> None:
    '''
    Функция, которая выводит все числа от 1 до num.
    :param num: Число от 1
    :return: None
    '''
    if number <= 0:
        print("Число должно быть положительным.")
        return None

    if num == 0:
        return None
    print_all_nums(num - 1)
    print(num)




number = int(input('Введите num: '))
print_all_nums(number)
