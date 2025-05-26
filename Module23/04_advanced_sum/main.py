# TODO здесь писать код
def find_nums_in_str(text: str) -> list:
    """
    Извлекает цифры из строки и возвращает их списком.

    :param text: Входная строка, содержащая текст и числа.
    :return: Список отдельных чисел.
    """
    numbers, buffer = [], ""
    for char in text:
        if char.isdigit():
            buffer += char
        elif buffer:
            numbers.append(int(buffer))
            buffer = ""
    if buffer:
        numbers.append(int(buffer))
    return numbers

def sum(*args) -> int:
    """
    Функция получает любые данные, ищет в них цифры, складывает и возвращает результат.

    :param args: Любой тип данных в любом количестве.
    :return: Результат сложения всех найденных чисел в данных.
    """
    total = 0
    for data in args:
        if isinstance(data, int) or isinstance(data, float):
            total += data
        elif isinstance(data, str):
            numbers_in_str = find_nums_in_str(data)     # Тут можно было использовать регулярные выражения,
            for i_item in numbers_in_str:               # но я решил написать свою функцию для поиска чисел.
                total += i_item
        elif isinstance(data, (list, tuple, set)):
            for i_item in data:
                total += sum(i_item)
        elif isinstance(data, dict):
            for i_key, i_value in data.items():
                total += sum(i_key)
                total += sum(i_value)
    return total




num_list = [1, 2, 3]                    # Сумма цифр = 6
num_tuple = (9, 8, 3)                   # Сумма цифр = 20
num_set = {4, 8, 12}                    # Сумма цифр = 24
nums_str = '12 + 100 сколько будет.'    # Сумма цифр = 112
nums_dict = {'first 1': 12, 'second': 24, 'num_list': num_list, num_tuple: 'key', 'num_set': num_set} # Сумма цифр = 87

print(sum(nums_dict, nums_str, num_set, num_tuple, num_list))   # Выдаст 249
