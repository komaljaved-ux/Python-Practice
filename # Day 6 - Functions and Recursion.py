# Day 6 - Functions and Recursion 

# --- Functions ---
# Functions are reusable blocks of code.
# simple function (no parameters)
def greet() -> None:
    print("Hello! Welcome to Python.")

# calling the function
greet()

# function with parameters
def add_numbers(a: int, b: int) -> None:
    sum_result: int = a + b
    print("Sum is:", sum_result)

add_numbers(4, 6)

# function with return value
def multiply(a: int, b: int) -> int:
    result: int = a * b
    return result

ans: int = multiply(5, 3)
print("Product is:", ans)

# function to check even or odd
def check_number(num: int) -> None:
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

check_number(10)
check_number(7)

# --- Default parameter ---
def greet_user(name: str = "User") -> None:
    print("Hello,", name)

greet_user("Komal")
greet_user()

# --- Recursion ---
# Recursion means a function that calls itself again and again.

def factorial(n: int) -> int:
    """Find factorial of a number using recursion."""
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("\nFactorial of 5 is:", factorial(5))

# another recursion example (countdown)
def countdown(n: int) -> None:
    """Print countdown numbers using recursion."""
    if n == 0:
        print("Time up!")
    else:
        print(n)
        countdown(n - 1)

print("\nCountdown from 5:")
countdown(5)

