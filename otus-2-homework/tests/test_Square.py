import pytest
from src.Square import Square

name = "Square"


def test_create_class():
    square = Square(name, 2)
    assert isinstance(square, Square)
    assert square.a == 2
    assert square.b == 2
    assert square.name == name


def test_area():
    square = Square(name, 2)
    assert square.area() == 4


def test_perimeter():
    square = Square(name, 2)
    assert square.perimeter() == 8


def test_add_area():
    square1 = Square(name, 2)
    square2 = Square(name, 3)
    assert square1.add_area(square2) == 13


def test_exception_in_method_add_area():
    foo_example = 0
    square = Square(name, 2)
    with pytest.raises(ValueError):
        square.add_area(foo_example)
