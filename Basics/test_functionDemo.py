def printMe(username, password):
    print(username, password)


def test_011():
    printMe("username1", "password1")
    printMe(username="username2", password="password2")
    printMe(password="password3", username="username3")

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print(f"key={key}, value={value}")


kwargs = {"arg3": 3, "arg2": "two", "arg1": 1}


def test_02a():
    greet_me(key1=10, key2=20)


def test_02b():
    greet_me(kwargs.items())

def test_03():
    sum = 0
    list = [1,2,3,4,5]
    for num in list:
        sum = sum + num
    average = sum / len(list)
    print("sum of list element is : ", sum)
    print("Average of list element is ", average)


def getTotal(*args):
    sum = 0
    for x in args:
        sum = sum + x
    print(sum)

def test_01():
    getTotal(1,2,3,4,5)

