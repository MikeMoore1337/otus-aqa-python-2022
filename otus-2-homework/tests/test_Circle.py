import pytest
import math
from src.Circle import Circle

name = "Circle"


def test_create_class():
    circle = Circle(name, 2)
    assert isinstance(circle, Circle)
    assert circle.radius == 2
    assert circle.name == name


def test_area():
    circle = Circle(name, 2)
    assert circle.area() == math.pi * 2 * 2


def test_perimeter():
    circle = Circle(name, 2)
    assert circle.perimeter() == 2 * math.pi * 2


def test_add_area():
    circle1 = Circle(name, 2)
    circle2 = Circle(name, 4)
    assert circle1.add_area(circle2) == (math.pi * 2 * 2) + (math.pi * 4 * 4)


def test_exception_in_method_add_area():
    foo_example = 0
    circle = Circle(name, 2)
    with pytest.raises(ValueError):
        circle.add_area(foo_example)
