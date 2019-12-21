import streamlit as st
from PIL import Image
import io

image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
st.text(f"the image type is {type(image)}")
if image is not None:
    st.image(
        image, caption=f"You amazing image has shape", use_column_width=True,
    )
