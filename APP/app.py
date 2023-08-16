import streamlit as st
import pandas as pd
import numpy as np

st.title("Web App Football Data")

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League',['Engalnd'])

st.sidebar.header("Season")
selected_season = st.sidebar.selectbox('League',['2022/2023'])

# WebScraping Football Data

https://www.football-data.co.uk/mmz4281/2324/E0.csv

def load_data(league. season):
  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  return data

df = load_data(select_league, select_season)
  



