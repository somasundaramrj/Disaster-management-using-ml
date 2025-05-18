import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# Load dataset
df = pd.read_csv("cyclone_dataset.csv")

# Rename columns
df.rename(columns={'Sea_Surface_Temperature':'Sea_temp',
                   'Proximity_to_Coastline':'Proxi_coast',
                   'Pre_existing_Disturbance':'pre_disturb'}, inplace=True)

# Features and Target
X = df[['Sea_temp', 'Humidity', 'Vorticity', 'pre_disturb']]
y = df['Cyclone']

# Handle imbalance
smote = SMOTE()
X_bal, y_bal = smote.fit_resample(X, y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_bal, y_bal, test_size=0.2, random_state=42)

# Apply feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train RandomForest model
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train_scaled, y_train)

# Save model and scaler
joblib.dump(model, "cyclone_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("✅ Model trained & saved correctly!")
