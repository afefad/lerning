# Lambda-функции
from typing import List, Dict, Union

# users: List[str] = ['user1', 'user2', 'user30', 'user3', 'user22', 'user100']
#
# sorted_users = sorted(users, key=lambda elem: int(elem[4:]))
# print(sorted_users)
#
# x = lambda a: a + 10
#
# print(x(5))


# grades: List[Dict[str, Union[str, int]]] = [
#     {'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41}, {'name': 'Joyce', 'score': 24},
#     {'name': 'Richard', 'score': 37}, {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
#     {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2}, {'name': 'Mary', 'score': 63},
#     {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44}, {'name': 'Richard', 'score': 78},
#     {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13}, {'name': 'Lloyd', 'score': 52},
#     {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40}, {'name': 'James', 'score': 54},
#     {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9}, {'name': 'Bruce', 'score': 68},
#     {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22}, {'name': 'Aaron', 'score': 3},
#     {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94}, {'name': 'Sandra', 'score': 40},
# ]
#
# min_score = min(grades, key=lambda x: x['score'])
# max_score = max(grades, key=lambda x: x['score'])
# print(f"Минимальный результат: {min_score}")
# print(f"Максимальный результат: {max_score}")


class Person:
    """
    Стандартный класс человек.

    :param name: Имя
    :param age: Возраст
    :param height: Рост
    :param weight: Вес
    """
    def __init__(self, name: str, age: int, height: int, weight: int):
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight

    @property
    def name(self) -> str:    #Геттер
        """Геттер для получения имени"""
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception('Имя должно передаваться строкой')

    @property
    def age(self) -> int:    #Геттер
        """Геттер для получения возраста"""
        return self._age

    @age.setter
    def age(self, age: int) -> None: #Сеттер
        if isinstance(age, int):
            self._age = age
        else:
            raise Exception('Возраст должен передаваться числом')

    @property
    def height(self) -> int:    #Геттер
        """Геттер для получения роста"""
        return self._height

    @height.setter
    def height(self, height):
        if isinstance(height, int):
            self._height = height
        else:
            raise Exception('Рост должен передаваться числом')

    @property
    def weight(self) -> int:    #Геттер
        """Геттер для получения веса"""
        return self._weight

    @weight.setter
    def weight(self, weight):
        if isinstance(weight, int):
            self._weight = weight
        else:
            raise Exception('Вес должен передаваться числом')


alfa = Person('Альфа', 24, 172, 80)
kostya = Person('Костя', 28, 153, 50)
igor = Person('Игорь', 32, 184, 79)

persons = [alfa, igor, kostya]

data: List[Dict[str, Union[str, int]]] = [
    {'name': i.name,'age': i.age,'height': i.height,'weight': i.weight} for i in persons
]

persons_sorted = sorted(data, key=lambda x: x['age'])

for i in data:
    print(i)
print()
for i in persons_sorted:
    print(i)

