import pandas as pd

df = pd.read_csv(
    "data/anomaly_results.csv",
    parse_dates=["datetime"]
)

anomalies = df[df["is_anomaly"]].copy()

# Count anomalies by hour
hour_counts = (
    anomalies["hour"]
    .value_counts()
    .sort_index()
)

print("Anomalies by hour:")
print(hour_counts)

# Count anomalies by day of week
day_counts = (
    anomalies["day_of_week"]
    .value_counts()
    .sort_index()
)

print("\nAnomalies by day of week:")
print(day_counts)

# Compare high and low anomalies
median_usage = df["Global_active_power"].median()

high_anomalies = anomalies[
    anomalies["Global_active_power"] > median_usage
]

low_anomalies = anomalies[
    anomalies["Global_active_power"] <= median_usage
]

print("\nMedian electricity usage:")
print(round(median_usage, 3), "kW")

print("\nHigh-usage anomalies:")
print(len(high_anomalies))

print("\nLow-usage anomalies:")
print(len(low_anomalies))