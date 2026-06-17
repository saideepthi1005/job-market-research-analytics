import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel(
    r"C:\Users\deept\Downloads\indian-job-market-dataset-2025.xlsx"
)

# Remove missing skill values
skills_df = df.dropna(subset=["tagsAndSkills"])

# Convert all skills into one list
all_skills = []

for skills in skills_df["tagsAndSkills"]:
    skill_list = [skill.strip() for skill in str(skills).split(",")]
    all_skills.extend(skill_list)

# Count skill frequency
skills_series = pd.Series(all_skills)
top_skills = skills_series.value_counts().head(15)

print("\nTop 15 Most Demanded Skills:\n")
print(top_skills)

# Plot
plt.figure(figsize=(12, 6))
top_skills.plot(kind="bar")

plt.title("Top 15 Most Demanded Skills")
plt.xlabel("Skills")
plt.ylabel("Number of Job Postings")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()