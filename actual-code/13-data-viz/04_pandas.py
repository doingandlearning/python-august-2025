import pandas as pd
import matplotlib.pyplot as plt
# DataFrame
df = pd.read_csv("users.csv")

# print(df.head())  # first 5 rows
# print(df.tail())  # last 5 rows
# print(df.describe())  # summary stats of numerical columns
# print(df.sample(5))  # returns 5 random rows

df["Age"] = df["Age"] + 1  # Vectorized broadcasting

print(df.head())

grouped_data = df.groupby("Department")["Salary"].mean()
print(grouped_data)

grouped_data.plot(kind="bar")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()