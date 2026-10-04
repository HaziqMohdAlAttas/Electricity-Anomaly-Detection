import pandas as pd

# Load the dataset
file_path = "data/household_power_consumption.txt"

df = pd.read_csv(
    file_path,
    sep=";",
    low_memory=False,
    na_values="?"
)

# Combine Date and Time into one datetime column
df["datetime"] = pd.to_datetime(
    df["Date"] + " " + df["Time"],
    dayfirst=True
)

# Convert power consumption to numeric
df["Global_active_power"] = pd.to_numeric(
    df["Global_active_power"],
    errors="coerce"
)

# Keep only the columns we need
df = df[["datetime", "Global_active_power"]]

# Remove rows with missing power readings
df = df.dropna()

# Set datetime as the index
df = df.set_index("datetime")

# Convert minute-by-minute data into hourly averages
hourly = df.resample("h").mean()

# Remove any remaining missing values
hourly = hourly.dropna()

# Show the result
print("Hourly dataset shape:")
print(hourly.shape)

print("\nFirst 10 rows:")
print(hourly.head())

# Save the cleaned data
hourly.to_csv("data/hourly_power.csv")

print("\nSaved cleaned dataset to data/hourly_power.csv")