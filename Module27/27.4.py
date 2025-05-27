# class Pet:
#     legs = 4
#     has_tail = True
#
#     def __str__(self):
#         tail = 'да' if self.has_tail else 'нет'
#         return 'Всего ног: {legs}\nХвост присутствует - {has_tail}'.format(
#             legs=self.legs,
#             has_tail=tail
#         )
#
#     def walk(self):
#         print('Гуляет')
#
# class Cat(Pet):
#
#     def sound(self):
#         print('Мяу!')
#
# class Dog(Pet):
#
#     def sound(self):
#         print('Гав!')
#
# class Frog(Pet):
#
#     has_tail = False
#     def sound(self):
#         print('Ква!')
#
#     def walk(self):
#         print('Плавает')
#
# cat = Cat()
# dog = Dog()
# frog = Frog()
# print(cat)
# print(dog)
# print(frog)
# cat.sound()
# dog.sound()
# frog.sound()
# cat.walk()
# dog.walk()
# frog.walk()

class Person:
    __count = 0     #Сокрытие данных "__" <- Инкопсуляция

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        Person.__count += 1

    def __str__(self):
        return f"Имя: {self.__name},\tВозраст: {self.__age}"

    def get_count(self):    #Геттер
        return self.__count

    def set_age(self, age): #Сеттер
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception("Недопустимый возраст")

    def get_age(self):    #Геттер
        return self.__age

    def get_name(self):    #Геттер
        return self.__name

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                'Студент учится в университете {}'.format(self.university)
            )
        )
        return info
        # return 'Студент {} учится в университете {}'.format(self.get_name(), self.university)

class Employee(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)
        self.company = company
        self.salary = salary

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                'Компания: {},\tЗарплата: {}'.format(self.company, self.salary)
            )
        )
        return info


student1 = Student('Tom', 24, 'MTI')
print(student1)

employee1 = Employee(name='Bob', age=41, company='Intel', salary='28.000$')
print(employee1)