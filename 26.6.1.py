"""
Задача 1. Драка
Что нужно сделать
Вы работаете в команде разработчиков мобильной игры, и вам досталась часть от ТЗ заказчика.

Есть два юнита, каждый называется «Воин». Каждому устанавливается здоровье в 100 очков.
Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет.
У того, кого бьют, оно уменьшается на 20 очков от одного удара. После каждого удара надо выводить сообщение,
какой юнит атаковал и сколько у противника осталось здоровья.
Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том,
кто одержал победу.

Реализуйте такую программу.

Что оценивается
Результат вычислений корректен.
Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
Сообщения о процессе получения результата осмысленны и понятны для пользователя.
Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.
"""
import random

class Unit:

    def __init__(self, name: str, health: int = 100):
        self.health = health
        self.name = name.capitalize()

    def attack(self, target):
        if self.health > 0:
            target.taking_damage(self.name)
        else:
            print("\nYou stupid fool!"
                  "\nThis warrior can't attack since he's dead!")

    def taking_damage(self, attacking_unit: str,  damage: int = 20):
        if self.health > 0:
            self.health -= damage
            print(f'\n{attacking_unit} attacked {self.name} and dealt 20 damage to it.')
            print(f"{self.name}'s health: {self.health}" if self.health > 0 else
                  f'\n{self.name} now is dead.\n{attacking_unit} WIN!')
        else:
            print('\nThis warrior is already dead!')

    def status(self):
        if self.health > 0:
            print(f'\nName: {self.name}'
                  f'\nHealth: {self.health}')
        else:
            print('\nDead!')




warrior_1 = Unit("Ryu")

warrior_2 = Unit("Ken")

print('\nFirst warrior:')
warrior_1.status()
print('\nSecond warrior:')
warrior_2.status()

warriors = [warrior_1, warrior_2]

try:
    for _ in range(10):
        attacking_warrior = random.choice(warriors)
        while True:
            attacked_warrior = random.choice(warriors)
            if attacked_warrior != attacking_warrior:
                break
        if attacked_warrior.health <= 0 or attacking_warrior.health <= 0:
            break
        else:
            attacking_warrior.attack(attacked_warrior)
except:
    print('Ой какая то ошибка!')