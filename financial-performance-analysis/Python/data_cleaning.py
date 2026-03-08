import pandas as pd

# Load dataset
df = pd.read_csv("../data/financial_data.csv")

print("Original Dataset")
print(df.head())

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(0)

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Convert numeric columns
df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
df["actual"] = pd.to_numeric(df["actual"], errors="coerce")

# Save cleaned dataset
df.to_csv("../data/clean_financial_data.csv", index=False)

print("\nClean dataset saved as clean_financial_data.csv")