from agent import agent, clean_text  # your LangChain agent instance
from audio import listen  # your whisper-based voice input
from display import render_display
import streamlit as st

st.set_page_config(page_title="Smart Glasses Display", layout="centered")
st.title("AI Agent with Glasses Display")

if st.button("Speak to Agent"):
    user_input = listen()
    cleaned = clean_text(user_input)

    if not cleaned or cleaned in ["exit", "quit"]:
        st.write("Exiting.")
    else:
        with st.spinner("Thinking..."):
            response = agent.invoke(user_input)
        render_display(response)
