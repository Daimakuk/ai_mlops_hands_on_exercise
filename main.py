
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt


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

monthly_rentals = (
    df.groupby("mnth")["cnt"]
    .mean()
    .reset_index()
)

print("\n--- MONTHLY AVERAGE RENTALS ---")
print(monthly_rentals)


monthly_rentals = (
    df.groupby("mnth")["cnt"]
    .mean()
    .reset_index()
)

print("\n--- MONTHLY AVERAGE RENTALS ---")
print(monthly_rentals)

Path("figures").mkdir(exist_ok=True)

sns.lineplot(
    data=monthly_rentals,
    x="mnth",
    y="cnt",
    marker="o"
)

plt.title("Average Daily Bike Rentals by Month")
plt.xlabel("Month")
plt.ylabel("Average Daily Rentals")
plt.xticks(range(1, 13))
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("figures/monthly_rentals.png", dpi=150)
plt.show()



plt.figure(figsize=(9, 5))

sns.scatterplot(
    data=df,
    x="temp",
    y="cnt",
    alpha=0.5
)

plt.title("Temperature vs Daily Bike Rentals")
plt.xlabel("Normalized Temperature")
plt.ylabel("Daily Rentals")
plt.tight_layout()

plt.savefig("figures/temperature_vs_rentals.png", dpi=150)
plt.show()


correlation = df["temp"].corr(df["cnt"])

print("\n--- CORRELATION ---")
print(f"Temperature vs Rentals: {correlation:.3f}")

yearly_rentals = (
    df.groupby("yr")["cnt"]
    .mean()
)

print("\n--- YEARLY AVERAGE RENTALS ---")
print(yearly_rentals)

monthly_by_year = (
    df.groupby(["yr", "mnth"])["cnt"]
    .mean()
    .unstack(level=0)
)

print("\n--- MONTHLY RENTALS BY YEAR ---")
print(monthly_by_year)

monthly_by_year.columns = ["2011", "2012"]

monthly_by_year.plot(
    marker="o",
    figsize=(10, 5)
)

plt.title("Average Daily Rentals by Month and Year")
plt.xlabel("Month")
plt.ylabel("Average Daily Rentals")
plt.xticks(range(1, 13))
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(
    "figures/monthly_by_year.png",
    dpi=150
)

plt.show()


media_2011 = df[df["yr"] == 0]["cnt"].mean()
media_2012 = df[df["yr"] == 1]["cnt"].mean()

aumento_percentuale = (
    (media_2012 - media_2011) / media_2011
) * 100

print(f"Media 2011: {media_2011:.2f}")
print(f"Media 2012: {media_2012:.2f}")
print(f"Aumento: {aumento_percentuale:.2f}%")



