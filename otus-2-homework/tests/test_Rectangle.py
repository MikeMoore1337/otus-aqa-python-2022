import pytest
from src.Rectangle import Rectangle

name = "Rectangle"


def test_create_class():
    rectangle = Rectangle(name, 4, 6)
    assert isinstance(rectangle, Rectangle)
    assert rectangle.name == name
    assert rectangle.a == 4
    assert rectangle.b == 6


def test_area():
    rectangle = Rectangle(name, 4, 6)
    assert rectangle.area() == 24


def test_perimeter():
    rectangle = Rectangle(name, 4, 6)
    assert rectangle.perimeter() == 20


def test_add_area():
    rectangle1 = Rectangle(name, 4, 6)
    rectangle2 = Rectangle(name, 8, 10)
    assert rectangle1.add_area(rectangle2) == 104

def test_exception_in_method_add_area():
    foo_example = 0
    rectangle = Rectangle(name, 10, 15)
    with pytest.raises(ValueError):
        rectangle.add_area(foo_example)
