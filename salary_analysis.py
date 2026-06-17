import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel(
    r"C:\Users\deept\Downloads\indian-job-market-dataset-2025.xlsx"
)

# Remove rows with missing salary
salary_df = df.dropna(subset=["maximumSalary"])

# Top 10 highest paying cities
top_salary_cities = (
    salary_df.groupby("location")["maximumSalary"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Highest Paying Cities:\n")
print(top_salary_cities)

# Plot
plt.figure(figsize=(12, 6))
top_salary_cities.plot(kind="bar")

plt.title("Top 10 Highest Paying Cities")
plt.xlabel("City")
plt.ylabel("Average Maximum Salary")
plt.xticks(rotation=40)

plt.tight_layout()

# Show graph
plt.show()