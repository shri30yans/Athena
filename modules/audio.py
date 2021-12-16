import speech_recognition as sr
import pyttsx3
import threading
import queue


class TTSThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.daemon = True
        self.start()

    def run(self):
        tts_engine = pyttsx3.init('sapi5')
        voices = tts_engine.getProperty('voices')
        tts_engine.setProperty('voice', voices[1].id)
        tts_engine.startLoop(False)
        t_running = True
        while t_running:
            if self.queue.empty():
                tts_engine.iterate()
            else:
                data = self.queue.get()
                tts_engine.say(data)
        tts_engine.endLoop()

# Creating a queue to send commands from the main thread
q = queue.Queue()
# Thread is auto-starting
tts_thread = TTSThread(q)  


def speak(audio):
    if audio is None:
        pass
    else:
        q.put(audio)

r = sr.Recognizer() 
 
def listen():
    with sr.Microphone() as source:
        '''
        r.adjust_for_ambient_noise()
        Adjusts the energy threshold dynamically using audio from source (an AudioSource instance) to account for ambient noise.
        Intended to calibrate the energy threshold with the ambient energy level. 
        Should be used on periods of audio without speech - will stop early if any speech is detected.
        '''
        #r.adjust_for_ambient_noise(source,duration = 2)

        '''
        r.pause_threshold 
        Represents the minimum length of silence (in seconds) that will register as the end of a phrase.
        '''
        r.pause_threshold = 0.6
        print("Listening...")
        try:
            audio = r.listen(source,timeout=4,phrase_time_limit=8)  
        
        except sr.WaitTimeoutError:
            print("listen() Timed out")
            return

        try:
            print("Recognizing...")   
            query = r.recognize_google(audio, language ='en-in', show_all=True)
            print(query)
            query_list = [x.get("transcript") for x in query.get("alternative")]
            print(f"User said: {query_list}")
        
        except sr.UnknownValueError:
            '''
            Google Speech Recognition could not understand the audio
            '''
            print("I could not understand what you said.")
            return 
    
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")
            speak("Request error")
            return 
        
        except Exception as e:
            #print(e)
            return
        
        return query_list