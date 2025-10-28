# DAY 5 - LOOPS PRACTICE

# Loops are used to repeat code multiple times.
# There are two main loops in Python:
#   1. for loop
#   2. while loop

#  FOR LOOP with range()
# range(1, 11) gives numbers from 1 to 10 (11 is excluded)
print("Numbers from 1 to 10:")
for i in range(1, 11):   # loop runs from 1 to 10
    print(i, end=" ")    # prints numbers in one line

#  NESTED LOOPS

# A loop inside another loop
# We’ll print a multiplication table from 1 to 5
print("\n\nMultiplication Table (1 to 5):")
for i in range(1, 6):          # Outer loop for rows
    for j in range(1, 6):      # Inner loop for columns
        print(i * j, end="\t") # Print product separated by tab
    print()                    # Move to next line after each row

# WHILE LOOP

# While loop runs until a condition becomes false
print("\nWhile Loop Example:")
x = 1
while x <= 5:           # runs as long as x is less than or equal to 5
    print("x =", x)
    x += 1              # increases x by 1 each time

#  CONTINUE and BREAK

# 'continue' skips one loop cycle
# 'break' stops the loop completely
print("\nUsing continue and break:")
for n in range(1, 10):
    if n == 3:
        continue  # skip number 3
    if n == 8:
        break     # stop the loop when n becomes 8
    print(n)

#  LOOPING THROUGH A LIST

print("\nLooping through a list of subjects:")
subjects = ["Python", "Math", "AI", "Data Science"]
for s in subjects:
    print("Subject:", s)

# LOOPING THROUGH A DICTIONARY

print("\nLooping through a dictionary:")
student = {"name": "Komal", "marks": 90, "grade": "A"}
for key, value in student.items():  # .items() gives both key and value
    print(key, ":", value)

print("\n--- End of Day 5 Practice ---")
