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
                  f'{self.name} is dead.\n{attacking_unit} WIN!')
        else:
            print('\nThis warrior is already dead!')

    def status(self):
        if self.health > 0:
            print(f'\nName: {self.name}'
                  f'\nHealth: {self.health}')
        else:
            print(f'\n{self.name} is dead.')

class Battle:

    def __init__(self, unit1: Unit, unit2: Unit, rounds: int = 10):
        self.unit1 = unit1
        self.unit2 = unit2
        self.rounds = rounds
        self.warriors = [unit1, unit2]

    def start(self):
        print('\nFirst warrior:')
        self.unit1.status()
        print('\nSecond warrior:')
        self.unit2.status()

        try:
            for _ in range(self.rounds):
                attacker = random.choice(self.warriors)
                defender = self.unit1 if attacker is self.unit2 else self.unit2

                if defender.health <= 0 or attacker.health <= 0:
                    break

                attacker.attack(defender)
        except Exception as e:
            print(f'Error occurred during the battle: {e}')

if __name__ == "__main__":
    warrior_1 = Unit("Ryu")
    warrior_2 = Unit("Ken")
    battle = Battle(warrior_1, warrior_2)
    battle.start()
