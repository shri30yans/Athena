import webbrowser
from modules.audio import speak,listen
from datetime import datetime
import os
import config
import requests

def open_website(website_link):
    webbrowser.open(website_link)

def tell_time():
    time = datetime.now().strftime("%I %M %p")   
    speak(f"The time is {time.replace('0','')}")

def tell_date():
    date = datetime.now().strftime("%d %B")   
    speak(f"Today is {date.replace('0','')}")

def tell_day():
    day = datetime.now().strftime("%A")   
    speak(f"Today is a {day}")

def play_music():
        songs = os.listdir(config.music_dir)
        if len(songs) > 0:
            speak("Here you go with music")
            random = os.startfile(os.path.join(config.music_dir, songs[0]))
        else:
            speak("There are no songs in the music folder.")







