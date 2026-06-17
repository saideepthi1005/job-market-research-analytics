import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel(
    r"C:\Users\deept\Downloads\indian-job-market-dataset-2025.xlsx"
)

# Top 10 cities with most job postings
top_cities = df["location"].value_counts().head(10)

print("\nTop 10 Hiring Cities:\n")
print(top_cities)

# Plot
plt.figure(figsize=(10, 5))
top_cities.plot(kind="bar")

plt.title("Top 10 Hiring Cities")
plt.xlabel("City")
plt.ylabel("Number of Jobs")

plt.tight_layout()
plt.show()
