class Figure:
    name = "figure"

    def __init__(self, name, i):
        if self.__class__ == Figure:
            raise Exception("abstract method")
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass

    def get_name(self):
        return self.name

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("You can’t create a figure!")
