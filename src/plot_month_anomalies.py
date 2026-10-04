import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/anomaly_results.csv",
    parse_dates=["datetime"]
)

# Select the first complete month in the dataset
start_date = df["datetime"].min().replace(day=1)

end_date = start_date + pd.DateOffset(months=1)

month = df[
    (df["datetime"] >= start_date) &
    (df["datetime"] < end_date)
]

anomalies = month[month["is_anomaly"]]

plt.figure(figsize=(14, 6))

plt.plot(
    month["datetime"],
    month["Global_active_power"],
    label="Electricity usage"
)

plt.scatter(
    anomalies["datetime"],
    anomalies["Global_active_power"],
    label="Detected anomalies"
)

plt.xlabel("Date")
plt.ylabel("Global Active Power (kW)")
plt.title(
    f"Electricity Usage and Detected Anomalies — "
    f"{start_date.strftime('%B %Y')}"
)

plt.legend()
plt.tight_layout()

plt.savefig(
    "results/month_anomalies.png",
    dpi=300
)

plt.show()