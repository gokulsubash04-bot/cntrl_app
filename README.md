# Control App (cntrl_app)

A simple Python application to programmatically manage (open and close) common applications on Windows.

## Features

- **Open Applications**: Launch applications like Google Chrome, Visual Studio Code, Notepad, and Calculator using Python's `subprocess`.
- **Close Applications**: Terminate running instances of these applications using Windows `taskkill`.

## Supported Applications

The application contains configuration maps for:
- Google Chrome (`chrome`)
- Visual Studio Code (`vs code`)
- Notepad (`notepad`)
- Calculator (`calculator`)

## Getting Started

### Prerequisites

- **Operating System**: Windows (uses Windows-specific executable paths and `taskkill` commands).
- **Python**: Python 3.x installed.

### How to Use

The script defines functions to interact with the applications:

```python
from test import open_app, close_app

# Open Calculator
open_app("calculator")

# Close Chrome
close_app("chrome")
```

### Script Structure

- `apps`: A dictionary containing paths to application executables.
- `open_app(name)`: Launches the specified application.
- `close_app(name)`: Forcefully closes the specified application using `taskkill`.
