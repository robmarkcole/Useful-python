import pandas as pd
import streamlit as st
import altair as alt
from typing import List
alt.data_transformers.enable('default', max_rows=None)

HA_CSV = 'ha.csv'

st.title('Data detective UI')

@st.cache
def get_data():
    df = pd.read_csv(HA_CSV, index_col=0)
    return df

@st.cache
def get_sensors(df):
    return list(df[df['domain']=='sensor']['entity_name'].unique())

def get_sensor_data(df, sensor_names : List[str]):
    data = df[df['entity_name'].isin(sensor_names)]
    return data

def get_sensor_chart(data):
    my_chart = alt.Chart(data).mark_line().encode(
        x='last_changed:T',
        y=alt.Y('state'),
        color='entity_name',
        tooltip=['entity_name', 'state', 'last_changed'],
    ).interactive()
    return my_chart

df = get_data()
sensors = get_sensors(df)
st.write(f"There are {len(sensors)} sensors")

sensor_1=st.selectbox('Select sensor 1 to plot', sensors)
sensor_2=st.selectbox('Select sensor 2 to plot', sensors)
data = get_sensor_data(df, [sensor_1, sensor_2])
st.altair_chart(get_sensor_chart(data))
st.dataframe(data)
