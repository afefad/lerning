class Pet:
    TOTAL_SOUNDS = 0

    def __init__(self) -> None:
        self.legs = 4
        self.has_tail = True

    def __str__(self) -> str:
        tail = 'да' if self.has_tail else 'нет'
        return 'Всего ног: {legs}\nХвост присутствует - {has_tail}'.format(
            legs=self.legs,
            has_tail=tail
        )

class Cat(Pet):
    @classmethod
    def sound(cls) -> None:
        cls.TOTAL_SOUNDS += 1
        print(cls.TOTAL_SOUNDS)
        print('Мяу!')


class Dog(Pet):
    @classmethod
    def sound(cls) -> None:
        cls.TOTAL_SOUNDS += 1
        print(cls.TOTAL_SOUNDS)
        print('Гав!')

cat = Cat()
dog = Dog()
print(cat)
print(dog)
cat.sound()
dog.sound()
cat.sound()
cat.sound()
cat.sound()