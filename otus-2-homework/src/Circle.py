import math
from src.Figure import Figure


class Circle(Figure):
    name = "circle"

    def __init__(self, name, radius):
        super().__init__(name, 0)
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def add_area(self, figure):
        super().add_area(figure)
        return figure.area() + self.area()
