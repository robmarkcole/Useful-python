import streamlit as st

st.title('My first widget app')

x = st.slider('x')
st.write(x, 'squared is', x * x)