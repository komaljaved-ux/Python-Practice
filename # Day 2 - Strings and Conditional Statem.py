# Day 2 - Strings and Conditional Statements Practice

# --- Strings in Python ---

# 1. Creating a string
message = "Hello Python Learner!"
print(message)

# 2. String Concatenation (joining)
first_name = "Komal"
last_name = "Javed"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# 3. String Indexing and Slicing
text = "Python Programming"
print(text[0])        # first letter
print(text[-1])       # last letter
print(text[0:6])      # substring (0 to 5)

# 4. String Methods
print(text.upper())   # all capital letters
print(text.lower())   # all small letters
print(text.replace("Python", "Java"))  # replace word

# --- Conditional Statements (if, elif, else) ---

# Example 1: Checking even or odd number
num = 10
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# Example 2: Grade checking
marks = 72
if marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")

# Example 3: Checking password strength
password = "Komal123"
if len(password) >= 8:
    print("Password is strong ")
else:
    print("Password is weak ")

print("\n--- End of Day 2 Practice ---")
