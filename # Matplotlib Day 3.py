# Matplotlib Day 3
# Topics: Multiple figures, legends, saving plots, real data plotting, grid, style

import matplotlib.pyplot as plt

# ---- Multiple Figures ----
plt.figure()
plt.plot([1, 2, 3, 4], [5, 10, 6, 8])
plt.title("Figure 1")

plt.figure()
plt.plot([1, 2, 3, 4], [10, 4, 8, 2])
plt.title("Figure 2")

plt.show()


# ---- Adding Legend ----
x = [1, 2, 3, 4, 5]
y1 = [3, 6, 9, 12, 15]
y2 = [2, 4, 6, 8, 10]

plt.plot(x, y1, label="Multiples of 3", linewidth=2)
plt.plot(x, y2, label="Multiples of 2", linewidth=2)
plt.title("Line Graph with Legends")
plt.xlabel("X")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.show()


# ---- Saving a Plot ----
plt.plot([1, 2, 3], [10, 20, 15])
plt.title("Saved Plot Example")
plt.savefig("my_plot.png")   # saves picture in folder
plt.show()


# ---- Real Data Plotting ----
# Example: Temperature of a week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temp = [20, 22, 23, 19, 24, 26, 25]

plt.plot(days, temp, marker='o')
plt.title("Weekly Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()


# ---- Using Styles ----
plt.style.use("ggplot")   # applying a built-in style
plt.plot([1, 2, 3, 4], [10, 20, 15, 25])
plt.title("Graph with ggplot Style")
plt.show()


# ---- Subplots with Real Data ----
fig, axes = plt.subplots(1, 2)

axes[0].plot(days, temp)
axes[0].set_title("Line Plot")

axes[1].bar(days, temp)
axes[1].set_title("Bar Plot")

plt.suptitle("Temperature Comparison")
plt.show()