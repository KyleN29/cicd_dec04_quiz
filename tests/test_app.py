import math
import sys
import pytest
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add, sub, multiply, divide, log, square, sin, cos, square_root, percentage

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_sub():
    assert sub(10, 0) == 10
    assert sub(10, 10) == 0
    assert sub(5, 4) != 2
    assert sub(0, 0) == 0
    assert sub(1, 5) == -4
    assert sub(-5, 3) == -8
    assert sub(-3, -3) == 0

def test_multiply():
    assert multiply(-3, -3) == 9
    assert multiply(100, 0) == 0
    assert multiply(1, 1) != 2
    assert multiply(10, -3) == -30

def test_divide():
    assert divide(5, 3) == 5/3
    assert divide(10, 5) == 2
    assert divide(10, -5) == -2
    assert divide(-10, -5) == 2

    with pytest.raises(ZeroDivisionError):
        divide(0, 0)

    with pytest.raises(ZeroDivisionError):
        divide(100, 0)

def test_log():
    assert log(4, 2) == 2
    assert log(16, 2) == 4
    assert log(16, 4) == 2

    with pytest.raises(ValueError):
        log(-1, 4)
    with pytest.raises(ValueError):
        log(1, 0)
    with pytest.raises(ValueError):
        log(5, -1)
    with pytest.raises(ValueError):
        log(0, 4)
    with pytest.raises(ValueError):
        log(0, 0)

def test_square():
    assert square(2) == 4
    assert square(4) == 16
    assert square(103) == 10609
    assert square(0) == 0
    assert square(-1) == 1
    assert square(-103) == 10609

def test_sin():
    assert sin(math.pi / 2) == pytest.approx(1)
    assert sin(-math.pi / 2) == pytest.approx(-1)
    assert sin(3 * math.pi / 2) == pytest.approx(-1)
    assert sin(0) == pytest.approx(0)

def test_cos():
    assert cos(0) == pytest.approx(1)
    assert cos(math.pi) == pytest.approx(-1)
    assert cos(math.pi / 2) == pytest.approx(0)
    assert cos(2 * math.pi) == pytest.approx(1)

def test_square_root():
    assert square_root(4) == 2
    assert square_root(16) == 4
    assert square_root(0) == 0
    assert square_root(9) == 3
    with pytest.raises(ValueError):
        square_root(-3)

def test_percentage():
    assert percentage(1, 100) == 1
    assert percentage(100, 100) == 100
    assert percentage(.3, 100) == .3
    assert percentage(120, 100) == 120

    with pytest.raises(ValueError):
        percentage(5, 0)
