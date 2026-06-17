import pandas as pd

df = pd.read_excel(
    r"data\cleaned_indian_job_market_dataset.xlsx"
)

print("\n===== DASHBOARD SUMMARY =====\n")

# Total jobs
print("Total Jobs:", len(df))

# Total companies
print("Total Companies:", df["companyName"].nunique())

# Top city
print("\nTop Hiring City:")
print(df["location"].value_counts().head(1))

# Top company
print("\nTop Hiring Company:")
print(df["companyName"].value_counts().head(1))

# Average salary
print("\nAverage Maximum Salary:")
print(round(df["maximumSalary"].mean(), 2))

# Average rating
print("\nAverage Company Rating:")
print(round(df["AggregateRating"].mean(), 2))