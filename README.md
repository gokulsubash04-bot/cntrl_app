# 🎙️ Control App (cntrl_app)

A Python-based, voice-controlled assistant designed to programmatically manage common Windows applications using speech recognition. Simply speak to open or close apps like WhatsApp, Google Chrome, Notepad, and the Calculator.

---

## ✨ Features

- **🎙️ Speech Recognition**: Utilizes Google's speech recognition engine via the `speech_recognition` library to process audio commands in real-time.
- **🚀 Native Integration**: Opens applications instantly using native Windows URI schemes and shell execution.
- **🛑 Forceful Closure**: Seamlessly terminates application processes using the Windows `taskkill` command.
- **🔄 Continuous Listening**: Runs in an interactive loop, continuously monitoring for your commands.

---

## 🛠️ Supported Voice Commands

| Voice Command | Action Description | Target Process / Command |
| :--- | :--- | :--- |
| **"open whatsapp"** | Launches the WhatsApp UWP application | `start whatsapp:` |
| **"close whatsapp"** | Force-closes all WhatsApp processes | `taskkill /f /im WhatsApp.Root.exe` |
| **"open chrome"** | Launches Google Chrome browser | `start chrome` |
| **"close chrome"** | Force-closes Google Chrome | `taskkill /f /im chrome.exe` |
| **"open notepad"** | Launches standard Windows Notepad | `notepad` |
| **"close notepad"** | Force-closes Notepad | `taskkill /f /im notepad.exe` |
| **"open calc"** | Launches Windows Calculator | `calc` |
| **"close calc"** | Force-closes the Calculator app | `taskkill /f /im CalculatorApp.exe` |
| **"close all"** | Closes all supported applications at once | Clears Chrome, Notepad, WhatsApp, and Calculator |

> [!NOTE]
> Modern Universal Windows Platform (UWP) apps installed from the Microsoft Store (such as WhatsApp and Calculator) use specific process names (`WhatsApp.Root.exe` and `CalculatorApp.exe`) rather than standard filenames. The application has been fully optimized to target these correct process names.

---

## 🚀 Getting Started

### 📋 Prerequisites

- **Operating System**: Windows (required for specific shell commands and `taskkill`).
- **Python Version**: Python 3.8 or higher.
- **Hardware**: An active microphone.

### 🔌 Installation

1. **Clone or navigate** to the project directory:
   ```bash
   cd d:\codeing\cntrl_app
   ```

2. **Activate the virtual environment** (if using one):
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install the required dependencies**:
   ```bash
   pip install SpeechRecognition pyaudio
   ```

> [!TIP]
> If you encounter issues installing `pyaudio` on Windows, you can install the pre-compiled wheel using pip, or install it via `pip install pipwin` followed by `pipwin install pyaudio`.

### 🎮 Running the App

Execute the main controller script:
```bash
python test.py
```

Once running, the app will output `Listening...🙉🙉🙉🙉🙉`. Simply speak any of the supported commands clearly into your microphone!

---

## 📂 Project Structure

- [test.py](file:///d:/codeing/cntrl_app/test.py): The main application script containing speech recognition and command execution logic.
- [README.md](file:///d:/codeing/cntrl_app/README.md): Documentation of the application.
