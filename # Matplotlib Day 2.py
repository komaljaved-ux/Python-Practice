# Matplotlib Day 2
# Topic: Graph Styling, Colors, Multiple Plots, Grid, Line Styles

import matplotlib.pyplot as plt

# ---- Line Style & Color ----
x = [1, 2, 3, 4, 5]
y = [5, 10, 6, 12, 8]

plt.plot(x, y, linestyle='--', linewidth=2)
plt.title("Line Chart with Style")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

# ---- Using Different Colors ----
plt.plot(x, y, color='red')
plt.title("Line Chart in Red Color")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# ---- Multiple Lines in Same Graph ----
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.title("Multiple Lines")
plt.xlabel("X")
plt.ylabel("Values")
plt.legend()  # show labels
plt.grid(True)
plt.show()

# ---- Histogram ----
data = [5, 10, 12, 15, 20, 22, 23, 25, 30, 30, 32, 35]
plt.hist(data, bins=5)
plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# ---- Custom Figure Size ----
plt.figure(figsize=(6,4))
plt.plot([1,2,3], [3,2,1])
plt.title("Custom Size Graph")
plt.show()

# ---- Subplots (Multiple Graphs in one window) ----
plt.subplot(1, 2, 1)   # 1 row, 2 columns, graph 1
plt.plot([1, 2, 3], [3, 6, 9])
plt.title("Plot 1")

plt.subplot(1, 2, 2)   # graph 2
plt.plot([1, 2, 3], [9, 6, 3])
plt.title("Plot 2")

plt.show()# Matplotlib Day 2
# Topic: Graph Styling, Colors, Multiple Plots, Grid, Line Styles

import matplotlib.pyplot as plt

# ---- Line Style & Color ----
x = [1, 2, 3, 4, 5]
y = [5, 10, 6, 12, 8]

plt.plot(x, y, linestyle='--', linewidth=2)
plt.title("Line Chart with Style")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

# ---- Using Different Colors ----
plt.plot(x, y, color='red')
plt.title("Line Chart in Red Color")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# ---- Multiple Lines in Same Graph ----
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.title("Multiple Lines")
plt.xlabel("X")
plt.ylabel("Values")
plt.legend()  # show labels
plt.grid(True)
plt.show()

# ---- Histogram ----
data = [5, 10, 12, 15, 20, 22, 23, 25, 30, 30, 32, 35]
plt.hist(data, bins=5)
plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# ---- Custom Figure Size ----
plt.figure(figsize=(6,4))
plt.plot([1,2,3], [3,2,1])
plt.title("Custom Size Graph")
plt.show()

# ---- Subplots (Multiple Graphs in one window) ----
plt.subplot(1, 2, 1)   # 1 row, 2 columns, graph 1
plt.plot([1, 2, 3], [3, 6, 9])
plt.title("Plot 1")

plt.subplot(1, 2, 2)   # graph 2
plt.plot([1, 2, 3], [9, 6, 3])
plt.title("Plot 2")

plt.show()