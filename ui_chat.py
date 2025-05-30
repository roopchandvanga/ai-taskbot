import streamlit as st
from agent import agent, clean_text
from audio import listen

st.set_page_config(page_title="Assistant", layout="centered")
st.title("Task bot")

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history --
for entry in st.session_state.messages:
    with st.chat_message(entry["role"]):
        st.markdown(entry["content"])

# Trigger on button click 
if st.button("Speak"):
    with st.spinner("Listening..."):
        user_input = listen()

    cleaned = clean_text(user_input)
    if not cleaned:
        st.warning("Didn't catch that.")
    elif cleaned in ["exit", "quit"]:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": "👋 Exiting. See you soon!"})
        st.rerun()

    else:
        # Save user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("Thinking..."):
            response = agent.invoke(user_input)

        # Save assistant message
        st.session_state.messages.append({"role": "assistant", "content": response["output"]})

        # Force rerender with new message
        st.rerun()



