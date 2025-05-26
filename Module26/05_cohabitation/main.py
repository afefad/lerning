from random import randint

class Person:
    """
    Человек может (должны быть такие методы):
    Есть (+ сытость, − еда);
    работать (− сытость, + деньги);
    играть (− сытость);
    ходить в магазин за едой (+ еда, − деньги);
    прожить один день (выбирает одно действие согласно приоритету и выполняет его).
    """
    live = True

    def __init__(self, name, house, hunger=50):
        self.name = name
        self.hunger = hunger
        self.house = house

    def info(self):
        if self.live:
            print(f'Name: {self.name}\n'
                  f'Status: live\n'
                  f'Hunger: {self.hunger}\n'
                  f'House:\n\tCash: {self.house.cash}\n'
                  f'\tSupplies: {self.house.supplies}\n')
        else:
            print(f'Name: {self.name}\n'
                  f'Status: dead\n')

    def go_eat(self):
        if self.live:
            if self.hunger >= 100:
                print(f'{self.name} is already full!\n')
            else:
                if self.house.supplies >= 30:
                    self.house.supplies -= 30
                    self.hunger += 30
                    print(f'{self.name} has eaten and now his satiety is {self.hunger}\n'
                          f'{self.name} hunger: {self.hunger}\n'
                          f'Supplies: {self.house.supplies}\n'
                          f'Cash: {self.house.cash}\n')
                elif self.house.supplies < 30:
                    print(f'There is no food in the fridge, so {self.name} went to the mall.')
                    self.go_to_mall()
        else:
            self.live = False
            print(f'{self.name} is dead!\n')

    def go_to_mall(self):
        if self.hunger <= 0:
            self.live = False
            print(f'{self.name} is dead!\n')
        elif self.hunger == 10:
            self.house.cash += 30
            self.hunger -= 10
            print(f'{self.name} went to the store, '
                  f'but unfortunately did not have time to eat and died of hunger.\n'
                  f'Supplies: {self.house.supplies}\n'
                  f'Cash: {self.house.cash}\n')
        else:
            if self.house.cash >= 30:
                self.hunger -= 10
                self.house.cash -= 30
                self.house.supplies += 60
                print(f'{self.name} bought some supplies.\n'
                      f'{self.name} hunger: {self.hunger}\n'
                      f'Supplies: {self.house.supplies}\n'
                      f'Cash: {self.house.cash}\n')
            else:
                print(f"{self.name} doesn't have enough money for food, so he went to work.")
                self.go_to_work()

    def go_to_work(self):
        if self.hunger <= 0:
            self.live = False
            print(f'{self.name} is dead!\n')
        elif self.hunger == 10:
            self.house.cash += 30
            self.hunger -= 10
            print(f'{self.name} worked all day, earned money and died of hunger.\n'
                  f'Supplies: {self.house.supplies}\n'
                  f'Cash: {self.house.cash}\n')
        else:
            self.house.cash += 30
            self.hunger -= 10
            print(f'{self.name} hunger: {self.hunger}\n'
                  f'Supplies: {self.house.supplies}\n'
                  f'Cash: {self.house.cash}\n')

    def play_a_game(self):
        if self.hunger <= 0:
            self.live = False
            print(f'{self.name} is dead!\n')
        else:
            self.hunger -= 10
            print(f'{self.name} spent the whole day playing video games and now his satiety is {self.hunger}\n'
                  f'{self.name} hunger: {self.hunger}\n'
                  f'Supplies: {self.house.supplies}\n'
                  f'Cash: {self.house.cash}\n')

    def live_through_the_day(self):
        if self.live:
            dice_score = randint(1, 6)
            if self.hunger <= 0:
                self.live = False
                print(f'{self.name} is dead!\n')
            elif self.hunger <= 20:
                print(f'{self.name} is hungry and went to eat.')
                self.go_eat()
            elif dice_score == 1:
                print(f'{self.name} decided to go to work.')
                self.go_to_work()
            elif dice_score == 2:
                print(f'{self.name} decided to go to eat.')
                self.go_eat()
            else:
                print(f'{self.name} decided to play video games.')
                self.play_a_game()
        else:
            return True

class House:
    cash = 0        # Тумбочка с деньгами
    supplies = 50   # Холодильник с едой

    def __init__(self):
        self.cash = 0
        self.supplies = 50
        self.residents = []  # список жильцов

    def add_resident(self, person):
        self.residents.append(person)

    def info(self):
        print(f'Cash: {self.cash}\n'
              f'Supplies: {self.supplies}\n')

    # Метод, который запускает проживание указанного количества дней всеми жильцами
    def live_days(self, days):
        days_counter = 0
        for day in range(days):
            print(f'The {day + 1} day has arrived.')
            print('-' * 20)
            # Проверяем жив ли хоть один жилец
            if any(resident.live for resident in self.residents):
                for resident in self.residents:
                    if resident.live:
                        resident.live_through_the_day()
                days_counter += 1
            else:
                print('All residents have died.\n')
                break
            print()
        print(f'The subjects lived for {days_counter} days.\nSubjects status:')
        for resident in self.residents:
            resident.info()



# Создаём дом и жильцов
house_1 = House()
man_1 = Person('Ivan', house_1)
man_2 = Person('Gena', house_1)

# Добавляем жильцов в дом
house_1.add_resident(man_1)
house_1.add_resident(man_2)

# Запускаем симуляцию
days = int(input('Enter the number of days of stay: '))
house_1.live_days(days)
