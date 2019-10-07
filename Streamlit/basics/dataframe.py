import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy
import pandas

st.title('My first dataframe app')
st.write("Here's our first attempt at using data to create a table:")

df = pandas.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write(df)

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df.columns)

st.write('You selected:', option)

## Use checkbox

if st.checkbox('Show dataframe'):
    chart_data = pandas.DataFrame(
       numpy.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)