class Employee:

    __salary = 800

    grade = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age



    def __repr__(self):
        return f"repr: x={self.name}, y={self.age}"


    def __str__(self):
        return f"str: x={self.name}, y={self.age}"


#e1 = Employee()
#print(e1.__salary)
#print(e1._Employee__salary)

e2 = Employee("abc",123)
print(e2)

print("================================")
print(Employee.grade)
print(e2.grade)
print(f"It has {Employee.grade} grade")
print("================================")
x = Employee("Asif",34)
y = Employee("Sudip",33)
print("Grade in x: ", x.grade)
print("Grade in y: ", y.grade)

Employee.grade = 2
print("Grade in x: ", x.grade)
print("Grade in y: ", y.grade)
