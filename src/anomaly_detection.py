import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Load feature dataset
df = pd.read_csv(
    "data/features.csv",
    parse_dates=["datetime"]
)

# Features used by the model
features = [
    "Global_active_power",
    "hour",
    "day_of_week",
    "rolling_mean_24h",
    "rolling_std_24h"
]

X = df[features]

# Create the Isolation Forest model
model = IsolationForest(
    contamination=0.02,
    random_state=42
)

# Train the model and predict anomalies
df["anomaly"] = model.fit_predict(X)

# Isolation Forest returns:
#  1  = normal
# -1  = anomaly

df["is_anomaly"] = df["anomaly"] == -1

# Count results
print("Total observations:", len(df))
print("Anomalies detected:", df["is_anomaly"].sum())

print(
    "Percentage detected as anomalies:",
    round(df["is_anomaly"].mean() * 100, 2),
    "%"
)

# Save results
df.to_csv("data/anomaly_results.csv", index=False)

# Plot electricity usage and detected anomalies
plt.figure(figsize=(14, 6))

plt.plot(
    df["datetime"],
    df["Global_active_power"],
    label="Electricity usage"
)

anomalies = df[df["is_anomaly"]]

plt.scatter(
    anomalies["datetime"],
    anomalies["Global_active_power"],
    label="Detected anomalies"
)

plt.xlabel("Date")
plt.ylabel("Global Active Power (kW)")
plt.title("Electricity Usage and Detected Anomalies")
plt.legend()

plt.tight_layout()

plt.savefig(
    "results/detected_anomalies.png",
    dpi=300
)

plt.show()