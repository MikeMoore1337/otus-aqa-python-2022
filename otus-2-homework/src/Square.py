from src.Rectangle import Rectangle


class Square(Rectangle):
    name = "square"

    def __init__(self, name, a):
        super().__init__(name, a, a)

# from src.Rectangle import Rectangle
#
# class Square(Rectangle):
#     name = "square"
#
#     def __init__(self, name, width, height):
#         super().__init__(name, 4)
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.width * self.height
#
#     @property
#     def perimeter(self):
#         return (self.width * self.height) ** 2
#
#     @property
#     def add_area(self, figure):
#         super().add_area(figure)
#         return figure.area() + self.area()
