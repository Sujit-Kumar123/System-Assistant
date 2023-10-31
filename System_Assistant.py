import pyttsx3                #For speak pip install pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import datetime

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
def speeak(args):
    """Speak by computer"""
    engine.say(args)
    engine.runAndWait()
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speeak('Good morning.')
    elif hour>=12 and hour<17:
        speeak('Good Afternoon.')
    else:
        speeak('Good Evening.')
    speeak('Sujit')
def recordAudio():
    """It take microphone input from user return string as output """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listerning.....')
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print('Recogning...')
        query=r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except:
        print('Say that again please....')
        return "None"
    return query




if __name__=='__main__':
    wish()
    while(True):
        que=recordAudio().lower()
        if 'wikipedia' in que:
            speeak('Searching wikipedia...')
            que=que.replace('wikipedia','')
            result=wikipedia.summary(que, sentences=2)
            speeak("According to wikipedia...")
            speeak(result)
        elif 'open youtube' in que:
            webbrowser.open("youtube.com")
        elif 'open google' in que:
            webbrowser.open("google.com")
        elif 'open facebook' in que:
            webbrowser.open("facebook.com")
        elif 'play videos' in que:
            mus = "G:\\machin_learning"
            song = os.listdir(mus)
            i = random.randint(0, len(song))
            print(i)
            os.startfile(os.path.join(mus, song[i]))
        elif 'the time' in que:
            time_str=datetime.datetime.now().strftime("%H:%M:%S")
            speeak(f"the time is {time_str}")
        elif 'open vscode' in que:
            codePath='C:\\Users\\sujit kumar\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
            os.startfile(codePath)
        #elif 'email to sujit' in que:
         #   print('Sujit')
