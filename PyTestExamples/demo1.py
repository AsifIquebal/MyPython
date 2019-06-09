import pytest


def test01():
    assert 10 * 2 == 20
    print("Test 1")


def test02():
    assert (20 * 2 == 2)
    print("Test 2")


def test_sum_output_type():
    assert type(sum(1, 2)) is int


def sum(num1, num2):
    """It returns sum of two numbers"""
    return num1 + num2
