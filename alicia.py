import pyttsx3
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import ctypes
import time
import keyboard

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 < hour < 12:
        speak("good morning sir ji")
    elif 12 < hour < 18:
        speak("Good After noon sir ji")
    else:
        speak("Good evening sir")
    speak("I am ALICIA . ONE  POINT O how may i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.energy_threshold = 1200
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n ")
    except Exception as e:
        print(e)
        print("Say that again")
        return "NONE"
    return query


if __name__ == "__main__":
    wishme()

    while True:

        query = takecommand().lower()

        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            speak(f"Searching for {query} on wikipedia ")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'hello' in query:
            speak("Hello sir ")

        # CODE WITH HARRY CHANNEL
        elif 'code with harry' in query:
            webbrowser.open("https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww")
        elif 'codewithharry' in query:
            webbrowser.open("https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww")

        # JAVA PLAYLIST BY HARRY BHAIYA
        elif 'java playlist' in query:
            webbrowser.open("https://www.youtube.com/watch?v=ntLJmHOJ0ME&list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q")
        elif 'javaplaylist' in query:
            webbrowser.open("https://www.youtube.com/watch?v=ntLJmHOJ0ME&list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q")

        # ANDROID DEVELOPMENT BY ANUJ BHAIYA
        elif 'Android' in query:
            webbrowser.open("https://www.youtube.com/watch?v=mndwTFO9glI&list=PLUcsbZa0qzu3Mri2tL1FzZy-5SX75UJfb")

        # SOFTWARE ENGINEERING PLAYLIST BY RAJIB MALL
        elif 'software engineering playlist' in query:
            webbrowser.open("https://www.youtube.com/playlist?list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt")
        elif 'softwareengineeringplaylist' in query:
            webbrowser.open("https://www.youtube.com/playlist?list=PLbRMhDVUMngf8oZR3DpKMvYhZKga90JVt")

        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/")



        elif 'quit' in query:
            speak("CLOSING THE PROGRAM")
            quit()
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")
        elif 'chrome' in query:
            speak("Opening google Chrome")
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
        elif 'close' in query:
            speak("Closing the chrome")
            browserExe = "chrome.exe"
            os.system("taskkill /f /im " + browserExe)

        elif 'code' in query:
            speak("Opening VIsual studio code")
            vspath = "C:\\Users\\Rahul\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(vspath)
        elif 'pycharm' in query:
            speak("Opening pycharm ")
            charmpath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.1\\bin\\pycharm64.exe"
            os.startfile(charmpath)
        elif 'java' in query:
            speak("Opening Intellij idea")
            javapath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.2.1\\bin\\idea64.exe"
            os.startfile(javapath)
        elif 'c drive' in query:
            speak("Opening c drive")
            cpath = "C:\\"
            os.startfile(cpath)
        elif 'd drive' in query:
            speak("Opening D drive")
            dpath = "D:\\"
            os.startfile(dpath)
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle bin IS empty now")
        elif 'switch tab' in query:
            speak("Switching the tab")
            keyboard.press_and_release('alt+tab')
        elif 'switch to tab' in query:
            speak("Switching the tab")
            keyboard.hook_key = 'alt'
            keyboard.press_and_release('tab+tab')
        elif 'switch three tab' in query:
            speak("Switching the tab")
            keyboard.press_and_release('alt+tab+tab+tab')
        elif 'switch four tab' in query:
            speak("Switching the tab")
            keyboard.press_and_release('alt+tab+tab+tab')
        elif 'take rest' in query:
            speak("ok sir")
            time.sleep(10)
        elif 'hibernate' in query:
            speak("Putting the system to hibernate")
            os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")
            quit()
        elif 'wake up' in query:
            speak("Alicia one point O on Duty sir")
            ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)
        elif 'sleep' in query:
            speak("Putting the system on sleep")
            ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)
        elif 'clear' in query:
            speak("Clearing the cache Of the system")
        elif 'made you' in query:
            speak("Thankxx to Rahul sir for taking me in this world")
        elif 'develop' in query:
            speak("i am developed by Mister Rahul")
        elif 'are you' in query:
            speak("I am fine Sir Thankxx FOr asking")
        elif 'you ready' in query:
            speak("YES SIR LETS ROCK")

        if 'play music' in query:
            music_dir = 'D:\\Songs\\English songs'
            songs = os.listdir(music_dir)
            speak("Playing the song ")
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))

        elif 'play next' in query:
            music_dir = 'D:\\Songs\\English songs'
            songs = os.listdir(music_dir)
            print(songs)
            speak("Playing the next song ")
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))
        elif 'music app' in query:
            speak("Closing the app")
            browserExe = "Music.UI.exe"
            os.system("taskkill /f /im " + browserExe)
