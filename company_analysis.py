import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel(
    r"C:\Users\deept\Downloads\indian-job-market-dataset-2025.xlsx"
)

# Remove missing company names
company_df = df.dropna(subset=["companyName"])

# Top companies by job postings
top_companies = company_df["companyName"].value_counts().head(15)

print("\nTop 15 Hiring Companies:\n")
print(top_companies)

# Plot
plt.figure(figsize=(12, 6))
top_companies.plot(kind="bar")

plt.title("Top 15 Hiring Companies")
plt.xlabel("Company")
plt.ylabel("Number of Job Postings")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()