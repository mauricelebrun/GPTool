from os import system
import sys
import pyttsx3
from pydub import AudioSegment


#def save_audio_mp3(text, filename):
    




def speak(text):
    if sys.platform == 'darwin':
        ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!-_$:+-/ ")
        clean_text = ''.join(c for c in text if c in ALLOWED_CHARS)
        system(f"say '{clean_text}'")
    else:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()