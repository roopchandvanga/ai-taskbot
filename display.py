import streamlit as st

def render_display(response_text):
    #st.set_page_config(page_title="Smart Glasses Display", layout="centered")
    st.markdown(
        f"<div style='font-size:30px; text-align:center; margin-top:30vh;'>{response_text}</div>",
        unsafe_allow_html=True
    )




