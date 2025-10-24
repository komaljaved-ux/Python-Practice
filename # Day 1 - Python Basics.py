# Day 1 - Python Basics

# Print statement
print("Hello, this is my first Python practice!")

# Variables
name = "Komal"
age = 20
print("My name is", name, "and I am", age, "years old.")

# Data Types
x = 10         # integer
y = 5.5        # float
z = "Python"   # string
print(type(x), type(y), type(z))

# String example
greeting = "Welcome to Python"
print(greeting.lower())
print(greeting.upper())
print(greeting[0:7])

# Conditional statements (if-else)
marks = 85
if marks >= 80:
    print("Excellent! You got an A grade.")
elif marks >= 60:
    print("Good job! You got a B grade.")
else:
    print("Keep trying!")