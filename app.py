import streamlit as st
from dbhelper import DB
import pandas as pd

db=DB()
st.sidebar.title("IPL Analysis")
btn0=st.sidebar.selectbox("Menu", ["IPL Players", "Top Pairs", "Team Wise Summary", "PowerPlay vs Dealth Overs","Player_wise_Summary"])
if btn0=="IPL Players":
    st.title("Player Analysis")
    col1,col2=st.columns(2)
    with col1:
        batter =db.fetch_batter()
        selected_batter =st.selectbox("Batter", sorted(batter))
    with col2:
        bowler=db.fetch_bowler()
        selected_bowler =st.selectbox("Bowler", sorted(bowler))
    btn1 = st.button("Search")
    if btn1:
        col1, col2, col3,col4 = st.columns(4)
        with col1:
            match = db.Match_played(selected_batter, selected_bowler)
            st.metric(label="Matches", value =match)
        with col2:
            runs_scored = db.Runs_Scored(selected_batter, selected_bowler)
            st.metric(label="Runs", value=runs_scored)
        with col3:
            ball=db.Balls(selected_batter, selected_bowler)
            st.metric(label="Balls", value=ball)
        with col4:
            wicket=db.wicket(selected_batter, selected_bowler)
            st.metric(label="Wicket",value=wicket)
elif btn0=="Top Pairs":
    st.title("Pair Analysis")
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Most Successful Batting vs Bowler")
        result1=db.Top_10_pair()
        df1=pd.DataFrame (result1,columns=["Batter", "Bowler", "Runs", "Balls"])
        st.dataframe (df1)
    with col2:
        st.subheader("Most Successful Bowler vs Batter")
        result2=db.Top_10_bowling_pair()
        df2=pd.DataFrame (result2,columns=["Bowler", "Batter", "Wicket"])
        st.dataframe (df2)

elif btn0=="Team Wise Summary":
    st.title("Team Wise Summary")
    unique_season=db.Season()
    selected_season=st.selectbox("Season", unique_season)
    Teams =db.All_Teams(selected_season)
    selected_team = st.selectbox("Team", sorted(Teams))
    btn1 = st.button("Search")
    if btn1:
        wins =db.Total_Win(selected_season, selected_team)
        loss =db.Total_Loss(selected_season, selected_team)
        Average_score_over = round(db.Average_score_per_over(selected_season, selected_team), 2)
        coll, col2, col3 = st.columns(3)
        with coll:
            st.metric(label="Wins", value=wins)
        with col2:
            st.metric(label="Loss", value=loss)
        with col3:
            st.metric(label="Average Score/Over", value=Average_score_over)
        col1, col2 = st.columns(2)
        with col1:
            batter_name, batter_score = db.Highest_scorer(selected_season, selected_team)
            st.metric(label="Highest Scorer", value=
            batter_name, delta = batter_score)
        with col2:
            bowler_name, bowler_wicket = db.Highest_wickets(selected_season, selected_team)
            st.metric(label="Highest Wicket Taker", value=
            bowler_name, delta=bowler_wicket)
elif btn0=="PowerPlay vs Dealth Overs":
    st.title("PowerPlay Vs Dealth Overs")
    unique_season = db.Season()
    selected_season = st.selectbox("Season", unique_season)
    Teams=db.All_Teams(selected_season)
    selected_team = st.selectbox("Team", sorted(Teams))
    date =db.ALL_Date(selected_season, selected_team)
    selected_date = st.selectbox("Date", date)
    btn1 = st.button("Search")
    if btn1:
        result = db.Phase_highest_scorer(selected_team, selected_season, selected_date)
        df = pd.DataFrame(result, columns=["Batter", "Phase", "Total_runs"])
        st.dataframe(df)
elif btn0=="Player_wise_Summary":
    st.title("Player_Summary")
    unique_batsman=db.All_Batsman()
    batsman_selected=st.selectbox("Batting Carrer", sorted (unique_batsman))
    btn1=st.button("Find Details")
    if btn1:
        col1,col2=st.columns(2)
        with col1:
            Total_Runs,Total_Batting_Match=db.Player_Average(batsman_selected)
            Average=round(Total_Runs/Total_Batting_Match, 2)
            st.metric(label="Average", value =Average)
        with col2:
            Highest_Score=db.Highest_score(batsman_selected)
            st.metric(label="Highest Score",value=Highest_Score)


























