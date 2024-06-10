# Python Basics Explanation Script

# 1. Variables
# Variables are used to store data values. In Python, you do not need to declare the variable type.
x = 5           # x is of type int
y = "Hello"     # y is of type str
z = 3.14        # z is of type float

# 2. Data Types
# Python has several built-in data types including integers, floats, strings, lists, tuples, and dictionaries.

# Integers
a = 10
b = -5

# Floats
c = 10.5
d = -3.14

# Strings
e = "Python is fun"
f = 'This is also a string'

# Lists (ordered, mutable collection)
g = [1, 2, 3, 4, 5]

# Tuples (ordered, immutable collection)
h = (1, 2, 3, 4, 5)

# Dictionaries (unordered, mutable collection of key-value pairs)
i = {"name": "John", "age": 30}

# 3. Functions
# Functions are defined using the 'def' keyword. They can accept parameters and return values.

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# 4. Conditionals
# Conditional statements are used to perform different actions based on different conditions.

j = 20

if j > 15:
    print("j is greater than 15")
elif j == 15:
    print("j is 15")
else:
    print("j is less than 15")

# 5. Loops
# Loops are used to execute a block of code repeatedly.

# For loop
for num in g:
    print(num)

# While loop
k = 0
while k < 5:
    print(k)
    k += 1

# 6. List Comprehensions
# List comprehensions provide a concise way to create lists.

squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 7. Exception Handling
# Exception handling is used to handle errors gracefully using try and except blocks.

try:
    l = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# 8. Classes and Objects
# Python supports object-oriented programming (OOP) with classes and objects.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person1 = Person("Bob", 25)
print(person1.introduce())  # Output: My name is Bob and I am 25 years old.

# 9. Modules
# Modules are Python files containing Python code. They can define functions, classes, and variables.

import math

print(math.sqrt(16))  # Output: 4.0

# 10. File I/O
# Python can handle file operations, such as reading and writing files.

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, file!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, file!

# This script provides a brief overview of some fundamental concepts in Python.
# Each topic includes comments explaining the concept and code examples demonstrating its use.
