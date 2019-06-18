import pytest

'''
run this with -s as well as without -s
'''


@pytest.fixture(autouse=True)
def setup_and_teardown():
        print('\nBefore Test')
        yield
        print('\nAfter Test')

def test01():
    assert 10 * 2 == 20
    print("This is a passed test for demonstration purpose")


def test02():
    print("This is a failed test for demonstration purpose")
    assert (20 * 2 == 2)


def test_sum_output_type():
    assert type(sum(1, 2)) is int


def sum(num1, num2):
    """It returns sum of two numbers"""
    return num1 + num2
