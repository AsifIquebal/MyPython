def report():
    print("""This is printed AFTER the test""")


import atexit

atexit.register(report)


def test01():
    assert 10 * 2 == 20
    print("This is a passed test for demonstration purpose")


def test02():
    print("This is a failed test for demonstration purpose")
    assert (20 * 2 == 2)
