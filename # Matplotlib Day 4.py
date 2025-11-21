# Matplotlib Day 4
# Topics: annotation, dark background, horizontal bar chart,
# area chart, box plot, error bar chart

import matplotlib.pyplot as plt

# ---- Dark Background ----
plt.style.use("dark_background")

x = [1, 2, 3, 4, 5]
y = [10, 8, 15, 12, 20]

plt.plot(x, y, marker='o')
plt.title("Dark Background Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# ---- Annotation (marking a point) ----
plt.plot(x, y, marker='o')
plt.title("Annotation Example")
plt.annotate("Highest Point", xy=(5, 20), xytext=(3, 22),
             arrowprops=dict(facecolor='yellow'))
plt.show()

# ---- Horizontal Bar Chart ----
names = ["Ali", "Komal", "Sara", "Hassan"]
marks = [85, 90, 78, 88]

plt.barh(names, marks)
plt.title("Horizontal Bar Chart")
plt.xlabel("Marks")
plt.ylabel("Names")
plt.show()

# ---- Area Chart ----
x = [1, 2, 3, 4, 5]
sales = [100, 150, 120, 180, 200]

plt.fill_between(x, sales, color='skyblue', alpha=0.5)
plt.title("Area Chart Example")
plt.xlabel("Month No.")
plt.ylabel("Sales")
plt.show()

# ---- Box Plot (to show data spread) ----
data = [12, 15, 14, 20, 22, 30, 25, 18]

plt.boxplot(data)
plt.title("Box Plot Example")
plt.show()

# ---- Error Bar Chart ----
values = [10, 20, 15, 25, 30]
errors = [1, 2, 1, 3, 2]

plt.errorbar(x, values, yerr=errors, fmt='-o')
plt.title("Error Bar Chart")
plt.xlabel("X")
plt.ylabel("Values")
plt.show()