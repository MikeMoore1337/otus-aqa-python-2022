from src.Figure import Figure


class Rectangle(Figure):
    name = "rectangle"

    def __init__(self, name, a, b):
        super().__init__(name, 4)
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2

    def add_area(self, figure):
        super().add_area(figure)
        return figure.area() + self.area()
