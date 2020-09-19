import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour>12:
        speak("Good Morning Shubham!")
    elif hour>=12 and hour>18:
        speak("Good Afternoon Shubham!")
    else:
        speak("Good Evening Shubham!")    
    speak("Hey! Shubham I am Riya. How may I help you ?")    

def takecammand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query 

if __name__ == "__main__":
    wishMe
    while True:
        query =takecammand().lower() 

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
             speak('Searching Wikipedia...')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=100)
             speak("According to wikipedia")
             print(results)
             speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
             music_dir = 'd:\\music'
             music = os.listdir(music_dir)
             print(music)
             speak("playing music.....")
             os.startfile(os.path.join(music_dir, music[0]))
             
        elif 'open vs code' in query:
            codePath = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening vs code")
            print("opening vs code...")
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak("opening chrome")
            print("opening chrome...")
            os.startfile(codePath)

        elif 'open microsoft edge' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft\\edge\\Application\\msedge.exe"
            speak("opening microsoft edge")
            print("opening microsoft edge...")
            os.startfile(codePath)

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"hey shubham it is {strtime}")
            print(strtime)
            












   
        



    

