import pandas as pd

file = input("CSV file: ")
df = pd.read_csv(file)

print("\nFirst rows:")
print(df.head())

numeric = df.select_dtypes("number")
print("\nSummary:")
print(numeric.describe())

if "sales" in df.columns:
    print("\nTotal sales:", df["sales"].sum())
    print("Average sales:", df["sales"].mean())
