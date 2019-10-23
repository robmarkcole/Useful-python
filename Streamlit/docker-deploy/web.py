import streamlit as st
import pandas as pd
import numpy as np

st.title('Machine Resources Utilization')
st.sidebar.title('Machine Resources Utilization')
DATE_COLUMN = 'date/time'

@st.cache
def load_data():
    data = pd.read_excel('m_1.xlsx')
    data.drop(['machine_id', 'mem_gps', 'mkpi'], axis=1, inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data['timestamp'])
    return data


data = load_data()
hour_data_group = data.groupby(data[DATE_COLUMN].dt.hour)

st.sidebar.markdown('Interact with the data here')
option = st.sidebar.selectbox(
    'Mean or Mean results to get ',
     ['mean', 'median'])

'You have selected: ', option

# median stats
if option == 'median':
    med_data = pd.DataFrame(data.groupby(data[DATE_COLUMN].dt.hour).median(),
                            columns=['cpu_util_percent', 'mem_util_percent', 'net_in', 'net_out', 'disk_io_percent'])
    med_data.reset_index(inplace=True)
    med_data.drop([DATE_COLUMN], axis=1, inplace=True)
    st.subheader('Median Resources Utilization per hour of the day in the whole week')
    if st.sidebar.checkbox('Show raw data'):
        st.subheader('Raw data')
        med_data
    st.line_chart(med_data)
    st.subheader('Median Resources Utilization per minute for the selected hour of the day in the whole week')
    # Some number in the range 0-23
    hour_to_filter = st.sidebar.slider('hour', 0, 23, 17)
    hour_data = hour_data_group.get_group(hour_to_filter)
    hour_data
    hour_median_data = pd.DataFrame(hour_data.groupby(hour_data[DATE_COLUMN].dt.minute).median(),
                                    columns=['cpu_util_percent', 'mem_util_percent',
                                             'net_in', 'net_out', 'disk_io_percent'])
    hour_median_data.reset_index(inplace=True)
    hour_median_data.drop([DATE_COLUMN], axis=1, inplace=True)
    st.line_chart(hour_median_data)


elif option == 'mean':
    mean_data = pd.DataFrame(data.groupby(data[DATE_COLUMN].dt.hour).mean(),
                             columns=['cpu_util_percent', 'mem_util_percent', 'net_in', 'net_out', 'disk_io_percent'])
    mean_data.reset_index(inplace=True)
    mean_data.drop([DATE_COLUMN], axis=1, inplace=True)
    st.subheader('Mean Resources Utilization per hour of the day in the whole week')
    if st.sidebar.checkbox('Show raw data'):
        st.subheader('Raw data')
        mean_data
    st.line_chart(mean_data)
    st.subheader('Mean Resources Utilization per minute for the selected hour of the day in the whole week')
    # Some number in the range 0-23
    hour_to_filter = st.sidebar.slider('hour', 0, 23, 17)
    hour_data = hour_data_group.get_group(hour_to_filter)
    hour_data
    hour_mean_data = pd.DataFrame(hour_data.groupby(hour_data[DATE_COLUMN].dt.minute).mean(),
                                  columns=['cpu_util_percent', 'mem_util_percent',
                                           'net_in', 'net_out', 'disk_io_percent'])
    hour_mean_data.reset_index(inplace=True)
    hour_mean_data.drop([DATE_COLUMN], axis=1, inplace=True)
    st.line_chart(hour_mean_data)








