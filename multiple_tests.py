import pytest


@pytest.mark.one
def test_method1():
    x = 5
    y = 10
    assert x == y


@pytest.mark.two
def test_method2():
    a = 15
    b = 20
    assert a + 5 ==b


# Run one at a time:
# pytest multiple_tests.py -k method1 -v

# Run by marker:
# pytest multiple_tests.py -m one