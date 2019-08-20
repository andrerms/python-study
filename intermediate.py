# Functions
def tri_recursion(k):
  if(k>=0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# lambda functions
def my_lambda_func(n):
    return lambda a : a * n

mydoubler = my_lambda_func(2)
mytripler = my_lambda_func(3)

print(mydoubler(10))
print(mytripler(3.33))

# Classes/Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        return "Hello, my name is " + self.name

p1 = Person("André", 38)

print(p1.name)
print(p1.age)

print(p1.myfunc())

p1.age = 32

print("New age is " + str(p1.age))

del p1

# Inheritance
class NewPerson:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

newPerson = NewPerson("John", "Doe")
newPerson.printname()

del newPerson

class Student(NewPerson):
    # pass
    def __init__(self, fname, lname, year):
        # NewPerson.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.graduationyear = year

    def printname(self):
        print("Welcome", self.firstname, self.lastname, "class of", self.graduationyear)

student = Student("André", "Souza", 2005)
student.printname()

del student

# Iterators
