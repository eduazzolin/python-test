import math


class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radios):
        self.radios = radios

    def area(self):
        return math.pi * self.radios ** 2

    def perimeter(self):
        return 2 * math.pi * self.radios
