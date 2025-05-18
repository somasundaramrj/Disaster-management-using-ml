import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
file_path = "Earthquake.csv"  # Ensure the correct path
df = pd.read_csv(file_path)

# Drop unnecessary columns
drop_cols = ["Date", "Time", "ID", "Source", "Location Source", "Magnitude Source", "Status"]
df_cleaned = df.drop(columns=drop_cols, errors="ignore")

# Handle missing values
df_cleaned.fillna(df_cleaned.median(numeric_only=True), inplace=True)

# Define features (X) and target (y)
X = df_cleaned[["Latitude", "Longitude", "Depth"]]
y = df_cleaned["Magnitude"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
rf_model = RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_split=20, min_samples_leaf=15, random_state=42)
rf_model.fit(X_train, y_train)

# Evaluate model
y_pred = rf_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae:.4f}")

# Save model
with open("earthquake_model.pkl", "wb") as file:
    pickle.dump(rf_model, file)

print("Model saved as 'earth.pkl'")
