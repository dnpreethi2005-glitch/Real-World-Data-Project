import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("retail_sales_dataset.csv")

# Age Distribution
plt.figure(figsize=(6,4))
sns.histplot(df["Age"], bins=10)
plt.title("Age Distribution")
plt.show()

# Quantity Distribution
plt.figure(figsize=(6,4))
sns.histplot(df["Quantity"], bins=10)
plt.title("Quantity Distribution")
plt.show()

# Gender Distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Gender")
plt.title("Gender Distribution")
plt.show()