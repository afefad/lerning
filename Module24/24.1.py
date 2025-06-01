import os

# folder_name = 'project'
# file_name = 'my_file.txt'
#
# path = 'docs/{folder}/{file}'.format(
#     folder=folder_name,
#     file=file_name
# )
#
# print(path)
#
# rel_path = os.path.join('docs', folder_name, file_name)
# print(rel_path)
#
# abs_path = os.path.abspath(file_name)
# print(abs_path)




# print(os.path.abspath('My_penus'))
#
# project_list = ['PyCharm', 'Stepik']
#
# def print_dirs(project):
#     print('\nСодержимое директории', project)
#     for i_elem in os.listdir(project):
#         path = os.path.join(project, i_elem)
#         print('\t', path)
#
# for i_proj in project_list:
#     path_to_project = os.path.abspath(os.path.join('..', i_proj))
#     print_dirs(path_to_project)



# '''
# Задача 1. Сисадмин
# Вы работаете системным администратором в одной компании. На диске каждого сотрудника компании в специальной
# папке access лежит файл admin.bat. Этот файл предназначен для вас, и вам нужен путь до этого файла,
# причём как относительный, так и абсолютный. Недолго думая, вы решили написать небольшой скрипт,
# который закинете по сети к этому файлу.
#
# Напишите программу, которая выводит на экран относительный и абсолютный пути до файла admin.bat.
#
# Пример результата:
#
# Абсолютный путь до файла: C:\\Users\\Roman\\PycharmProjects\\Skillbox\\access\\admin.bat
#
# Относительный путь до файла: Skillbox\\access\\admin.bat
# '''
# abs_path = os.path.abspath(os.path.join('C:', '%HOMEPATH%', 'PycharmProjects', 'Skillbox', 'access', 'admin.bat'))
# relative_path = os.path.join('Skillbox', 'access', 'admin.bat')
#
# print('Абсолютный путь до файла: {}'.format(abs_path))
# print('Относительный путь до файла: {}'.format(relative_path))



# '''
# Задача 2. Содержимое
# Выберите любую директорию на своём диске и затем напишите программу,
# выводящую на экран абсолютные пути к файлам и папкам, которые находятся внутри этой директории.
#
# Результат программы на примере директории проекта python_basic:
#
# Содержимое каталога G:\PycharmProjects\python_basic
#     G:\PycharmProjects\python_basic\.git
#     G:\PycharmProjects\python_basic\.idea
#     G:\PycharmProjects\python_basic\Module14
#     G:\PycharmProjects\python_basic\Module15
#     G:\PycharmProjects\python_basic\Module16
#     G:\PycharmProjects\python_basic\Module17
#     G:\PycharmProjects\python_basic\Module18
#     G:\PycharmProjects\python_basic\Module19
#     G:\PycharmProjects\python_basic\Module20
#     G:\PycharmProjects\python_basic\Module21
#     G:\PycharmProjects\python_basic\Module22
# '''
#
# dir_for_DEgenerate = os.path.join("C:", os.sep, 'Games')
#
# def print_dirs(project):
#     print('Содержимое каталога {}'.format(project))
#     for _ in os.listdir(project):
#         path = os.path.join(project, _)
#         print('\t', path)
#
# if os.path.exists(dir_for_DEgenerate):
#     print_dirs(dir_for_DEgenerate)
# else:
#     print(f"Путь {dir_for_DEgenerate} не существует.")



# '''
# Задача 3. Корень диска
# Напишите программу, которая выводит на экран только корень диска, на котором запущен скрипт.
# Учтите, что скрипт может быть запущен где угодно и при любой вложенности папок.
#
# Результат программы на примере диска G:
#
# Корень диска: G:\\
# '''
#
# dir_root = os.path.abspath(os.sep)
# print(dir_root)