from src.math_operations import add, sub

def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 0) == 0
    assert sub(10, 7) == 3
    assert sub(7, 10) == -3