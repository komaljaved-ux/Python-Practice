# Day 4 - Sets and Dictionaries Practice

# --- Sets in Python ---
# A set is an unordered collection of unique elements.

# Creating a set
fruits = {"apple", "banana", "mango", "apple"}  # duplicate 'apple' will be removed
print("Fruits set:", fruits)

# Adding items
fruits.add("orange")
print("After adding orange:", fruits)

# Removing items
fruits.remove("banana")
print("After removing banana:", fruits)

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference (A-B):", A.difference(B))
print("Symmetric Difference:", A.symmetric_difference(B))

# Looping through a set
print("\nLooping through set A:")
for item in A:
    print(item)

# --- Dictionaries in Python ---
# A dictionary stores data in key-value pairs.

student = {
    "name": "Komal",
    "age": 20,
    "course": "Python",
    "marks": 88
}
print("\nStudent Dictionary:", student)

# Accessing values
print("Name:", student["name"])
print("Marks:", student.get("marks"))

# Adding and updating values
student["grade"] = "A"
student["marks"] = 90
print("Updated Student:", student)

# Removing items
student.pop("age")
print("After removing 'age':", student)

# Looping through a dictionary
print("\nKeys:")
for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

print("\n--- End of Day 4 Practice ---")