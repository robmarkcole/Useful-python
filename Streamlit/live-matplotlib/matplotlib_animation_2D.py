# https://discuss.streamlit.io/t/how-to-animate-a-line-chart/164/6
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

cm_hot = plt.cm.get_cmap('hot')

def get_frame():
    data = np.random.randint(0, 100, size=(80,80))
    im = cm_hot(data)
    im = np.uint8(im * 255)
    return Image.fromarray(im)

my_image = st.image(get_frame(), caption='Random image', width=600)

while True:
    time.sleep(0.1)
    my_image.image(get_frame(), caption='Random image', width=600)