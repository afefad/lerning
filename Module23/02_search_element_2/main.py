# TODO здесь писать код

def searching(
        key: str,
        data: dict,
        search_depth: int =-1):
    """
    Рекурсивно ищет ключ в словаре на заданной глубине.

    :param key: Ключ, который нужно найти в словаре.
    :param data: Словарь, в котором выполняется поиск.
    :param search_depth: Максимальная глубина поиска. Если -1, глубина не ограничена.
    :return: Значение найденного ключа или None, если ключ не найден.
    """
    if search_depth == 0:
        return None
    elif search_depth > 0:
        search_depth -= 1

    if not isinstance(data, dict):
        return None

    for i_element in data.keys():
        if i_element == key:
            return data[key]
        elif isinstance(data[i_element], dict):
            result = searching(key, data[i_element], search_depth)
            if result is not None:
                return result


def search_with_the_specified_depth(key: str, data: dict) -> None:
    """
    Запрашивает у пользователя выбор глубины поиска и выводит значение найденного ключа.

    :param key: Ключ, который нужно найти в словаре.
    :param data: Словарь, в котором выполняется поиск.
    """
    while True:
        choice = input('Хотите ввести максимальную глубину? Y/N: ')
        if choice.lower() in ('yes', 'y', 'д', 'да'):
            search_depth = int(input('Введите максимальную глубину: '))
            print('Значение ключа: {}'.format(searching(key, data, search_depth)))
            break
        elif choice.lower() in ('no', 'n', 'н', 'нет'):
            print('Значение ключа: {}'.format(searching(key, data)))
            break
        else:
            print('Пожалуйста введите ответ.')




site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

while True:
    key_for_search = input('Введите искомый ключ: ')
    if key_for_search:
        search_with_the_specified_depth(key_for_search, site)
