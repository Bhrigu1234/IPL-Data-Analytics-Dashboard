# 🏏 IPL Data Analytics Dashboard

An interactive IPL analytics dashboard built using **MySQL, Python, and Streamlit** to analyze player performance, team statistics, and match insights using advanced SQL queries.

---

## 🚀 Project Overview

This project demonstrates end-to-end data handling:

- MySQL as backend database
- Python for database connectivity (OOP structure)
- Advanced SQL (Aggregations + Window Functions)
- Streamlit for interactive dashboard
- Real-time filtering & dynamic analytics

The goal was to simulate a real-world data analytics system similar to sports analytics platforms.

---

## 🛠 Tech Stack

- Python
- MySQL
- Streamlit
- Pandas
- SQL (Window Functions, Subqueries, Aggregations)
- Git & GitHub

---

## 📊 Key Features

### 🔹 Player vs Bowler Analysis
- Matches Played
- Runs Scored
- Balls Faced
- Wickets Taken

### 🔹 Top 10 Performance Pairs
- Highest scoring batter-bowler combinations
- Highest wicket-taking bowler-batter combinations

### 🔹 Team-Wise Season Summary
- Total Wins & Losses
- Average Score per Over
- Highest Run Scorer
- Highest Wicket Taker

### 🔹 Phase-Based Analysis
- PowerPlay Performance
- Middle Overs Analysis
- Death Over Impact

### 🔹 Player Career Summary
- Batting Average
- Highest Score
- Running Average (Match-wise progression)

---

## 📌 SQL Concepts Implemented

- GROUP BY & Aggregations (SUM, COUNT)
- Subqueries
- CASE WHEN logic
- Window Functions:
  - DENSE_RANK()
  - ROW_NUMBER()
  - Running Averages using OVER()

---

## 🖥 How to Run the Project

1. Clone the repository:
git clone https://github.com/BHRIGU1234/IPL-Data-Analytics-Dashboard.git

2. Install dependencies:
pip install -r requirements.txt


3. Ensure MySQL is running and database `ipl` exists.

4. Run the application:
streamlit run app.py

---

## 📸 Screenshots

### Player Analysis
![Batsman Bowler Analysis](screenshots/Batsman_Bowler_Analysis.png)
![Most Successful Pairs](screenshots/Most_Successful_Pairs.png)
![PowerPlay vs Middle Overs vs Death Overs](screenshots/Over_Analysis.png)
![Player Analysis](screenshots/player_analysis.png)
![Team Summary](screenshots/Team_wise_summary.png)


## 💡 What This Project Demonstrates

- Backend + Frontend integration
- Writing optimized analytical SQL queries
- Handling relational datasets
- Implementing window functions for advanced analytics
- Modular Python architecture
- Git version control best practices

---

## 🏗 Project Architecture

This project follows a modular 3-layer architecture ensuring separation of concerns and scalable design.

### 1️⃣ Data Layer – MySQL Database
- Stores structured IPL datasets (ball-by-ball & match metadata)
- Tables:
  - `matches`
  - `matches_details`
- Implements relational queries using:
  - Aggregations (SUM, COUNT)
  - Subqueries
  - Window Functions (DENSE_RANK, ROW_NUMBER)

---

### 2️⃣ Backend Layer – Python (dbhelper.py)
- Handles secure database connection
- Encapsulates SQL queries inside class methods
- Follows OOP principles for modular and reusable design
- Acts as middleware between database and frontend

---

### 3️⃣ Frontend Layer – Streamlit (app.py)
- Provides interactive dashboard interface
- Implements dynamic filters (Season, Team, Player)
- Displays computed analytics using metrics & dataframes
- Enables real-time data-driven insights

---

## 🔄 End-to-End Data Flow
```
User Interaction (Streamlit UI)
        ↓
Python Backend (DB Class Methods)
        ↓
SQL Query Execution (MySQL)
        ↓
Aggregated / Processed Results
        ↓
Visualization in Dashboard

```
---

## 📈 Future Improvements

- Deploy dashboard using Streamlit Cloud / Render
- Add caching for query optimization
- Implement player comparison feature
- Add interactive charts (Plotly integration)
- Create automated ETL pipeline for data refresh


## 👨‍💻 Author

Bhrigu Kumar Das
Aspiring Data Engineer | SQL | Python | Data Analytics
🔗 GitHub: https://github.com/BHRIGU1234
🔗 LinkedIn: linkedin.com/in/bhrigu-kumar-das-bb5894276