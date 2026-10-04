import pandas as pd

# Load anomaly results
df = pd.read_csv(
    "data/anomaly_results.csv",
    parse_dates=["datetime"]
)

# Keep only detected anomalies
anomalies = df[df["is_anomaly"]].copy()

# Sort by electricity usage
highest = anomalies.sort_values(
    "Global_active_power",
    ascending=False
)

print("Highest electricity usage among detected anomalies:")
print(
    highest[
        [
            "datetime",
            "Global_active_power",
            "hour",
            "day_of_week",
            "rolling_mean_24h",
            "rolling_std_24h"
        ]
    ].head(10).to_string(index=False)
)

print("\nLowest electricity usage among detected anomalies:")
lowest = anomalies.sort_values(
    "Global_active_power"
)

print(
    lowest[
        [
            "datetime",
            "Global_active_power",
            "hour",
            "day_of_week",
            "rolling_mean_24h",
            "rolling_std_24h"
        ]
    ].head(10).to_string(index=False)
)