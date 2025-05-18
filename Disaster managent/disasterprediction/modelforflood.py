import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("flood.csv")

# Convert FloodProbability to binary classification
df["FloodProbability"] = df["FloodProbability"].apply(lambda x: 1 if x > 0.60 else 0)

# Selecting Features and Target
X = df.drop(columns=['FloodProbability'])
y = df['FloodProbability']

# Feature Importance
model = RandomForestRegressor()
model.fit(X, y)
feature_importance = pd.DataFrame({"features": X.columns, "importance": model.feature_importances_})
top_features = feature_importance.nlargest(5, "importance")["features"]

# Use only important features
X_selected = df[top_features]

# Splitting into Train & Test
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# Train Final Model
final_model = RandomForestRegressor(n_estimators=100, random_state=42)
final_model.fit(X_train, y_train)

# Model Evaluation
y_pred = final_model.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}")
print(f"R² Score: {r2_score(y_test, y_pred)}")

# Save Model
with open("flood_model.pkl", "wb") as f:
    pickle.dump(final_model, f)

print("Model saved as 'flood_model.pkl'")
