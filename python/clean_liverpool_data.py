import pandas as pd
from io import StringIO

# Read the raw CSV file
file_path = "data/liverpool_matches.csv"

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Find where the real match table starts
start = None

for i, line in enumerate(lines):
    if line.startswith("Date,Time,Round,Day,Venue,Result"):
        start = i
        break

# Create clean data
match_lines = lines[start:]
data = StringIO("".join(match_lines))

df = pd.read_csv(data, on_bad_lines="skip")

# Keep only rows containing real match dates
df = df[df["Date"].astype(str).str.match(r"^\d{4}-\d{2}-\d{2}$")]

# Convert date to proper date format
df["Date"] = pd.to_datetime(df["Date"])

# Convert numeric columns
df["GF"] = pd.to_numeric(df["GF"], errors="coerce")
df["GA"] = pd.to_numeric(df["GA"], errors="coerce")
df["Poss"] = pd.to_numeric(df["Poss"], errors="coerce")

# Save clean dataset
output_file = "data/liverpool_matches_clean.csv"

df.to_csv(output_file, index=False)

print("🔴 Liverpool data cleaned successfully!")
print("Matches:", len(df))
print("Columns:", len(df.columns))
print("Saved to:", output_file)