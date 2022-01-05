import webbrowser
from modules.audio import speak, listen
from modules.googlecalender import authenticate_google,get_date,get_events
from datetime import datetime
import os
import config
from cv2 import *

def camera():
    # initialize the camera
    cam = VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
        imshow("cam-test",img)
        waitKey(0)
        destroyWindow("cam-test")
        imwrite("filename.jpg",img) #save image

def get_schedule(query_list):
    '''Get all events on a particular day and read them out.'''
    date = get_date(query_list)
    service = authenticate_google()
    events = get_events(date, service)
    if not events:
        speak('No upcoming events found.')
    else:
        speak(f"You have {len(events)} events on this day.")

        for event in events:
            '''
            dictionary.get(keyname, value)
            Args:
                keyname: The keyname of the item you want to return the value from
                value: A value to return if the specified key does not exist. Returns None by default.
            
            If dateTime does not exist search for date.
            '''
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event.get("summary"))
            
            start_time = str(start.split("T")[1].split("-")[0])
            
            if int(start_time.split(":")[0]) < 12:
                start_time = start_time + "AM"
            else:
                start_time = str(int(start_time.split(":")[0])-12)
                start_time = start_time + "PM"

            speak((event.get("summary") or "Event") + " at " + start_time)




def open_website(query_list,website_link):
    webbrowser.open(website_link)


def tell_time(query_list):
    time = datetime.now().strftime("%I %M %p")
    speak(f"The time is {time.replace('0','')}")


def tell_date(query_list):
    date = datetime.now().strftime("%d %B")
    speak(f"Today is {date.replace('0','')}")


def tell_day(query_list):
    day = datetime.now().strftime("%A")
    speak(f"Today is a {day}")


def play_music(query_list):
    songs = os.listdir(config.music_dir)
    if len(songs) > 0:
        speak("Here you go with music")
        random = os.startfile(os.path.join(config.music_dir, songs[0]))
    else:
        speak("There are no songs in the music folder.")
