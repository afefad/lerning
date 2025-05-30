# my_list = [1, 2, 3, 4]
# iterator = iter(my_list)
#
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

# Задача 1. Свой for (ну почти)
# Дан любой итерируемый объект, например список из N чисел.
# Реализуйте функцию, которая эмулирует работу цикла for с помощью цикла while и проходит во всем элементам
# итерируемого объекта. Не забудьте про исключение «конца итерации».

def my_for_loop(iterable):
    # Получаем итератор из итерируемого объекта
    iterator = iter(iterable)

    while True:
        try:
            # Получаем следующий элемент
            item = next(iterator)
            print(item)  # или любое другое действие с элементом
        except StopIteration:
            # Конец итерации
            break


# Пример использования:
my_list = [1, 2, 3, 4, 5]
my_for_loop(my_list)