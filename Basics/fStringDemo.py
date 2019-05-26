name = "Asif"
age = 34


def test_01():
    print("Hello, %s..." % name)
    print("Hello, %s. You are %s." % (name, age))


def test_02():
    person = {'name': 'Eric', 'age': 74}
    print("Hello, {name}. You are {age}.".format(**person))


def test_03():
    print(f"Hello, {name}. You are {age}.")
    print(f"{to_lowercase(name)}")


def to_lowercase(input):
    return input.lower()



