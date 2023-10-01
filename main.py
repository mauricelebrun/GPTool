
try:
    import streamlit as st
    import openai
    import pyttsx3
    import random
    from src.gpt import api_gpt
    from src.front import space
    from src.voice import speak

    # OpenAI API key
    openai.api_key = st.secrets["api_key"]

    # Init pyttsx3
    engine = pyttsx3.init()

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

        # Limit prompt length
        prompt = prompt[-10000:]

        # Generate assistant response
        response = api_gpt(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

except:
    texts_error = ['Henri is busy painting the bloom of Japanese nuclear plankton',
                   'Henri is busy observing the wild birds in the Bois de Boulogne.',
                   'Henri is puzzled by Northern Lights above the butte Chaumont.']
    st.error(random.choice(texts_error))