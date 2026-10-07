# 🔴 Liverpool FC Football Analytics

A football analytics project focused on analyzing Liverpool FC match performance using **Python, SQL, and Power BI**.

## 📌 Project Overview

This project collects, cleans, analyzes, and visualizes Liverpool FC football match data. The goal is to transform raw football match information into meaningful performance insights through data analytics and an interactive Power BI dashboard.

The project demonstrates an end-to-end data analytics workflow, from data collection and cleaning to SQL analysis, Python visualization, and dashboard development.

## 🎯 Objectives

- Analyze Liverpool FC match results and performance.
- Calculate wins, draws, losses, goals scored, and goals conceded.
- Analyze goal difference and average possession.
- Compare home and away performance.
- Clean and prepare football match data for analysis.
- Store and query data using SQLite and SQL.
- Create visualizations using Python.
- Build an interactive Power BI dashboard.
- Present football performance insights in a professional format.

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **SQL**
- **SQLite**
- **Power BI**
- **Git & GitHub**

## 📂 Project Structure

```text
Liverpool_Football_Analytics/
│
├── data/
│   ├── liverpool_matches.csv
│   ├── liverpool_matches_clean.csv
│   ├── liverpool_analytics.db
│   ├── liverpool_results_chart.png
│   └── liverpool_goals_chart.png
│
├── python/
│   ├── get_liverpool_data.py
│   ├── clean_liverpool_data.py
│   ├── liverpool_analysis.py
│   ├── create_database.py
│   ├── sql_test.py
│   └── liverpool_setup.py
│
├── SQL/
│   └── liverpool_queries.sql
│
├── report/
│   ├── Liverpool_Football_Analytics_Report.md
│   └── liverpool_dashboard.png
│
├── Liverpool_Football_Analytics.pbix
├── .gitignore
└── LICENSE🔄 Data Analytics Workflow
1. Data Collection

Football match data was collected and stored in CSV format for analysis.

2. Data Cleaning

Python and Pandas were used to clean the raw dataset, remove unnecessary rows, convert dates and numerical fields, and create a structured dataset.

3. Exploratory Analysis

Python was used to calculate important performance statistics such as:

Total matches
Wins
Draws
Losses
Goals scored
Goals conceded
Goal difference
Average possession
Home and away performance
4. SQL Analysis

The cleaned dataset was stored in a SQLite database. SQL queries were used to retrieve completed matches and calculate key performance indicators.

5. Data Visualization

Python was used with Matplotlib to create charts showing Liverpool's match results and goals scored/conceded.

6. Power BI Dashboard

Power BI was used to create an interactive football analytics dashboard containing KPI cards, charts, match-result analysis, possession analysis, and home-vs-away comparisons.

📊 Dashboard

The Power BI dashboard provides a visual overview of Liverpool FC's performance, including:

Total Matches
Wins
Draws
Losses
Goals Scored
Goals Conceded
Goal Difference
Win Percentage
Average Goals Scored
Average Goals Conceded
Average Possession
Match Results
Home vs Away Matches
Possession by Opponent
📈 Key Results

Based on the completed matches in the current dataset:

Metric	Value
Completed Matches	5
Wins	2
Draws	3
Losses	0
Goals Scored	7
Goals Conceded	4
Goal Difference	+3
Win Percentage	40%
Average Goals Scored	1.40
Average Goals Conceded	0.80
Average Possession	59%
💡 Skills Demonstrated

This project demonstrates practical skills in:

Data collection
Data cleaning
Data analysis
Python programming
Pandas
SQL and SQLite
Data visualization
Power BI
Dashboard development
Git and GitHub
Technical documentation
🚀 Future Improvements

Future versions of this project could include:

Player-level performance analysis
Expected Goals (xG) analysis
Shot maps
Player heatmaps
League table analysis
Advanced team statistics
Automated data collection
Machine learning for match prediction
Live football data integration
👨‍💻 Author

Jouhar

BCA Student | Data Science & Analytics Enthusiast

⭐ If you find this project useful, feel free to explore the repository
