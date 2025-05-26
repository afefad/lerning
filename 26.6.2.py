"""
Задача 2. Студенты
Что нужно сделать
Реализуйте модель с именем Student, содержащую поля «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
Затем создайте список из десяти студентов (данные о студентах можете придумать или запросить у пользователя)
и отсортируйте список по возрастанию среднего балла. Выведите результат на экран.

Что оценивается
Результат вычислений корректен.
Input содержит корректные приглашения для ввода.
Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
Сообщения о процессе получения результата осмысленны и понятны для пользователя.
Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.
"""
# TODO: Хуйня какая то, Доработать!!!.

from random import randint

class Student:

    def __init__(self, name: str, group_num: int, grades_list: dict):

        parts = name.split()
        if len(parts) != 3 or not all(part.isalpha() for part in parts):
            raise ValueError('При создании объекта класса Student, '
                             'name должно содержать ФИО через пробел (например, "Иванов Иван Иванович")')

        if not isinstance(group_num, int):
            raise TypeError('При создании обьекта класса Student, '
                            'group_num задаётся в численной форме.')

        if not isinstance(grades_list, dict):
            raise TypeError('При создании обьекта класса Student, '
                            'grades_list должен быть словарем.')
        elif len(grades_list) != 5:
            raise ValueError('При создании обьекта класса Student, '
                             'grades_list должен содержать ровно 5 пар ключ-значение')

        self.name = name
        self.grades_list = grades_list
        self.group_num = group_num

    def print_grades_list(self, grades_list: dict):
        print('\nЖурнал оценок.')
        for i_key, i_valie in grades_list.items():
            print(f'\t{i_key}:\t{i_valie}')

    def info(self):
        print(f'\nИнформация о студенте.'
              f'\nИмя: {self.name}'
              f'\nГруппа обучения: {self.group_num}')
        self.print_grades_list(self.grades_list)

    def gpa(self) -> float:
        """
        Считает средний балл студента и возвращает float.
        :return: Средний балл.
        """
        return sum(self.grades_list.values()) / len(self.grades_list.values())


def random_grades_list() -> dict:
    """
    Функция для создания случайного списка успеваемости.
    :return: Список успеваимости студента из 5 пар Ключ - Значение.
    """
    temp_dict = dict()
    school_subjects = ('Русский', 'Литература', 'Аглебра', 'Геометрия', 'Английский')

    for i_subject in school_subjects:
        temp_dict[i_subject] = randint(2, 5)

    return temp_dict

def create_students_list(quantity) -> list:
    students = []
    for i in range(quantity):
        globals()[f'student_{i + 1}'] = Student(names[i], randint(1,4), random_grades_list())
        students.append(globals()[f'student_{i + 1}'])
    return students

names = (
    "Иванов Иван Иванович",
    "Петров Петр Петрович",
    "Сидоров Сидор Сидорович",
    "Кузнецов Алексей Дмитриевич",
    "Смирнова Мария Викторовна",
    "Ковалев Анатолий Сергеевич",
    "Морозова Елена Павловна",
    "Николаев Игорь Владимирович",
    "Федорова Анастасия Андреевна",
    "Захаров Денис Олегович"
)
max = Student("Захаров Денис Олегович", randint(1,4), random_grades_list())
max.gpa()


average_grade_dict = {}
try:
    students = create_students_list(10)

    for i_stud in students:
        average_grade_dict[i_stud.name] = i_stud.gpa()
    sorted_grades = dict(sorted(average_grade_dict.items(), key=lambda item: item[1]))
    print(sorted_grades)


except:
    print('Что то пошло не так.')