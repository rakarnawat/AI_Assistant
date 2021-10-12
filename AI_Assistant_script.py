try:
    import speech_recognition as sr
    import pyttsx3
    import pyaudio
    import pywhatkit
    import datetime
    import wikipedia
    import twitter
    import wolframalpha
    from bs4 import BeautifulSoup
    import requests
    import csv
    import os
    from googlesearch import search
    from urllib.request import urlopen
    import webbrowser
    #from main import *
except:
    print("Internet issue1")
    exit()
try:
    app = wolframalpha.Client('/* your wolframalpha id */')
except:
    print('Internet Issue2')

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#global command
#i=99
engine.setProperty('rate', 180)
def start():
    try:
        engine.say("Hello")
        #engine.say("My name is john")
        #engine.say("I have a sister named, jennifer")
        #engine.say("With whom would you like to talk")
        engine.runAndWait()
    except:
        talk("i feel there is some error, wait!, will try again")
        start()
start()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            #talk("listening...")
            print('listening...')
            voice = listener.listen(source, phrase_time_limit=5)
            command = listener.recognize_google(voice, language='en-in')
            print("Recognised command : " + command)
            command = command.lower()
            global i
            i = 1
            if 'john' in command:
                engine.setProperty('voice', voices[0].id)
                command = command.replace('john', '')
                print(command)
                i = 1
            elif 'jennifer' in command:
                engine.setProperty('voice', voices[1].id)
                command = command.replace('jennifer', '')
                print(command)
                i = 1
            elif 'goodbye' in command:
                engine.say("ooh no!, ok!, bye!")
                engine.runAndWait()
                i = 0
                AlwaysWakeUp()
                #engine.stop()
                #exit()
            #engine.runAndWait()
    except:
        print("timeout or some error" + take_command())
        run_assistant()
    return command

take_command()
#print(i)
if i == 1:
    engine.say("Hello sir!, how may i help you?")
    engine.runAndWait()


def AlwaysWakeUp():
    try:
        with sr.Microphone() as source:
            #talk("listening...")
            print('listening...')
            voice = listener.listen(source, phrase_time_limit=5)
            global command
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            print(command)
        if "hey john" in command:
            engine.setProperty('voice', voices[0].id)
            run_assistant()
        elif "hey jennifer" in command :
            engine.setProperty('voice', voices[1].id)
            run_assistant()
        else:
            AlwaysWakeUp()
    except:
        talk("Sorry! what?, i didn't understand that")
        AlwaysWakeUp()

def run_assistant():
    try:
        command = take_command()
        print("Searching for " + command)
        if 'who are you' in command:
            talk("I am your assistant")
        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is ' + time)

        elif 'jor se bolo' in command :
            person = command.replace('bolo', '')
            print(person)
            talk('jai, mata, di')
        elif 'namaste' in command:
            person = command.replace('namaste', '')
            print(person)
            talk('namaste! seth ji!')
        elif 'hack wifi' in command:
            print("ok")
        else:
            try:
                res = app.query(command)
                print(next(res.results).text)
                talk(next(res.results).text)
            except:
                google = 1
            try:
                if google == 1:
                    query = command
                    mylist = []
                    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                        print(j)
                        mylist.append(j)
                        print(mylist)
                    for a in range(len(mylist)):
                        if 'wiki' in mylist[a]:
                            person = command.replace('who is', '')
                            print(person)
                            talk('Searching for ' + person)
                            info = wikipedia.summary(person, 1)
                            print(info)
                            talk(info)
                            exit(j)
                            exit(a)
                        elif 'wiki' not in mylist[a]:
                            print("its not in Wikipedia")
                            print(mylist[0])
                            webbrowser.open_new(mylist[0])
                            exit(j)
                            exit(a)
                else:
                    print("ooh no! I don't know about that, would you like to ask something else! ")
                    talk("ooh no! I don't know about that, would you like to ask something else! ")
            except:
                print("I guess there is some issue!")
                #talk("I guess there is some issue!")
    except:
        talk("I didn't understand that, can you say it again!")

while i==1:
    run_assistant()

else:
    AlwaysWakeUp()

def cmd():
    command = take_command()
