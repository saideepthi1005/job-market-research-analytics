import pandas as pd

# Load dataset
df = pd.read_excel(
    r"data\indian-job-market-dataset-2025.xlsx"
)

print("Original Shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

print("After Removing Duplicates:", df.shape)

# Fill missing company ratings with median
df["AggregateRating"] = df["AggregateRating"].fillna(
    df["AggregateRating"].median()
)

# Fill missing review counts with 0
df["ReviewsCount"] = df["ReviewsCount"].fillna(0)

# Fill missing experience values
df["minimumExperience"] = df["minimumExperience"].fillna(
    df["minimumExperience"].median()
)

df["maximumExperience"] = df["maximumExperience"].fillna(
    df["maximumExperience"].median()
)

# Fill missing salary values
df["minimumSalary"] = df["minimumSalary"].fillna(
    df["minimumSalary"].median()
)

df["maximumSalary"] = df["maximumSalary"].fillna(
    df["maximumSalary"].median()
)

print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())

# Save cleaned dataset
df.to_excel(
    "data/cleaned_indian_job_market_dataset.xlsx",
    index=False
)

print("\nCleaned dataset saved successfully.")