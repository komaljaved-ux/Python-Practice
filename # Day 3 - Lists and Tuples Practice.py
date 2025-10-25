# Day 3 - Lists and Tuples Practice

# --- Lists in Python ---
# A list is a collection that can hold multiple items and can be changed (mutable).

# Creating a list
fruits = ["apple", "banana", "mango", "orange"]
print("Original list:", fruits)

# Accessing items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Changing an item
fruits[1] = "grapes"
print("After changing second item:", fruits)

# Adding items
fruits.append("kiwi")            # add at the end
fruits.insert(2, "cherry")       # insert at index 2
print("After adding new fruits:", fruits)

# Removing items
fruits.remove("apple")           # remove by name
popped_item = fruits.pop()       # remove last item
print("Removed item:", popped_item)
print("After removing:", fruits)

# Slicing a list
print("First three fruits:", fruits[0:3])

# Loop through list
print("\nLooping through fruits:")
for fruit in fruits:
    print(fruit)

# --- Tuples in Python ---
# A tuple is similar to a list but it cannot be changed (immutable).

# Creating a tuple
colors = ("red", "green", "blue", "yellow")
print("\nTuple of colors:", colors)

# Accessing tuple items
print("First color:", colors[0])
print("Last color:", colors[-1])

# Length of tuple
print("Number of colors:", len(colors))

# Tuple cannot be changed — the following line will cause an error if uncommented
# colors[0] = "black"

# Loop through tuple
print("\nLooping through colors:")
for color in colors:
    print(color)

# Tuple methods
numbers = (1, 2, 3, 2, 4, 2)
print("\nCount of 2 in numbers tuple:", numbers.count(2))
print("Index of first 3:", numbers.index(3))

print("\n--- End of Day 3 Practice ---")