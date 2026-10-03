import pandas as pd
import sqlite3

# Load clean Liverpool data
df = pd.read_csv("data/liverpool_matches_clean.csv")

# Create SQLite database
connection = sqlite3.connect("data/liverpool_analytics.db")

# Save data into database
df.to_sql("liverpool_matches", connection, if_exists="replace", index=False)

connection.close()

print("🔴 Liverpool database created successfully!")
print("Matches added:", len(df))