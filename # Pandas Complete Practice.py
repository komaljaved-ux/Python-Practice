# Pandas Complete Practice
# Pandas is used for handling and analyzing data like Excel in Python

import pandas as pd

# ---- Part 1: Series (Single Column Data) ----
data = [10, 20, 30, 40]
numbers = pd.Series(data)
print("Series:")
print(numbers)

# Custom index
marks = pd.Series([90, 85, 78], index=["Ali", "Komal", "Sara"])
print("\nMarks Series:")
print(marks)

# Accessing data from Series
print("Komal's Marks:", marks["Komal"])

# ---- Part 2: DataFrame (Table Form Data) ----
students = {
    "Name": ["Ali", "Komal", "Sara"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(students)
print("\nStudent DataFrame:")
print(df)

# DataFrame information
print("\nFirst 2 rows:")
print(df.head(2))

print("\nShape (rows, columns):")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

# Accessing a column
print("\nMarks Column:")
print(df["Marks"])

# Adding a new column
df["Grade"] = ["A", "A+", "B"]
print("\nUpdated DataFrame with Grade:")
print(df)

# Accessing a single row
print("\nRow with index 1:")
print(df.loc[1])

# ---- Part 3: Data Analysis ----
data2 = {
    "Name": ["Ali", "Komal", "Sara", "Hassan"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 88],
    "City": ["Lahore", "Multan", "Karachi", "Islamabad"]
}

df2 = pd.DataFrame(data2)
print("\nNew Student Data:")
print(df2)

# Summary statistics
print("\nSummary of numeric data:")
print(df2.describe())

# Selecting specific columns
print("\nOnly Names and Marks:")
print(df2[["Name", "Marks"]])

# Head and Tail
print("\nFirst 2 Rows:")
print(df2.head(2))

print("\nLast 2 Rows:")
print(df2.tail(2))

# Conditional filtering
print("\nStudents with marks > 80:")
print(df2[df2["Marks"] > 80])

# Sorting data
print("\nSorted by Marks (Descending):")
print(df2.sort_values(by="Marks", ascending=False))

# ---- Part 4: File Handling with Pandas ----
# Saving data to a CSV file
df2.to_csv("students.csv", index=False)
print("\nData saved to students.csv")

# Reading the CSV file
new_df = pd.read_csv("students.csv")
print("\nData read from CSV file:")
print(new_df)