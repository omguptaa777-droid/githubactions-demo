from src.math_operations import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(2,-2) == 0
    assert add(5,1) == 6

def test_sub():
    assert sub(3,2) == 1
    assert sub(-4,2) == -6
    assert sub(2,0) == 2
