import pytest
from src.Figure import Figure
from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle

@pytest.fixture()
def figure():
    return Figure()

@pytest.fixture()
def triangle():
    return Triangle(13, 14, 15)

@pytest.fixture()
def square():
    return Square(10)

@pytest.fixture()
def rectangle():
    return Rectangle(13, 14)

@pytest.fixture()
def circle():
    return Circle(5)
