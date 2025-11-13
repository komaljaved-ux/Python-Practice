# Pandas Advanced Practice
# Topic: interpolate, merge, concat, join, groupby, append, melt, pivot

import pandas as pd
import numpy as np

# ---- 1. interpolate() ----
data = {"A": [1, 2, np.nan, 4, 5]}
df = pd.DataFrame(data)
print("Before Interpolation:")
print(df)

df["A"] = df["A"].interpolate()
print("\nAfter Interpolation:")
print(df)

# ---- 2. merge() ----
data1 = {"ID": [1, 2, 3], "Name": ["Ali", "Komal", "Sara"]}
data2 = {"ID": [1, 2, 3], "Marks": [85, 90, 78]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merged = pd.merge(df1, df2, on="ID")
print("\nMerged DataFrame:")
print(merged)

# ---- 3. concat() ----
df_a = pd.DataFrame({"Name": ["Ali", "Komal"], "Marks": [85, 90]})
df_b = pd.DataFrame({"Name": ["Sara", "Hassan"], "Marks": [78, 88]})
concat_df = pd.concat([df_a, df_b])
print("\nConcatenated DataFrame:")
print(concat_df)

# ---- 4. join() ----
df_x = pd.DataFrame({"A": [1, 2, 3]}, index=["x", "y", "z"])
df_y = pd.DataFrame({"B": [10, 20, 30]}, index=["x", "y", "z"])
joined = df_x.join(df_y)
print("\nJoined DataFrame:")
print(joined)

# ---- 5. groupby() ----
data3 = {
    "City": ["Lahore", "Multan", "Karachi", "Lahore", "Multan"],
    "Sales": [200, 150, 300, 250, 100]
}
df3 = pd.DataFrame(data3)
print("\nGrouped by City (Total Sales):")
print(df3.groupby("City")["Sales"].sum())

# ---- 6. min(), max(), mean() ----
print("\nMin Sales:", df3["Sales"].min())
print("Max Sales:", df3["Sales"].max())
print("Average Sales:", df3["Sales"].mean())

# ---- 7. append() ----
new_row = pd.DataFrame({"City": ["Islamabad"], "Sales": [180]})
df3 = pd.concat([df3, new_row])
print("\nAfter Append:")
print(df3)

# ---- 8. melt() ----
df4 = pd.DataFrame({
    "Name": ["Ali", "Komal"],
    "Math": [85, 90],
    "English": [80, 88]
})
melted = pd.melt(df4, id_vars=["Name"], var_name="Subject", value_name="Marks")
print("\nMelted DataFrame (Columns → Rows):")
print(melted)

# ---- 9. pivot() ----
pivoted = melted.pivot(index="Name", columns="Subject", values="Marks")
print("\nPivoted DataFrame (Rows → Columns):")
print(pivoted)