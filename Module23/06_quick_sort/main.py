# TODO здесь писать код

example_list = [5, 8, 9, 4, 2, 9, 1, 8]

def fragmentation(data: list):
    """
    Быстрая сортировка списка от меньшего к большему.

    :param data: Список для сортировки.
    :return: Новый список.
    """
    if not data:
        return [], [], []

    lower, equal, greater = [], [], []
    support_element = data[-1]

    for i_element in data:
        if i_element < support_element:
            lower.append(i_element)
        elif i_element == support_element:
            equal.append(i_element)
        else:
            greater.append(i_element)

    return lower, equal, greater

def quick_sort(data):
    if len(data) <= 1:
        return data

    less, equal, greater = fragmentation(data)

    sorted_less = quick_sort(less)
    sorted_greater = quick_sort(greater)
    return sorted_less + equal + sorted_greater


print(quick_sort(example_list))
