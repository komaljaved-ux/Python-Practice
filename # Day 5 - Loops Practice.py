# Day 5 - Loops Practice

# --- For Loop with range() ---
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")

# --- Nested Loops ---
print("\n\nMultiplication Table (1 to 5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()

# --- While Loop Example ---
print("\nWhile Loop Example:")
x = 1
while x <= 5:
    print("x =", x)
    x += 1

# --- Using continue and break ---
print("\nUsing continue and break:")
for n in range(1, 10):
    if n == 3:
        continue  # skip 3
    if n == 8:
        break     # stop when 8
    print(n)

# --- Looping through a list ---
print("\nLooping through a list of subjects:")
subjects = ["Python", "Math", "AI", "Data Science"]
for s in subjects:
    print("Subject:", s)

# --- Looping through a dictionary ---
print("\nLooping through a dictionary:")
student = {"name": "Komal", "marks": 90, "grade": "A"}
for key, value in student.items():
    print(key, ":", value)

print("\n--- End of Day 5 Practice ---")
