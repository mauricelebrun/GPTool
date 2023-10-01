from os import system
import sys
import pyttsx3
from pydub import AudioSegment

def speak(text, engine):
    ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!-_$:+-/ ")
    clean_text = ''.join(c for c in text if c in ALLOWED_CHARS)
    engine.say(clean_text)
    engine.runAndWait()