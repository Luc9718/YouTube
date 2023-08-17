import streamlit as st
import pandas as pd
import numpy as np

st.title("Web App Football Data")

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League',['England'])

st.sidebar.header("Season")
selected_season = st.sidebar.selectbox('League',['2022/2023'])

# WebScraping Football Data
def load_data(league, season):
  
  if selected_league == 'England':
    league = 'E0'    

if selected_season == '2022/2023':
  season = '2223
  
  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  return data

df = load_data(select_league, select_season)
  
st.subheader("Dataframe: "+selected_league)
st.dataframe(df)


