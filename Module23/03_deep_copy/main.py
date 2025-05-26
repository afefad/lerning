site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

# TODO здесь писать код
import copy

def code_print(site: dict, tab_counter: int = 0) -> None:
    """
    Наглядно печатает структуру словаря переданного в функцию.

    :param site: Передаётся словарь.
    :param tab_counter: Сколько отступов нужно поместить перед структурой
    :return: None
    """
    tab = '\t'
    keys = list(site.keys())
    last_index = len(keys) - 1
    for index, i_key in enumerate(keys):
        i_value = site[i_key]

        if isinstance(i_value, dict):
            print(tab * tab_counter, "'{}':".format(i_key), " {", sep='')
            tab_counter += 1
            code_print(i_value, tab_counter)
            print(tab * (tab_counter - 1), '}', sep='', end='')
        elif isinstance(i_value, str):
            print(tab * tab_counter, "'{}': '{}'".format(i_key, i_value), sep='', end='')

        if index != last_index:
            print(',')
        else:
            print()
    tab_counter -= 1

def update_key_recursively(data: dict,
                           target_key: str,
                           new_value: str) -> None:
    """
    Функция которая меняет значение ключа в словарях рекурсивно на любую глубину.

    :param data: Словарь для замены ключа.
    :param target_key: Ключ для замены значения
    :param new_value: Новое значение для ключа.

    :return: None
    """
    if isinstance(data, dict):
        for i_key, i_value in data.items():
            if i_key == target_key:
                data[i_key] = new_value
            else:
                update_key_recursively(i_value, target_key, new_value)

def create_new_site(dicts_list: dict,
                    site_for_copy: dict,
                    counter: int) -> None:
    """
    Функция для создания списка сайтов по продаже телефонов.


    :param dicts_list: Список для добавления сайта.
    :param site_for_copy: Список с примером структуры сайта.
    :param counter: Сколько сайтов надо создать и добавить список сайтов.
    :return: None
    """
    while counter != 0:
        site_copy = copy.deepcopy(site_for_copy)
        product = input('Введите название продукта для нового сайта: ')
        product_string = f'У нас самая низкая цена на {product}'
        tagret_key = 'h2'
        update_key_recursively(site_copy, tagret_key, product_string)
        dicts_list[product] = site_copy
        for i_key in dicts_list.keys():
            print(f'Сайт для {i_key}:')
            print('site = {')
            code_print(dicts_list[i_key], 2)
            print('}')
            print()
        counter -= 1




sites_count = int(input('Сколько сайтов: '))
sites_dict = {}
create_new_site(sites_dict, site, sites_count)
