import streamlit as st

video_file_buffer = st.file_uploader("Upload an mp4 video", type=["mp4"])

if video_file_buffer is not None:
    st.video(video_file_buffer)
