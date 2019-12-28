import pandas as pd
import streamlit as st
import altair as alt
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

def get_binary_sensors(df):
    return list(df[df['domain']=='binary_sensor']['entity_name'].unique())

df = get_data()
sensors = get_sensors(df)
binary_sensors = get_binary_sensors(df)

st.write(f"There are {len(sensors)} sensors and {len(binary_sensors)} binary_sensors")

#st.dataframe(df)

def get_sensor_data(sensor_name : str):
    return df[df['entity_name'].isin([sensor_name])]

sensor_to_plot = st.selectbox('Select a sensor to plot', sensors)
data = get_sensor_data(sensor_to_plot)

my_chart = alt.Chart(data).mark_line().encode(
    x='last_changed',
    y=alt.Y('state', title=data.iloc[0]['friendly_name']),
  #  color='entity_name',
    tooltip=['entity_name', 'state', 'last_changed'],
).properties(
    width=600,
    height=300
).interactive()

st.altair_chart(my_chart, width=-1)