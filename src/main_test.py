from q2 import fib

def test_fib():
    assert fib(0) == []
    assert fib(1) == [0]
    assert fib(2) == [0,1]
    assert fib(19) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]