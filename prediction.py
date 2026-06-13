import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("retail_sales_dataset.csv")

# Convert Gender into numbers
df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})

# Features and target
X = df[["Age", "Quantity", "Price per Unit", "Gender"]]
y = df["Total Amount"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)

print("Model Accuracy:", accuracy)