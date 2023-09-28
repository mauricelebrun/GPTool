import streamlit as st
import openai
from os import system
from src.gpt import api_gpt
from src.front import space
from src.voice import save_audio
import time

# OpenAI API key
openai.api_key = st.secrets["api_key"]

# Page title
title = "<h1 style='text-align: center; color: #FFFFFF;'>Henri Rousseau</h1>"
st.markdown(title, unsafe_allow_html=True)

space(2)


# Define prompt
prompt = st.chat_input("Prompt")

# Define output
if prompt:
    message = st.chat_message("user")
    message.write(prompt)
    with st.spinner("Loading..."):
        output = api_gpt(prompt)

        # Display output
        message = st.chat_message("assistant", avatar='rousseau.png')
        message.write(output)

    # Save text to audio file and then run it using st.audio()
    #save_audio(output, "output.mp3")
    system(f"say '{output}'")
    #st.audio("output.mp3", format="audio/mp3")



