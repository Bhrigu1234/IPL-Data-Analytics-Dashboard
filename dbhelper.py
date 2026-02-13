import mysql.connector


class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password=""
            )
            self.mycursor = self.conn.cursor()
            print("Connection Established")
        except:
            print("Connection Error")

    def fetch_batter(self):
        batter = []
        self.mycursor.execute("""SELECT DISTINCT(batter) FROM ipl.matches""")
        data = self.mycursor.fetchall()
        for item in data:
            batter.append(item[0])
        return batter

    def fetch_bowler(self):
        bowler = []
        self.mycursor.execute("""SELECT DISTINCT (bowler) FROM ipl.matches""")
        data = self.mycursor.fetchall()
        for item in data:
            bowler.append(item[0])
        return bowler

    def Match_played(self, batter, bowler):
        self.mycursor.execute("""SELECT COUNT(DISTINCT(ID)) FROM ipl.matches
        WHERE batter="{}" AND bowler="{}" """.format(batter, bowler))
        data = self.mycursor.fetchall()
        return data[0][0]

    def Runs_Scored(self, batter, bowler):
        self.mycursor.execute("""
        SELECT SUM(batsman_run)
        FROM ipl.matches
        WHERE batter="{}" and bowler="{}"
        """.format(batter, bowler))
        data = self.mycursor.fetchall()
        return data[0][0]

    def Balls(self, batter, bowler):
        self.mycursor.execute("""
        SELECT COUNT(*)
        FROM ipl.matches
        WHERE batter="{}" and bowler="{}" and (extra_type NOT IN ("wides") OR extra_type IS NULL)
        """.format(batter, bowler))
        data = self.mycursor.fetchall()
        return data[0][0]

    def wicket(self, batter, bowler):
        self.mycursor.execute("""SELECT COUNT(*) FROM ipl.matches
        WHERE kind NOT IN ("run out") and batter="{}" and bowler="{}"
        """.format(batter, bowler))
        data = self.mycursor.fetchall()
        return data[0][0]

    def Top_10_pair(self):
        self.mycursor.execute("""
        SELECT batter, bowler, SUM(batsman_run) AS "Total Runs", COUNT(*) AS "Total_Balls" FROM ipl.matches
        WHERE extra_type NOT IN ("wides") OR extra_type IS NULL
        GROUP BY batter, bowler
        ORDER BY Total_Balls DESC LIMIT 10""")
        data = self.mycursor.fetchall()
        return data

    def Top_10_bowling_pair(self):
        self.mycursor.execute("""
        SELECT bowler, batter, SUM(isWicketDelivery) AS "Total_wicket" FROM ipl.matches
        WHERE kind NOT IN ("run out")
        GROUP BY batter, bowler
        ORDER BY Total_wicket DESC LIMIT 10""")
        data = self.mycursor.fetchall()
        return data

    def Season(self):
        season = []
        self.mycursor.execute("""
        SELECT DISTINCT (Season) FROM ipl.matches_details 
        """)
        data = self.mycursor.fetchall()
        for item in data:
            season.append(item[0])
        return season

    def All_Teams(self, selected_season):
        Teams = []
        self.mycursor.execute("""
        SELECT DISTINCT (Team1) FROM ipl.matches_details
        WHERE Season="{}"
        UNION
        SELECT DISTINCT (Team2) FROM ipl.matches_details
        WHERE Season="{}"
        """.format(selected_season, selected_season))
        data = self.mycursor.fetchall()
        for item in data:
            Teams.append(item[0])
        return Teams

    def Total_Win(self, selected_season, selected_team):
        self.mycursor.execute("""
        SELECT COUNT(*) 
        FROM( SELECT *
        FROM ipl.matches_details
        WHERE Season="{}" AND (Team1="{}" OR Team2="{}"))t
        WHERE t.WinningTeam="{}"
        """.format(selected_season, selected_team, selected_team, selected_team))
        data = self.mycursor.fetchall()
        return data[0][0]

    def Total_Loss(self, selected_season, selected_team):
        self.mycursor.execute("""
        SELECT COUNT(*) 
        FROM( SELECT *
        FROM ipl.matches_details
        WHERE Season="{}" AND (Team1="{}" OR Team2="{}"))t
        WHERE t.WinningTeam!="{}"
        """.format(selected_season, selected_team, selected_team, selected_team))
        data = self.mycursor.fetchall()
        return data[0][0]

    def Average_score_per_over(self, selected_season, selected_team):
        self.mycursor.execute("""
        SELECT SUM(batsman_run) FROM ipl.matches
        WHERE ID IN (SELECT ID
        FROM ipl.matches_details
        WHERE Season="{}" AND (Team1="{}" OR Team2="{}")) AND BattingTeam="{}"
        """.format(selected_season, selected_team, selected_team, selected_team))
        data1 = self.mycursor.fetchall()
        Runs = data1[0][0]
        self.mycursor.execute("""SELECT COUNT(*) FROM ipl.matches
        WHERE ID IN (SELECT ID FROM ipl.matches_details
        WHERE Season="{}" AND (Team1="{}" OR Team2="{}")) AND BattingTeam="{}"
        """.format(selected_season, selected_team, selected_team, selected_team))
        data2 = self.mycursor.fetchall()
        Balls = data2[0][0]
        Average = (Runs / Balls) * 6
        return Average

    def Highest_scorer(self, selected_season, selected_team):
        self.mycursor.execute("""
        SELECT batter, SUM(batsman_run) AS "Total_runs"
        FROM ipl.matches
        WHERE ID IN (SELECT ID
        FROM ipl.matches_details
        WHERE Season="{}" AND (Team1="{}" OR Team2="{}"))        
        GROUP BY batter
        ORDER BY Total_runs DESC
        """.format(selected_season, selected_team, selected_team))
        data = self.mycursor.fetchall()
        return data[0][0], data[0][1]

    def Highest_wickets(self, selected_season, selected_team):
        self.mycursor.execute("""
        SELECT bowler,SUM(isWicketDelivery) AS "Total_wicket"
        FROM ipl.matches
        WHERE ID IN (SELECT ID
        FROM ipl.matches_details
        WHERE Season="{}" AND (Team1 ="{}" OR Team2="{}")) AND (kind IS NULL OR kind IN ("caught", "caught and bowled","bowled","stumped","lbw"))
        GROUP BY bowler
        ORDER BY Total_wicket DESC
        """.format(selected_season, selected_team, selected_team))
        data = self.mycursor.fetchall()
        return data[0][0], data[0][1]

    def ALL_Date(self, selected_season, selected_team):
        date = []
        self.mycursor.execute("""
        SELECT date FROM ipl.matches_details
        WHERE Team1=("{}" OR Team2="{}") AND Season="{}"
        """.format(selected_team, selected_team, selected_season))
        data = self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
        return date

    def Phase_highest_scorer(self, selected_team, selected_season, selected_date):
        self.mycursor.execute("""
        SELECT batter,phase,Total_Runs FROM
        (SELECT batter,SUM(batsman_run) AS "Total_Runs"
        ,COUNT(overs) AS "Balls",
    CASE
        WHEN overs BETWEEN 0 AND 5 THEN "Power_Play"
        WHEN overs BETWEEN 6 AND 14 THEN "Middle_Over"
        WHEN overs BETWEEN 15 and 19 THEN "Dealth_Over"
        END AS phase,
        DENSE_RANK() OVER(PARTITION BY phase ORDER BY Total_runs DESC) AS "Rank"
        FROM ipl.matches
        WHERE ID IN (SELECT ID FROM ipl.matches_details
        WHERE Season="{}" AND (Team1="{}" OR Team2="{}") AND Date="{}")
        GROUP BY batter,phase
        ORDER BY phase DESC, Total_Runs DESC, Balls ASC) t
        WHERE t.Rank=1
        """.format(selected_season, selected_team, selected_team, selected_date))
        data = self.mycursor.fetchall()
        return data

    def All_Batsman(self):
        batsman = []
        self.mycursor.execute("""
        SELECT DISTINCT (batter) FROM ipl.matches""")
        data = self.mycursor.fetchall()
        for item in data:
            batsman.append(item[0])
        return batsman

    def Player_Average(self, batsman_selected):
        self.mycursor.execute("""
        SELECT SUM(Match_Runs) AS "Total_Runs",
        COUNT(*) AS "Total_Batting_Match"
        FROM (SELECT SUM(batsman_run) AS "Match_Runs"
        FROM ipl.matches
        WHERE batter="{}"
        GROUP BY ID
        ORDER BY ID) AS t
        """.format(batsman_selected))
        data = self.mycursor.fetchall()
        return data[0][0], data[0][1]

    def Highest_score(self, batsman_selected):
        self.mycursor.execute("""
        SELECT Max(Match_Runs) AS "Highest Score"
        FROM(SELECT SUM(batsman_run) AS "Match_Runs"
        FROM ipl.matches
        WHERE batter="{}"
        GROUP BY ID
        ORDER BY ID) t"""
                              .format(batsman_selected))
        data = self.mycursor.fetchall()
        return data[0][0]

    def Running_Average(self, batsman_selected):
        self.mycursor.execute("""
        SELECT
        concat("Match-", CAST(ROW_NUMBER() OVER(ORDER BY ID) AS CHAR)) AS "Match Number",
        AVG(SUM(batsman_run)) OVER(ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS "Running Average"
        FROM ipl.matches
        WHERE batter="{}"
        GROUP BY ID
        ORDER BY ID
        """.format(batsman_selected))
        data = self.mycursor.fetchall()
        return data














































































