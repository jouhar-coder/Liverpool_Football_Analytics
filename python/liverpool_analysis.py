import pandas as pd

# Load clean Liverpool data
file_path = "data/liverpool_matches_clean.csv"
df = pd.read_csv(file_path)
# Keep only completed matches
df = df[df["Result"].isin(["W", "D", "L"])]
# Basic results
wins = (df["Result"] == "W").sum()
draws = (df["Result"] == "D").sum()
losses = (df["Result"] == "L").sum()

# Goals
goals_scored = df["GF"].sum()
goals_conceded = df["GA"].sum()

# Win percentage
win_percentage = (wins / len(df)) * 100

# Average possession
average_possession = df["Poss"].mean()

print("🔴 LIVERPOOL FOOTBALL ANALYTICS")
print("--------------------------------")
print("Matches:", len(df))
print("Wins:", wins)
print("Draws:", draws)
print("Losses:", losses)
print("Goals scored:", goals_scored)
print("Goals conceded:", goals_conceded)
print("Win percentage:", round(win_percentage, 2), "%")
print("Average possession:", round(average_possession, 2), "%")

# Home vs Away analysis

home_matches = df[df["Venue"] == "Home"]
away_matches = df[df["Venue"] == "Away"]

print("\n🏠 HOME PERFORMANCE")
print("-------------------")
print("Matches:", len(home_matches))
print("Wins:", (home_matches["Result"] == "W").sum())
print("Draws:", (home_matches["Result"] == "D").sum())
print("Losses:", (home_matches["Result"] == "L").sum())

print("\n✈️ AWAY PERFORMANCE")
print("-------------------")
print("Matches:", len(away_matches))
print("Wins:", (away_matches["Result"] == "W").sum())
print("Draws:", (away_matches["Result"] == "D").sum())
print("Losses:", (away_matches["Result"] == "L").sum())
# Points and goal averages

points = (wins * 3) + (draws * 1)

goals_per_match = goals_scored / len(df)
goals_conceded_per_match = goals_conceded / len(df)

print("\n🏆 POINTS & GOAL AVERAGES")
print("--------------------------")
print("Points earned:", points)
print("Goals per match:", round(goals_per_match, 2))
print("Goals conceded per match:", round(goals_conceded_per_match, 2))


import matplotlib.pyplot as plt

results = ["Wins", "Draws", "Losses"]
values = [wins, draws, losses]

plt.bar(results, values)

plt.title("Liverpool Match Results")
plt.xlabel("Result")
plt.ylabel("Number of Matches")

plt.savefig("data/liverpool_results_chart.png")
plt.close()

# Goals comparison

goals = ["Goals Scored", "Goals Conceded"]
goal_values = [goals_scored, goals_conceded]

plt.bar(goals, goal_values)

plt.title("Liverpool Goals Comparison")
plt.xlabel("Type")
plt.ylabel("Goals")

plt.savefig("data/liverpool_goals_chart.png")
plt.close()