
import pandas as pd

df = pd.read_csv("datasets/day.csv")

print("DATASET SHAPE:")
print(df.shape)

print("\nFIRST FIVE ROWS:")
print(df.head())

print("\nDATASET INFORMATION:")
df.info()

print("\n--- MISSING VALUES ---")
print(df.isna().sum())

print("\n--- DUPLICATES ---")
print(df.duplicated().sum())

print("\n--- STATISTICS ---")
print(df.describe())

print("\n--- NEGATIVE RENTALS ---")
print((df["cnt"] < 0).sum())

df["dteday"] = pd.to_datetime(df["dteday"])

invalid_totals = (
    df["cnt"] != df["casual"] + df["registered"]
)

print("\n--- INVALID TOTALS ---")
print(invalid_totals.sum())

print("\n--- DUPLICATED DATES ---")
print(df["dteday"].duplicated().sum())

print("\n--- LOWEST RENTAL DAYS ---")
print(
    df.nsmallest(5, "cnt")[
        ["dteday", "cnt", "weathersit", "temp", "hum"]
    ]
)

