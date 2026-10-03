import sqlite3

connection = sqlite3.connect("data/liverpool_analytics.db")

query = """
SELECT
    COUNT(*) AS matches,
    SUM(CASE WHEN Result = 'W' THEN 1 ELSE 0 END) AS wins,
    SUM(CASE WHEN Result = 'D' THEN 1 ELSE 0 END) AS draws,
    SUM(CASE WHEN Result = 'L' THEN 1 ELSE 0 END) AS losses,
    SUM(GF) AS goals_scored,
    SUM(GA) AS goals_conceded,
    SUM(GF) - SUM(GA) AS goal_difference,
    ROUND(AVG(Poss), 2) AS average_possession
FROM liverpool_matches
WHERE Result IN ('W', 'D', 'L');
"""

result = connection.execute(query).fetchone()

connection.close()

print("🔴 LIVERPOOL KPI SUMMARY")
print("------------------------")
print("Matches:", result[0])
print("Wins:", result[1])
print("Draws:", result[2])
print("Losses:", result[3])
print("Goals scored:", result[4])
print("Goals conceded:", result[5])
print("Goal difference:", result[6])
print("Average possession:", result[7], "%")