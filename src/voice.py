import streamlit as st
#from gtts import gTTS



def speak(text, engine):

    # clean text
    ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!-_$:+-/ ")
    clean_text = ''.join(c for c in text if c in ALLOWED_CHARS)

    # save audio to file
    engine.setProperty('rate', 165)
    engine.save_to_file(clean_text, '../output.mp3')
    engine.runAndWait()
    print('file saved')

    # play audio
    audio_bytes = open('../output.mp3', 'rb').read()
    st.audio(audio_bytes, format='audio/mp3')

    # say text
    #
    #engine.say(clean_text)
    #engine.runAndWait()
    #



