class Person:

    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def __str__(self) -> str:
        return f"Имя: {self._name},\tВозраст: {self.age}"

    @property
    def age(self) -> int:    #Геттер
        return self._age

    @age.setter
    def age(self, age) -> None: #Сеттер
        if age in range(1, 90):
            self._age = age
        else:
            raise Exception("Недопустимый возраст")

    @property
    def name(self) -> str:    #Геттер
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception('Имя должно передаваться строкой')


tom = Person('Tom', 25)
print(tom)
print(tom.age)
tom.age = 36
print(tom.age)
print(tom.name)

class Vehicle:

    def __init__(self, name: str):
        '''
        Транспортное средство

        :param name: Название транспортного средства
        '''
        self._name = name
        self._type = 'Не задано'

    def __str__(self) -> str:
        return (f'Название транспортного средства: {self._name}\n'
                f'Тип транспортного средства: {self._type}\n')

    def get_ride(self) -> None:
        '''Метод, что бы совершить поездку.'''
        if self._type == 'Не задано':
            print('тип транспортного средства не известен.\n'
                  'Мы не знаем где на нём ездить.')
        else:
            print('Вы куда то отправились.')

    @property
    def name(self) -> str:    #Геттер
        """Геттер для получения названия транспортного средства"""
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception('Название должно передаваться строкой')

    @property
    def type(self) -> str:    #Геттер
        """Геттер для получения типа транспортного средства"""
        return self._type

    @type.setter
    def type(self, type: str) -> None: #Сеттер
        if isinstance(type, str):
            self._type = type
        else:
            raise Exception('Тип транспорта должен передаваться строкой')

class Car(Vehicle):

    def __init__(self, name: str):
        super().__init__(name)
        self._type = 'Дорожный автомобиль'