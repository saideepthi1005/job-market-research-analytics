import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel(
    r"C:\Users\deept\Downloads\indian-job-market-dataset-2025.xlsx"
)

# Remove missing salary values
salary_df = df.dropna(subset=["maximumSalary"])

print("\nSalary Statistics:\n")
print(salary_df["maximumSalary"].describe())

# Histogram
plt.figure(figsize=(10, 6))

plt.hist(
    salary_df["maximumSalary"],
    bins=30
)

plt.title("Salary Distribution")
plt.xlabel("Maximum Salary")
plt.ylabel("Number of Job Postings")

plt.tight_layout()
plt.show()