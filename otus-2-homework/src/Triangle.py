from src.Figure import Figure


class Triangle(Figure):
    name = "triangle"

    def __init__(self, name, a, b, c):
        super().__init__(name, 3)
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        p = (self.a + self.b + self.c) / 2
        area = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return area

    @property
    def perimeter(self):
        return self.a + self.b + self.c


    def add_area(self, figure):
        super().add_area(figure)
        return figure.area + self.area
