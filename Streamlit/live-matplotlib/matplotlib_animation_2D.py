import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time


def get_frame():
    return np.random.randint(0, 100, size=(10,10))


the_plot = st.pyplot(plt.imshow(get_frame()))

def init():
    the_plot.set_data(get_frame())
    return [the_plot]

# animation function.  This is called sequentially
def animate(i):
    the_plot.set_array(get_frame())
    return [the_plot]

for i in range(100):
    animate(i)
    time.sleep(0.1)