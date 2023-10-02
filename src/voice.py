import streamlit as st
import time
import pyttsx3



def speak(text):

    # clean text
    ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!-_$:+-/ ")
    clean_text = ''.join(c for c in text if c in ALLOWED_CHARS)

    # Init pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    engine.say(clean_text)
    #engine.save_to_file(clean_text, '../name.mp3')
    engine.runAndWait()

    # wait until speaking is finished (approximate)
    time.sleep(len(clean_text)/10)



    # play audio with streamlit
    #st.audio('../name.mp3', format='audio/mp3')


