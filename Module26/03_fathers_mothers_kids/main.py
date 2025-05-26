from random import randint

class Parent:

    def __init__(self, name: str, age: int, child_list: list):
        self.name = name
        self.age = age
        self.child_list = child_list

    def info(self):
        print(f'Name: {self.name}\n'
              f'Age: {self.age}\n\n'
              f'Children:')
        for i_num, i_child in enumerate(self.child_list):
            print(f'{i_num + 1} ребёнок.')
            i_child.info()

    def feed_the_child(self, child_num):

        if child_num > len(self.child_list):
            raise IndexError(f'Вы пытаетесь накормить {child_num} ребёнка, но у родителя {self.name} всего', f'{len(self.child_list)} детей.' if len(self.child_list) > 1 else '1 ребёнок.')

        child_hunger = self.child_list[child_num - 1].state_of_hunger
        if  child_hunger != 1:
            self.child_list[child_num - 1].state_of_hunger += 1
            print(f'{self.name} накормил {self.child_list[child_num - 1].name}, '
                  f'теперь он {self.child_list[child_num - 1].hunger_status()}')
        else:
            print(f'{self.child_list[child_num - 1].name} уже сыт.')

    def calm_the_child(self, child_num):

        if child_num > len(self.child_list):
            raise IndexError(f'Вы пытаетесь успокоить {child_num} ребёнка, но у родителя {self.name} всего', f'{len(self.child_list)} детей.' if len(self.child_list) > 1 else '1 ребёнок.')

        child_calm = self.child_list[child_num - 1].state_of_calm
        if  child_calm != 1:
            self.child_list[child_num - 1].state_of_calm += 1
            print(f'{self.name} Успокоил {self.child_list[child_num - 1].name}, '
                  f'теперь он {self.child_list[child_num - 1].calm_status()}')
        else:
            print(f'{self.child_list[child_num - 1].name} уже спокоен, его не надо успокаивать.')

class Child:
    calm_states = ['Возбуждён', 'Спокоен']
    hunger_states = ['Голоден', 'Сыт']

    def __init__(self, name: str, age: int, state_of_calm = randint(0, 1), state_of_hunger = randint(0, 1)):
        self.name = name
        self.age = age
        self.state_of_calm = state_of_calm
        self.state_of_hunger = state_of_hunger

    def info(self):
        print(f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'{self.calm_states[self.state_of_calm]}\n'
              f'{self.hunger_states[self.state_of_hunger]}\n')

    def hunger_status(self):
        return self.hunger_states[self.state_of_hunger]

    def calm_status(self):
        return self.calm_states[self.state_of_calm]


child_1 = Child('Ванёк', 18, state_of_calm = 0)
child_2 = Child('Лиза', 6, state_of_hunger = 1)

temp = [child_1, child_2]

parent_1 = Parent('Гена', 44, [child_1, child_2])

parent_1.feed_the_child(1)
parent_1.feed_the_child(2)

parent_1.calm_the_child(1)
parent_1.calm_the_child(2)
