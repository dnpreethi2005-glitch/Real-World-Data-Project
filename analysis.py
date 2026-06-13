import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("retail_sales_dataset.csv")

# First 5 rows
print("First 5 rows:")
print(df.head())

# Information about dataset
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical summary
print("\nStatistics:")
print(df.describe())

# Sales by Product Category
sales = df.groupby("Product Category")["Total Amount"].sum()

plt.figure(figsize=(8,5))
sales.plot(kind="bar")
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Amount")
plt.show()

# Gender Distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Gender")
plt.title("Gender Distribution")
plt.show()