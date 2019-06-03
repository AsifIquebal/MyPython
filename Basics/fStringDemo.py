import time

name = "Asif"
age = 34


def test_01():
    print("Hello, %s..." % name)
    print("Hello, %s. You are %s." % (name, age))


def test_02():
    person = {'name': 'Eric', 'age': 74}
    print("Hello, {name}. You are {age}.".format(**person))


def test_callFunction():
    time.sleep(4)
    print(f"Hello, {name}. You are {age}.")
    print(f"{to_lowercase(name)}")
    print(f"{name.capitalize()}")
    print(f"{name.upper()}")


def test_compute():
    time.sleep(3)
    print(f"{2*3}")


def to_lowercase(input):
    return input.lower()



class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"


def test_useObjects():
    time.sleep(3)
    comedian = Comedian("Eric", "Idle", "74")
    print(f"{comedian}")
    print(f"{comedian!r}")