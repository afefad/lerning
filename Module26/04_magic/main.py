class Elements:
    elements = []

class Water:
    name = 'Water'

    def __init__(self):
        Elements.elements.append(self)

    def __add__(self, other):
        if other.name == 'Air':
            print(f'{self.name} + {other.name} = Storm')
            return Storm()
        elif other.name == 'Fire':
            print(f'{self.name} + {other.name} = Steam')
            return Steam()
        elif other.name == 'Earth':
            print(f'{self.name} + {other.name} = Mood')
            return Mood()
        else:
            print(f'{self.name} + {other.name} = Something')
            return Something()

class Air:
    name = 'Air'

    def __init__(self):
        Elements.elements.append(self)

    def __add__(self, other):
        if other.name == 'Fire':
            print(f'{self.name} + {other.name} = Thunder')
            return Thunder()
        elif other.name == 'Water':
            print(f'{self.name} + {other.name} = Storm')
            return Storm()
        elif other.name == 'Earth':
            print(f'{self.name} + {other.name} = Dust')
            return Dust()
        elif other.name == 'Lava':
            print(f'{self.name} + {other.name} = Basalt')
            return Basalt()
        else:
            print(f'{self.name} + {other.name} = Something')
            return Something()

class Earth:
    name = 'Earth'

    def __init__(self):
        Elements.elements.append(self)

    def __add__(self, other):
        if other.name == 'Air':
            print(f'{self.name} + {other.name} = Dust')
            return Dust()
        elif other.name == 'Fire':
            print(f'{self.name} + {other.name} = Lava')
            return Lava()
        elif other.name == 'Water':
            print(f'{self.name} + {other.name} = Mood')
            return Mood()
        else:
            print(f'{self.name} + {other.name} = Something')
            return Something()

class Fire:
    name = 'Fire'

    def __init__(self):
        Elements.elements.append(self)

    def __add__(self, other):
        if other.name == 'Water':
            print(f'{self.name} + {other.name} = Steam')
            return Steam()
        elif other.name == 'Earth':
            print(f'{self.name} + {other.name} = Lava')
            return Lava()
        elif other.name == 'Air':
            print(f'{self.name} + {other.name} = Thunder')
            return Thunder()
        else:
            print(f'{self.name} + {other.name} = Something')
            return Something()

class Storm:
    name = 'Storm'

    def __init__(self):
        Elements.elements.append(self)

    def __add__(self, other):
        print(f'{self.name} + {other.name} = Something')
        return Something()

class Steam:
    name = 'Steam'

    def __init__(self):
        Elements.elements.append(self)

    def __add__(self, other):
        print(f'{self.name} + {other.name} = Something')
        return Something()

class Mood:
    name = 'Mood'

    def __init__(self):
        Elements.elements.append(self)

    def __add__(self, other):
        if other.name == 'Air':
            print(f'{self.name} + {other.name} = Earth')
            Elements.elements.remove(self)
            return Earth()
        else:
            print(f'{self.name} + {other.name} = Something')
            return Something()

class Thunder:
    name = 'Thunder'

    def __init__(self):
        Elements.elements.append(self)

    def __add__(self, other):
        print(f'{self.name} + {other.name} = Something')
        return Something()

class Dust:
    name = 'Dust'

    def __init__(self):
        Elements.elements.append(self)

    def __add__(self, other):
        print(f'{self.name} + {other.name} = Something')
        return Something()

class Lava:
    name = 'Lava'

    def __init__(self):
        Elements.elements.append(self)

    def __add__(self, other):
        if other.name == 'Air':
            print(f'{self.name} + {other.name} = Basalt')
            return Basalt()
        else:
            print(f'{self.name} + {other.name} = Something')
            return Something()

class Something:
    name = 'Something'

    def __init__(self):
        Elements.elements.append(self)

    def __add__(self, other):
        print(f"Something can't be combined with anything!")

class Basalt:
    name = 'Basalt'

    def __init__(self):
        Elements.elements.append(self)

    def __add__(self, other):
        print(f'{self.name} + {other.name} = Something')
        return Something()


elements = Elements()

water = Water()
air = Air()
fire = Fire()
earth = Earth()

storm = water + air
steam = water + fire
mood = water + earth
thunder = air + fire
dust = air + earth
lava = earth + fire
basalt = lava + air
something = lava + mood
something_2 = mood + water
earth_2 = mood + air

elements_list = []
for i_element in elements.elements:
    elements_list.append(i_element.name)

print('\n',  elements_list, sep='')
