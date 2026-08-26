from app import add, subtract


def test_add_typical():
    assert add(2, 3) == 5


def test_subtract_typical():
    assert subtract(5, 3) == 2


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2


def test_subtract_with_zero():
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5
