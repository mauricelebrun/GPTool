import streamlit as st
import tiktoken as tk


def count_token(text, encoding_name="cl100k_base"):
    encoding = tk.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(text))
    return num_tokens

@st.cache_data(show_spinner=False)
def pricing_input(model, token):
    prices = {'gpt-3.5-turbo': 0.0015/1000*token,
              'gpt-4': 0.03/1000*token,
              'babbage': 0.0004/1000*token,
              'davinci': 0.002/1000*token,
              'curie': 0.0006/1000*token,
              'ada': 0.0008/1000*token
              }
    return prices[model]

@st.cache_data(show_spinner=False)
def pricing_output(model, token):
    prices = {'gpt-3.5-turbo': 0.002/1000*token,
              'gpt-4': 0.06/1000*token,
              'babbage': 0.0004/1000*token,
              'davinci': 0.002/1000*token,
              'curie': 0.0006/1000*token,
              'ada': 0.0008/1000*token
              }
    return prices[model]