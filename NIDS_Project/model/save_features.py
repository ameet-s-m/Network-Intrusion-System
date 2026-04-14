import pandas as pd
import joblib

X = pd.read_csv("X_processed.csv")

# Save column names
joblib.dump(X.columns.tolist(), "feature_names.pkl")

print("✅ Feature names saved")