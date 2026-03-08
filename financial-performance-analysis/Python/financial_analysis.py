import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("../data/clean_financial_data.csv")

# Calculate variance
df["variance"] = df["actual"] - df["budget"]

# Variance percentage
df["variance_percent"] = (df["variance"] / df["budget"]) * 100

# Department summary
dept_summary = df.groupby("department")[["budget", "actual", "variance"]].sum()

print("\nDepartment Summary")
print(dept_summary)

# Monthly summary
monthly_summary = df.groupby("month")[["budget", "actual"]].sum()

print("\nMonthly Summary")
print(monthly_summary)

# Plot revenue comparison
monthly_summary.plot(kind="bar")

plt.title("Budget vs Actual by Month")
plt.xlabel("Month")
plt.ylabel("Amount")

plt.tight_layout()
plt.show()

# Save analysis dataset
df.to_csv("../data/financial_analysis_output.csv", index=False)

print("\nAnalysis file created.")