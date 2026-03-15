import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I did not understand.")
        return ""

speak("Voice Assistant Activated")

while True:
    query = take_command()

    if "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak("Current time is " + current_time)

    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "exit" in query:
        speak("Goodbye!")
        break
