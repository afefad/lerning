class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(
            f'Картошка {self.index} сейчас {Potato.states[self.state].lower()}'
        )
class PotatoGarden:

    def __init__(self, count):
        self.potatos = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print(
            'Картошка прорастает!'
        )
        for i_potato in self.potatos:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatos]):
            print('Картошка ещё не созрела!\n')
        else:
            print('Вся картошка созрела! Можно собирать\n')