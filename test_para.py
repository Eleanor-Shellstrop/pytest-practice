import pytest


# Test parametrized

@pytest.mark.parametrize("x, y, z", [(10, 30, 300), (20, 40, 200)])
def test_method(x, y, z):
    """ 10 * 30 will pass, 20 * 40 will not"""
    assert x * y == z