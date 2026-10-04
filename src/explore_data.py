import pandas as pd

# Load the dataset
file_path = "data/household_power_consumption.txt"

df = pd.read_csv(
    file_path,
    sep=";",
    low_memory=False
)

# Basic information
print("Dataset shape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())