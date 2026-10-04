import pandas as pd

df = pd.read_csv(
    "data/anomaly_results.csv",
    parse_dates=["datetime"]
)

# Total observations for each day
total_by_day = (
    df["day_of_week"]
    .value_counts()
    .sort_index()
)

# Anomalies for each day
anomalies_by_day = (
    df[df["is_anomaly"]]["day_of_week"]
    .value_counts()
    .sort_index()
)

# Combine the two
results = pd.DataFrame({
    "total_observations": total_by_day,
    "anomalies": anomalies_by_day
})

results["anomaly_rate"] = (
    results["anomalies"] /
    results["total_observations"] *
    100
)

day_names = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

results["day"] = results.index.map(day_names)

results = results[
    [
        "day",
        "total_observations",
        "anomalies",
        "anomaly_rate"
    ]
]

print("Anomaly rate by day:")
print(results.to_string(index=False))

results.to_csv(
    "results/anomaly_rates_by_day.csv",
    index=False
)

print("\nSaved results to results/anomaly_rates_by_day.csv")