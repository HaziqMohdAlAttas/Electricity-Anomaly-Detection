import pandas as pd

# Load the hourly dataset
df = pd.read_csv(
    "data/hourly_power.csv",
    parse_dates=["datetime"]
)

# Set datetime as the index
df = df.set_index("datetime")

# Create time-based features
df["hour"] = df.index.hour
df["day_of_week"] = df.index.dayofweek

# Create rolling usage features
df["rolling_mean_24h"] = (
    df["Global_active_power"]
    .rolling(window=24)
    .mean()
)

df["rolling_std_24h"] = (
    df["Global_active_power"]
    .rolling(window=24)
    .std()
)

# Remove rows where rolling statistics cannot be calculated
df = df.dropna()

# Save the feature dataset
df.to_csv("data/features.csv")

print("Feature dataset shape:")
print(df.shape)

print("\nFeatures:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nSaved feature dataset to data/features.csv")