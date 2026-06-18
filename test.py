import speech_recognition as sr
import os

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...🙉🙉🙉🙉🙉")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command

    except Exception:
        return ""

def execute_command(command):
    if "open whatsapp" in command:
        os.system("start whatsapp:")
    elif "close whatsapp" in command:
        os.system("taskkill /f /im WhatsApp.Root.exe")
    elif "open chrome" in command:
        os.system("start chrome")
    elif "close chrome" in command:
        os.system("taskkill /f /im chrome.exe")

    elif "open notepad" in command:
        os.system("notepad")
    elif "close notepad" in command:
        os.system("taskkill /f /im notepad.exe")

    elif "open calc" in command:
        os.system("calc")
    elif "close calc" in command:
        os.system("taskkill /f /im CalculatorApp.exe")
    elif "close all" in command:
        os.system("taskkill /f /im WhatsApp.Root.exe")
        os.system("taskkill /f /im chrome.exe")
        os.system("taskkill /f /im notepad.exe")
        os.system("taskkill /f /im CalculatorApp.exe")
    else:
        print("Command not recognized(●'◡'●)(●'◡'●)(●'◡'●)")

while True:
    command = listen()
    execute_command(command)