import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
#from AI_Assistant_script import *
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.utils import asynckivy

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
except:
    print("Internet issue1")
    exit()
try:
    app = wolframalpha.Client('QHU7T6-KGL38TUHGG')
except:
    print('Internet Issue2')


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 180)
sendoutput= ''
def talk(text):
    engine.say(text)
    engine.runAndWait()
#def take_command():
#    return command

def run_assistant():
    try:
        print(choose)
        command = command1
        command = command.lower()
        print("Searching for " + command)
        if 'who are you' in command:
            if choose == 0:
                talk("I am your assistant")
            sendoutput = "I am your assistant"

        elif 'play' in command:
            song = command.replace('play', '')
            if choose == 0:
                talk('playing ' + song)
            sendoutput = pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            if choose == 0:
                talk('Current time is ' + time)
            sendoutput = 'Current time is ' + time
        elif 'jor se bolo' in command :
            person = command.replace('bolo', '')
            print(person)
            if choose == 0:
                talk('jai, mata, di')
            sendoutput = 'jai, mata, di'
        elif 'namaste' in command:
            person = command.replace('namaste', '')
            print(person)

            if choose == 0:
                talk('namaste! seth ji!')
            sendoutput = 'namaste! seth ji!'
        elif 'hack wifi' in command:
            print("ok")
            if choose == 0:
                talk('working on that')
            sendoutput = 'working on that'
        else:
            try:
                res = app.query(command)
                print(next(res.results).text)
                if choose == 0:
                    talk(next(res.results).text)
                sendoutput = next(res.results).text
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
                            if choose == 0:
                                talk('Searching for ' + person)
                            sendoutput = 'Searching for ' + person
                            info = wikipedia.summary(person, 1)
                            print(info)
                            if choose == 0:
                                talk(info)
                            sendoutput = info
                            exit(j)
                            exit(a)
                        elif 'wiki' not in mylist[a]:
                            print("its not in Wikipedia")
                            if choose == 0:
                                talk("its not in Wikipedia")
                            sendoutput = "its not in Wikipedia"
                            print(mylist[0])
                            sendoutput = mylist
                            webbrowser.open_new(mylist[0])
                            exit(j)
                            exit(a)
                else:
                    print("ooh no! I don't know about that, would you like to ask something else! ")
                    if choose == 0:
                        talk("ooh no! I don't know about that, would you like to ask something else! ")
                    sendoutput =  "ooh no! I don't know about that, would you like to ask something else! "

            except:
                print("I guess there is some issue!")
                #talk("I guess there is some issue!")

                MyLayout()
    except:
        if choose == 0:
            talk("I didn't understand that, can you say it again!")
        sendoutput = "I didn't understand that, can you say it again!"

    return sendoutput

class FirstWindow(Screen):
    def start(self):
        try:
            engine.say("jai shree krishna")
            engine.runAndWait()
        except:
            talk("i feel there is some error, wait!, will try again")

    # start()

class MyLayout(Screen):
    def press(self):
        #create a variable
        global command1, sendoutput, choose
        choose = 1
        command1 = self.ids.text_input.text
        sendoutput = self.ids.output.text
        print(command1)
        #update the label
        self.ids.output.text = run_assistant()
        self.ids.text_input.text = ''
        return choose
    def press1(self):
        #create a variable
        global command1, sendoutput, choose
        choose = 0
        sendoutput = self.ids.output.text
        command1 = self.ids.text_input.text
        print(command1)
        #update the label
        self.ids.output.text = run_assistant()
        self.ids.text_input.text = ''
        return choose
    def speech_recognition(self):
        global command1, sendoutput, choose
        choose = 0
        sendoutput = self.ids.output.text
        try:
            with sr.Microphone() as source:
                # talk("listening...")
                print('listening...')
                voice = listener.listen(source, phrase_time_limit=5)
                command1 = listener.recognize_google(voice, language='en-in')
                command1 = command1.lower()
                print("Recognised command : " + command1)
                self.ids.text_input.text = command1
        except:
            print('Some Error')
        # update the label
        return choose

    def speech_result(self):
        self.ids.output.text = run_assistant()
        self.ids.text_input.text = ''

class WindowManager(ScreenManager):
    pass

class mainApp(App):
    def build(self):
        kv = Builder.load_file('main.ky')
        return kv #MyLayout()

if __name__=="__main__":
    mainApp().run()

"""
def recognize_command():
    try:
        with sr.Microphone() as source:
            # talk("listening...")
            print('listening...')
            voice = listener.listen(source, phrase_time_limit=5)
            command = listener.recognize_google(voice, language='en-in')
            print("Recognised command : " + command)
            command = command.lower()
    except:
        print("Error in command recognition!")
    return command

class main(App):
    def build(self):
        superBox = RelativeLayout(size=(300, 300))
        btn1 = Button(text='hi', pos_hint={'top': 1}, size_hint=(1, 0.455))
        superBox.add_widget(btn1)
        btn2 = TextInput(text=recognize_command(), font_size=34, size_hint_y=None, pos_hint={"x": 0.0, "center_y": 0.495}, size_hint=(1, 0.1))
        superBox.add_widget(btn2)
        btn3 = Button(text='Search', pos_hint={"x": 0.0, "center_y": 0.358}, size_hint=(0.5, None))
        superBox.add_widget(btn3)
        btn4 = Button(text='Re-run', pos_hint={"x": 0.5, "center_y": 0.358}, size_hint=(0.5, None))
        superBox.add_widget(btn4)
        btn5 = Button(text='console output', pos_hint={'bottom': 1}, size_hint=(1, 0.273))
        superBox.add_widget(btn5)
        return superBox

    def set_heading(self):
        async def set_heading():
            await asynckivy.sleep(0.2)
            text_heading = self.strng.get_screen('main').ids.heading
            text_heading.text = recognize_command()

        asynckivy.start(set_heading())

#root = main()
if __name__ == "__main__":
    main().run()
#root.run()
"""
'''
class BoxLayoutApp(App):

    def build(self):
        superBox = BoxLayout(size=(300, 300))
        HB = BoxLayout(orientation='horizontal')
        VB = BoxLayout(orientation='vertical')
        btn1 = Button(text='one', pos_hint ={'top': 1}, size_hint=(1, 0.455))
        VB.add_widget(btn1)
        btn2 = Button(text='2', pos_hint={"x": 0.0, "center_y": 0.457}, size_hint=(0.5, None))
        VB.add_widget(btn2)
        btn3 = Button(text='3', pos_hint={"x": 0.5, "center_y": 0.457}, size_hint=(0.5, None))
        VB.add_widget(btn3)
        btn4 = Button(text='console output', pos_hint={'bottom': 1}, size_hint=(1, 0.368))
        VB.add_widget(btn4)
        superBox.add_widget(HB)
        superBox.add_widget(VB)
        return superBox

root = BoxLayoutApp()

root.run()
'''