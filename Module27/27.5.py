class Person:
    """
    Базовый класс, описывающий человека

    __count: Общее количество человек

    Args:
        name (str): Имя человека
        age (int): Возраст человека
    """
    __count = 0     #Сокрытие данных "__" <- Инкопсуляция

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        Person.__count += 1

    def __str__(self):
        return f"Имя: {self.__name}\tВозраст: {self.__age}"

    def get_count(self):    #Геттер
        """
        Геттер для получения количества инстансов

        :return: __count
        """
        return self.__count

    def set_age(self, age): #Сеттер
        """
        Сеттер для установки возраста.

        :param age: Возраст
        :type age: int
        :raise Exeption: Если возраст не в границах от 1 до 90, то вызывается исключение.
        """
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception("Недопустимый возраст")

    def get_age(self):    #Геттер
        """
        Геттер для получения возраста.

        :return: __age
        :rtype: int
        """
        return self.__age



misha = Person("Misha", 20)
tom = Person("Tom", 25)
print(misha)
print(misha.get_count())
new_age = 80
misha.set_age(new_age)
print(misha.get_age())

print(Person.__doc__)