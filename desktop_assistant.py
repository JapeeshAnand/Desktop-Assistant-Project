import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    '''
    It takes microphone audio input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-ca')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that gain please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', '')  # (email and password)
    server.sendmail('', to, content)  # (email)
    server.close()


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
    # logic for executing tasks based on query
        if('wikipedia' in query):
            speak("Searching Wikipedia...")
            query = query.replace("Wikipdedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif('open youtube' in query):
            webbrowser.open("youtube.com")

        elif('open google' in query):
            webbrowser.open("google.com")

        elif('open stackoverflow' in query):
            webbrowser.open("stackoverflow.com")

        elif('play music' in query):
            music_dir = ""  # music directory
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif('send email' in query):
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Who should I send it to?")
                to = takeCommand()
                sendEmail(to, content)
                speak("Emai;l has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email!")

        elif('stop' in query):
            break
