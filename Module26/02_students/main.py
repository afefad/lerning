from random import randint

class Student:
    """
    Класс для создания студента!
    """
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

    def print_grades_list(self):
        """
        Вывод оценок выбранного студента.
        :return:
        """
        print('\nЖурнал оценок.')
        for i_key, i_value in self.grades_list.items():
            print(f'\t{i_key}:\t{i_value}')

    def info(self):
        """
        Вывод информации о студенте.
        :return:
        """
        print(f'\nИнформация о студенте.'
              f'\nИмя: {self.name}'
              f'\nГруппа обучения: {self.group_num}')
        self.print_grades_list()

    def gpa(self) -> float:
        """
        Считает средний балл студента и возвращает float.
        :return: Средний балл.
        """
        return sum(self.grades_list.values()) / len(self.grades_list.values())


class Group:
    """
    Класс для представления группы студентов.
    """
    def __init__(self, group_num: int, names: tuple):
        self.group_num = group_num
        self.names = names
        self.students = []
        self.average_grade_dict = {}

    def random_grades_list(self) -> dict:
        """
        Метод для создания случайного словаря успеваемости.
        :return: Словарь успеваемости студента из 5 пар Ключ - Значение.
        """
        temp_dict = dict()
        school_subjects = ('Русский', 'Литература', 'Аглебра', 'Геометрия', 'Английский')

        for i_subject in school_subjects:
            temp_dict[i_subject] = randint(2, 5)

        return temp_dict

    def dict_print(self, dict_for_print: dict, tab_nums = 1) -> None:
        """
        Печатает словарь студентов в формате 'Ключ: Значение'
        :param dict_for_print: словарь успеваемости студентов.
        :param tab_nums: Количество отступов перед выводом, по умолчанию - 1.
        :return:
        """
        tab = '\t' * tab_nums
        max_str_len = max(len(i_str) for i_str in dict_for_print.keys())

        for i_key, i_value in dict_for_print.items():
            needed_len = max_str_len - len(i_key)
            print(f'{tab}{i_key}:{' ' * needed_len}\t{i_value}')

    def create_students_list(self):
        """
        Создаёт список студентов и сохраняет его в self.students
        """
        for i in range(len(self.names)):
            new_student = Student(self.names[i], self.group_num, self.random_grades_list())
            self.students.append(new_student)

    def calculate_averages(self):
        """
        Считает средний балл каждого студента и заполняет словарь self.average_grade_dict
        """
        for i_stud in self.students:
            self.average_grade_dict[i_stud.name] = i_stud.gpa()

    def show_sorted_by_gpa(self):
        """
        Сортирует студентов по среднему баллу и выводит.
        """
        sorted_grades = dict(sorted(self.average_grade_dict.items(), key=lambda item: item[1]))
        print('\nСписок учеников по возрастанию среднего балла:')
        self.dict_print(sorted_grades)

    def run(self):
        """
        Главный метод запуска. Создаёт студентов, считает баллы и выводит отсортированный список.
        """
        self.create_students_list()
        self.calculate_averages()
        self.show_sorted_by_gpa()


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

# Запуск через метод
Group(group_num=1, names=names).run()
