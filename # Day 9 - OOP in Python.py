# Day 9 - OOP in Python 
# Topics: Inheritance, Method Overriding & Static Methods
# --- Inheritance Example ---
class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def speak(self) -> None:
        print(f"{self.name} makes a sound.")

# Dog class inherits from Animal class
class Dog(Animal):
    def speak(self) -> None:   # Method Overriding
        print(f"{self.name} says: Woof Woof!")

class Cat(Animal):
    def speak(self) -> None:
        print(f"{self.name} says: Meow Meow!")

dog1: Dog = Dog("Buddy")
cat1: Cat = Cat("Kitty")

dog1.speak()
cat1.speak()

# --- Static Method Example ---
class MathOps:
    @staticmethod
    def add(num1: int, num2: int) -> int:
        return num1 + num2

    @staticmethod
    def multiply(num1: int, num2: int) -> int:
        return num1 * num2

result_add: int = MathOps.add(4, 6)
result_mul: int = MathOps.multiply(3, 7)

print(f"Addition: {result_add}")
print(f"Multiplication: {result_mul}")