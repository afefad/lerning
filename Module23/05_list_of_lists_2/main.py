nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

# TODO здесь писать код

def list_compilation(data: list) -> list:
    """
    Раскрывает все вложенные списки, оставляет только внешний список.

    :param data: Принимает list.
    :return: Один общий список.
    """
    temp_list = []

    def flatten(current_data):
        if isinstance(current_data, list):
            for i_elem in current_data:
                flatten(i_elem)
        else:
            temp_list.append(current_data)

    flatten(data)
    return temp_list




print(list_compilation(nice_list))
