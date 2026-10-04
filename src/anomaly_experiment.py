import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv(
    "data/features.csv",
    parse_dates=["datetime"]
)

features = [
    "Global_active_power",
    "hour",
    "day_of_week",
    "rolling_mean_24h",
    "rolling_std_24h"
]

X = df[features]

contamination_values = [0.01, 0.02, 0.05]

results = []

for contamination in contamination_values:

    model = IsolationForest(
        contamination=contamination,
        random_state=42
    )

    predictions = model.fit_predict(X)

    anomaly_count = (predictions == -1).sum()
    anomaly_percentage = anomaly_count / len(df) * 100

    results.append({
        "contamination": contamination,
        "anomalies_detected": anomaly_count,
        "percentage_detected": anomaly_percentage
    })

results_df = pd.DataFrame(results)

print("Contamination experiment:")
print(results_df)

results_df.to_csv(
    "results/contamination_experiment.csv",
    index=False
)

print("\nSaved results to results/contamination_experiment.csv")