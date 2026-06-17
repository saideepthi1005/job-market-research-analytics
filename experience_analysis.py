import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel(
    r"C:\Users\deept\Downloads\indian-job-market-dataset-2025.xlsx"
)

# Remove missing values
exp_df = df.dropna(subset=["experience"])

# Count experience categories
top_experience = exp_df["experience"].value_counts().head(15)

print("\nMost Requested Experience Levels:\n")
print(top_experience)

# Plot
plt.figure(figsize=(12, 6))
top_experience.plot(kind="bar")

plt.title("Most Requested Experience Levels")
plt.xlabel("Experience")
plt.ylabel("Number of Job Postings")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()