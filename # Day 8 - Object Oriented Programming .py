# Day 8 - Object Oriented Programming (OOP) in Python
# Topic: Classes, Objects, and Constructors
# --- Defining a Class ---
# A class is like a blueprint for creating objects.
class Student:
    # constructor to initialize object attributes
    def __init__(self, name: str, age: int, grade: str) -> None:
        self.name: str = name
        self.age: int = age
        self.grade: str = grade

    # method to display student info
    def show_details(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# --- Creating Objects ---
# Each object is an instance of the class
student1: Student = Student("Komal", 20, "A")
student2: Student = Student("Ali", 21, "B")

# Calling methods for each object
student1.show_details()
student2.show_details()

# --- Another Example: Car Class ---
class Car:
    def __init__(self, brand: str, color: str) -> None:
        self.brand: str = brand
        self.color: str = color

    def start(self) -> None:
        print(f"{self.brand} car is starting...")

    def show_color(self) -> None:
        print(f"This car is {self.color} in color.")

# creating objects
car1: Car = Car("Honda", "Red")
car2: Car = Car("Toyota", "Blue")

# calling methods
car1.start()
car1.show_color()

car2.start()
car2.show_color()