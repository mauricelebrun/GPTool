import streamlit as st
import openai
from os import system
from src.gpt import api_gpt
from src.front import space
#from src.voice import save_audio
import time

# OpenAI API key
openai.api_key = st.secrets["api_key"]

# Page title
title = "<h1 style='text-align: center; color: #FFFFFF;'>Henri Rousseau</h1>"
st.markdown(title, unsafe_allow_html=True)
space(2)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] == "assistant":
        with st.chat_message(message["role"], avatar="rousseau.png"):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Add all messages to chat history in the prompt
    prompt = "\n".join([message["content"] for message in st.session_state.messages])

    # Limit prompt length to 2048 tokens
    prompt = prompt[-10000:]

    # Generate assistant response
    response = api_gpt(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})