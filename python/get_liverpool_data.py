import pandas as pd
from io import StringIO

file_path = "data/liverpool_matches.csv"

# Read the file
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Find the real match table
start = None

for i, line in enumerate(lines):
    if line.startswith("Date,Time,Round,Day,Venue,Result"):
        start = i
        break

if start is None:
    print("❌ Match table not found!")
else:
    # Keep only the real table
    match_lines = lines[start:]

    data = StringIO("".join(match_lines))

    df = pd.read_csv(data, on_bad_lines="skip")

    # Keep only rows that have a real date
    df = df[df["Date"].astype(str).str.match(r"^\d{4}-\d{2}-\d{2}$")]

    print("🔴 Liverpool Football Analytics")
    print("Number of rows:", len(df))
    print("Number of columns:", len(df.columns))

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 matches:")
    print(df.head())
