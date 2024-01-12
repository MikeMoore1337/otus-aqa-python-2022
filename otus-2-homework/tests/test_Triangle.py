import pytest
from src.Triangle import Triangle

name = "Triangle"


def test_create_class():
    triangle = Triangle(name, 12, 13, 14)
    assert isinstance(triangle, Triangle)
    assert triangle.a == 12
    assert triangle.b == 13
    assert triangle.c == 14
    assert triangle.name == name


def test_area():
    triangle = Triangle(name, 13, 14, 15)
    assert triangle.area == 84


def test_perimeter():
    triangle = Triangle(name, 1, 1, 1)
    assert triangle.perimeter == 3


def test_add_area():
    triangle1 = Triangle(name, 3, 3, 3)
    triangle2 = Triangle(name, 7, 7, 7)
    assert round(int(triangle1.add_area(triangle2))) == 25

def test_exception_in_method_add_area():
    foo_example = 0
    triangle = Triangle(name, 8, 8, 8)
    with pytest.raises(ValueError):
        triangle.add_area(foo_example)
