# Matplotlib Basics
# Matplotlib is used to make charts and graphs in Python

import matplotlib.pyplot as plt

# ---- Line Chart ----
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.title("Simple Line Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# ---- Bar Chart ----
names = ["Ali", "Komal", "Sara", "Hassan"]
marks = [85, 90, 78, 88]

plt.bar(names, marks)
plt.title("Students Marks")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.show()

# ---- Scatter Plot ----
a = [1, 2, 3, 4, 5]
b = [5, 7, 4, 9, 12]

plt.scatter(a, b)
plt.title("Scatter Plot Example")
plt.xlabel("A values")
plt.ylabel("B values")
plt.show()

# ---- Pie Chart ----
sizes = [30, 25, 20, 25]
labels = ["Math", "English", "Science", "Urdu"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Subject Distribution")
plt.show()