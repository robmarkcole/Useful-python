import pandas as pd
import streamlit as st
import altair as alt
from typing import List

alt.data_transformers.enable("default", max_rows=None)

HA_CSV = "ha.csv"

st.title("Data detective UI")


@st.cache
def get_data():
    df = pd.read_csv(HA_CSV, index_col=0)
    df["last_changed"] = pd.to_datetime(df["last_changed"])
    return df


@st.cache
def get_sensors(df):
    sensors = list(df[df["domain"] == "sensor"]["entity_name"].unique())
    sensors.sort()  # in place sort
    return sensors


def get_sensor_data(df, sensor_names: List[str]):
    data = df[df["entity_name"].isin(sensor_names)]
    return data


def get_sensor_line_chart(data):
    line_chart = (
        alt.Chart(data)
        .mark_line()
        .encode(
            x="last_changed:T",
            y=alt.Y("state"),
            color="entity_name",
            tooltip=["state",],  # 'entity_name','last_changed'
        )
        .interactive()
    )
    return line_chart


def get_sensor_scatter_chart(data):
    """Scatter plot of first 2 columns of time indexed sensor data (wide format)."""
    scatter_chart = (
        alt.Chart(data)
        .mark_circle(size=60)
        .encode(x=data.columns[0], y=data.columns[1],)
        .interactive()
    )
    return scatter_chart


def pivot_dataframe(df, aggfunc="mean"):
    """
    Transform a long df to a wide df, with mean sampling.
    """
    df_pivoted = df.pivot_table(
        index="last_changed", columns="entity_name", values="state", aggfunc=aggfunc
    )
    return df_pivoted


df = get_data()
sensors = get_sensors(df)
st.write(f"There are {len(sensors)} sensors")

sensor_1 = st.selectbox("Select sensor 1 to plot", sensors)
sensor_2 = st.selectbox("Select sensor 2 to plot", sensors, index=1)
data = get_sensor_data(df, [sensor_1, sensor_2])
st.altair_chart(get_sensor_line_chart(data))

st.write(f"Plot of the two factors against each other and their correlation")
pivoted_df = pivot_dataframe(data).resample("1T").mean()

st.altair_chart(get_sensor_scatter_chart(pivoted_df), width=200)
st.dataframe(pivoted_df.corr().iloc[0])
