import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "data/household_power_consumption.txt"

df = pd.read_csv(
    file_path,
    sep=";",
    low_memory=False,
    na_values="?"
)

# Combine Date and Time into a single datetime column
df["datetime"] = pd.to_datetime(
    df["Date"] + " " + df["Time"],
    dayfirst=True
)

# Convert power consumption to numeric
df["Global_active_power"] = pd.to_numeric(
    df["Global_active_power"],
    errors="coerce"
)

# Remove rows where power consumption is missing
df = df.dropna(subset=["Global_active_power"])

# Sort by time
df = df.sort_values("datetime")

# Plot the first 7 days
start_date = df["datetime"].min()
end_date = start_date + pd.Timedelta(days=7)

week = df[
    (df["datetime"] >= start_date) &
    (df["datetime"] < end_date)
]

plt.figure(figsize=(12, 5))

plt.plot(
    week["datetime"],
    week["Global_active_power"]
)

plt.xlabel("Date and Time")
plt.ylabel("Global Active Power (kW)")
plt.title("Household Electricity Usage Over One Week")

plt.tight_layout()
plt.show()