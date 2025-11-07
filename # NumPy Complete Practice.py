# NumPy Complete Practice
# NumPy is a python library used for working with arrays and fast calculations

import numpy as np

# ---- Part 1: Creating Arrays ----
arr = np.array([1, 2, 3, 4])
print("Array:", arr)

# Type of array
print("Type:", type(arr))

# 2D Array (matrix form)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:")
print(arr2)

# Shape of array (rows, columns)
print("Shape:", arr2.shape)


# ---- Part 2: Special Arrays ----
# Zeros array
zeros_arr = np.zeros((2, 3))
print("Zeros Array:")
print(zeros_arr)

# Ones array
ones_arr = np.ones((3, 3))
print("Ones Array:")
print(ones_arr)

# Range array
range_arr = np.arange(1, 11)
print("Range Array:", range_arr)


# ---- Part 3: Math Operations ----
arr_math = np.array([10, 20, 30, 40])
print(arr_math + 2)
print(arr_math - 5)
print(arr_math * 3)
print(arr_math / 2)


# ---- Part 4: Statistics ----
print("Max:", arr_math.max())
print("Min:", arr_math.min())
print("Sum:", arr_math.sum())
print("Mean:", arr_math.mean())


# ---- Part 5: Sorting and Joining ----
unsorted = np.array([5, 2, 9, 1])
print("Sorted:", np.sort(unsorted))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Joined:", np.concatenate([a, b]))


# ---- Part 6: Reshape ----
arr3 = np.arange(1, 13)
print("Reshape to 3x4:")
print(arr3.reshape(3, 4))


# ---- Part 7: Random Values ----
rand_arr = np.random.rand(2, 3)
print("Random Array:")
print(rand_arr)
