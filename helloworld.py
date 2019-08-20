# First exercise
print("My first Python line of code - this time")
print("Print: Check!")
# Second exercise
if 5>2:
    print("Five is greater than 2")
    print("Identation: Check!")

# Third exercise
"""This is a single docstring"""
"""This is a
multiline docstring"""
print("Docstring: Check!")

# Variables
x = 5
y = "André"
print(x)
print(y)

x = "x was 5"
print(x)

print(x + ", now it is a string!")

x = 1
y = 999
print(x+y)

# Numeric Variables
x = 1 # int
y = 2.8 # float
z = 1j # complex

print(type(x))
print(type(y))
print(type(z))

# Casting
x = int(1)
y = int(2.8)
z = int("3")

print(x)
print(y)
print(z)

x = float(1)
y = float(2.8)
z = float("3")

print(x)
print(y)
print(z)

x = str(1)
y = str(2.8)
z = str(3.0)

print(x)
print(y)
print(z)

# String Literals
a = "Yes, I did it!"
print(a[1])
print(a[3:6])
print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("I", "we"))
print(a.split(","))
a = "     Yes, I did it!    ;)"
print(a.strip())

# Command-line String Input
print("Enter your name:")
x = input()
print("Hello, " + x)

# Operators
x = 5
y = 2
z = -2

xy = x // y
xz = x // z

print(xy)
print(xz)

x = "Este é um teste!"
print("teste" in x)

# Lists
x = ["Cristiane", "Laura", "Giulia"]

for i in x:
    print(i)

if "Cristiane" in x:
    print("Cristiane found!")

x.append("André")
x.insert(0, "André")
print(x)

# x.remove("André")
# print(x)
#
# x.remove("André")
# print(x)

while("André" in x):
    x.remove("André")
    print(x)

# Sets
thisset = {"apple", "banana", "pinaple", "kiwi"}
print(thisset)
thisset.add("peach")
print(thisset)
thisset.update(["orange", "guava", "dragon fruit"])
print(thisset)

# Dictionaries
thisdic = {
    "brand":"Tesla",
    "model":"Model 3",
    "year":2020
}
print(thisdic)

print(thisdic["model"])
print(thisdic.get("year"))

print(len(thisdic))
