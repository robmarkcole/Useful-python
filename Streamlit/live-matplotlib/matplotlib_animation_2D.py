# https://discuss.streamlit.io/t/how-to-animate-a-line-chart/164/6
import streamlit as st
import numpy as np
import time

def get_frame():
    return np.random.randint(0, 255, size=(100,100))

my_image = st.image(get_frame(), caption='Random image', width=600)

while True:
    time.sleep(0.1)
    my_image.image(get_frame(), caption='Random image', width=600)