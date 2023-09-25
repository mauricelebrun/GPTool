import streamlit as st
import openai
import time
from src.gpt import api_gpt
from src.front import space
from src.pricing import pricing_input, pricing_output, count_token

# OpenAI API key
openai.api_key = st.secrets["api_key"]

# Page title
title = "<h1 style='text-align: center; color: #23242B;'>Henri Rousseau</h1>"
st.markdown(title, unsafe_allow_html=True)

space(2)


# Define prompt
prompt = st.chat_input("Prompt")

# Define output
if prompt:
    start = time.time()
    message = st.chat_message("user")
    message.write(prompt)
    with st.spinner("Loading..."):
        output = api_gpt(prompt)
        total_tokens = count_token(prompt + output)
        #total_price = pricing_input(model, total_tokens) + pricing_output(model, total_tokens)

        # Display pricing with output
        end = time.time()
        output = output #+ "\n\n" + f"Total tokens: {total_tokens} | Total price: ${total_price:.4f} | Time: {end-start:.2f} seconds"

        # Display output
        message = st.chat_message("assistant")
        message.write(output)


