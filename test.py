import subprocess
import os

apps = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "vs code": "C:\\Users\\GOKUL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe"
}

def open_app(name):
    if name in apps:
        subprocess.Popen(apps[name])
        print(f"Opening {name}")
    else:
        print("App not found")

#open_app("calculator")
#open_app("chrome")
#open_app("vs code")
#open_app("notepad")

def close_app(name):
    processes = {
        "chrome": "chrome.exe",
        "vs code": "Code.exe",
        "notepad": "notepad.exe",
        "calculator": "CalculatorApp.exe"
    }

    if name in processes:
        os.system(f'taskkill /f /im "{processes[name]}"')
if "close" in command:
        close_app("chrome")
        close_app("vs code")
        close_app("notepad")
        close_app("calculator")