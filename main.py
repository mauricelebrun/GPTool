import streamlit as st
import openai
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
col1, col2 = st.columns(2)

# Select model and temperature
with col1:
    model = st.selectbox("Select model",
                         ["gpt-3.5-turbo", "gpt-4", "babbage", "ada", "curie", "davinci"])
with col2:
    temperature = st.slider("Temperature", 0.0, 2.0, 0.5, 0.1)


# Define prompt
instruction = "An helpful AI assistant"
prompt = st.chat_input("Prompt")

# Define output
if prompt:
    message = st.chat_message("user")
    message.write(prompt)
    with st.spinner("Loading..."):
        output = api_gpt(prompt, instruction, temperature=temperature)
        total_tokens = count_token(prompt + output)
        total_price = pricing_input(model, total_tokens) + pricing_output(model, total_tokens)

        # Display pricing with output
        output = output + "\n\n" + f"Total tokens: {total_tokens} | Total price: ${total_price:.4f}"

        # Display output
        message = st.chat_message("assistant")
        message.write(output)


