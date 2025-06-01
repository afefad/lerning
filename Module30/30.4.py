# Задача 1. Фигуры
#
# При моделировании компьютерных объектов используются два типа фигур: прямоугольники и квадраты. Каждая из них имеет координаты XY,
# длину и ширину. Также каждая фигура может менять координаты (двигаться) и менять размер.
#
# Реализуйте такие классы. Учтите, что с точки зрения интерфейса прямоугольник и квадрат — это разные фигуры и работают они по-разному.
# В частности, по разному работает метод изменения размера фигуры, так как у квадрата все стороны равны.

# Вариант с примесью - когда один метод работает одинаково для двух классов

from abc import ABC, abstractmethod

class Figure(ABC):
    '''
    Абстрактный базовый класс фигура

    :param pos_x: координата X
    :param pos_y: координата Y
    :param length: длина фигуры
    :param width: ширина фигуры
    '''
    def __init__(self, pos_x: int, pos_y: int, length: int, width: int):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    @abstractmethod
    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

class ResizebleMixin:
    def resize(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

class Rectangle(Figure, ResizebleMixin):
    """Прямоугольник. Родительский класс: Figure"""
    pass

class Square(Figure, ResizebleMixin):
    """Квадрат. Родительский класс: Figure"""
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)

rect_1 = Rectangle(pos_x=10, pos_y=20, length=5, width=6)
rect_2 = Rectangle(pos_x=30, pos_y=40, length=10, width=11)
square_1 = Square(pos_x=50, pos_y=70, size=7)

for i_figure in [rect_1, rect_2, square_1]:
    new_x = i_figure.length * 2
    new_y = i_figure.width * 2
    i_figure.resize(new_x, new_y)