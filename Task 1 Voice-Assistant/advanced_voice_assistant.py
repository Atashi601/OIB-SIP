import tkinter as tk
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        result_label.config(text="You said: " + command)

        if "time" in command.lower():
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Current time is " + current_time)

        elif "google" in command.lower():
            webbrowser.open("https://www.google.com")

        elif "youtube" in command.lower():
            webbrowser.open("https://www.youtube.com")

    except:
        speak("Sorry, I did not understand.")

# GUI Window
window = tk.Tk()
window.title("Voice Assistant")
window.geometry("400x300")

tk.Label(window, text="Voice Assistant", font=("Arial", 16)).pack(pady=10)

status_label = tk.Label(window, text="Click the button and speak")
status_label.pack(pady=5)

tk.Button(window, text="Start Listening", command=listen).pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=5)

window.mainloop()
