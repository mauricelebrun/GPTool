import streamlit as st
import openai
import time
from src.gpt import api_gpt
from src.front import space
from src.pricing import pricing_input, pricing_output, count_token

# OpenAI API key
openai.api_key = st.secrets["api_key"]

# Page title
title = "<h1 style='text-align: center; color: #23242B;'>GPTool</h1>"
st.markdown(title, unsafe_allow_html=True)
space(2)

# Columns initialization
col1, col2 = st.columns([1,2])

# Select model and temperature
with col1:
    model = st.selectbox("Select model",
                         ["gpt-3.5-turbo", "gpt-4", "babbage", "ada", "curie", "davinci"])
with col2:
    temperature = st.slider("Temperature", 0.0, 2.0, 0.5, 0.1)

space(2)


# Define prompt
instruction = """You are an expert in Python, problem solving, data science and data
                visualization (matplotlib, seaborn, plotly and pandas). You are
                always happy to help others. You're very educational, explaining things
                in simple, intuitive terms. """
prompt = st.chat_input("Prompt")

# Define output
if prompt:
    start = time.time()
    message = st.chat_message("user")
    message.write(prompt)
    with st.spinner("Loading..."):
        output = api_gpt(prompt, instruction, temperature=temperature)
        total_tokens = count_token(prompt + output)
        total_price = pricing_input(model, total_tokens) + pricing_output(model, total_tokens)

        # Display pricing with output
        end = time.time()
        output = output + "\n\n" + f"Total tokens: {total_tokens} | Total price: ${total_price:.4f} | Time: {end-start:.2f} seconds"

        # Display output
        message = st.chat_message("assistant")
        message.write(output)


