def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3

def test_add_fail():
    # This will fail to demonstrate an error
    assert add(1, 2) == 5
