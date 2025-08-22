import time
from functools import wraps


def timing_decorator(func):
    """
    Декоратор, который измеряет время выполнения функции и выводит его.

    Args:
        func: Функция, время выполнения которой нужно измерить

    Returns:
        wrapper: Обернутая функция с измерением времени
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time:.6f} секунд")
        return result

    return wrapper


@timing_decorator
def count_divisible_numbers(divisor):
    """
    Функция, которая получает на вход число, а на выходе выдаёт количество чисел 
    от 1 до 1000000000 которые делятся на число на входе без остатка.

    Args:
        divisor (int): Число, на которое должны делиться числа из диапазона

    Returns:
        int: Количество чисел от 1 до 1000000000, делящихся на divisor без остатка
    """
    # Проверка на корректность входных данных
    if divisor <= 0:
        raise ValueError("Делитель должен быть положительным числом")

    # Подсчет количества чисел от 1 до 1000000000, делящихся на divisor
    # Это просто 1000000000 деленное на divisor (целочисленное деление)
    counter = 0
    for i in range(divisor, 1000000001):
        if i % divisor == 0:
            counter += 1

    return counter

digit = int(input("Введите делитель: "))
print(count_divisible_numbers(digit))

'''
Введите делитель: 152
Время выполнения функции count_divisible_numbers: 54.927401 секунд
6578946

Введите делитель: 152
Время выполнения функции count_divisible_numbers: 37.016877 секунд
6578947
'''