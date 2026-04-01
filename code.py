import pandas as pd

# Load raw file
df = pd.read_csv("processed.cleveland.data", header=None)

# Add column names
df.columns = [
    "age","sex","cp","trestbps","chol","fbs","restecg",
    "thalach","exang","oldpeak","slope","ca","thal","target"
]

# Handle missing values
df = df.replace("?", pd.NA)
df = df.dropna()

# Convert target (0 = no disease, 1 = disease)
df["target"] = df["target"].apply(lambda x: 1 if int(x) > 0 else 0)

# Save clean CSV
df.to_csv("heart_clean.csv", index=False)

print("✅ Done! File created: heart_clean.csv")
print(df.head())