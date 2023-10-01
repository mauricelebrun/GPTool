from os import system
import sys
import pyttsx3
import time

def speak(text, engine):

    # clean text
    ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!-_$:+-/ ")
    clean_text = ''.join(c for c in text if c in ALLOWED_CHARS)

    # say text
    engine.setProperty('rate', 165)
    engine.say(clean_text)
    engine.runAndWait()

    # wait for speech to finish
    while engine._inLoop:
        time.sleep(.1)
    engine.stop()


