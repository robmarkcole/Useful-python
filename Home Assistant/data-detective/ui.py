import pandas as pd
import streamlit as st

HA_CSV = 'ha.csv'

st.title('Data detective UI')

@st.cache
def get_data():
    df = pd.read_csv(HA_CSV, index_col=0)
    return df

@st.cache
def get_sensors(df):
    return list(df[df['domain']=='sensor']['entity_name'].unique())

def get_binary_sensors(df):
    return list(df[df['domain']=='binary_sensor']['entity_name'].unique())

df = get_data()
sensors = get_sensors(df)
binary_sensors = get_binary_sensors(df)
# st.write(sensors)

st.dataframe(df)