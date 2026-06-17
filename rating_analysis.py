import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    r"data\indian-job-market-dataset-2025.xlsx"
)

rating_df = df.dropna(subset=["AggregateRating"])

print("\nRating Statistics:\n")
print(rating_df["AggregateRating"].describe())

plt.figure(figsize=(10,6))

plt.hist(
    rating_df["AggregateRating"],
    bins=20
)

plt.title("Company Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Companies")

plt.tight_layout()
plt.show()