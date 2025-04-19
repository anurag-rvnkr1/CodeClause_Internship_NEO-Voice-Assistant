# Neo-Voice-Assistant 🎙️✨

![NeoVoice Snap](https://github.com/anurag-rvnkr1/CodeClause_Internship_NEO-Voice-Assistant/blob/main/screenshots/assistant%20UI.jpg)

<div align="center">
  
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
  [![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/username/neovoice-assistant/pulls)
  
  <h3>A modern, responsive voice assistant with an elegant UI and seamless speech recognition</h3>

  [Features](#features) • 
  [Demo](#demo) • 
  [Installation](#installation) • 
  [Usage](#usage) • 
  [Database](#database) • 
  [Customization](#customization) • 
  [Contributing](#contributing)
  
</div>

## 🎬 Demo

<details>
<summary>Click to see NeoVoice in action! 👀</summary>
<br>
<p align="center">
  <img src="https://github.com/anurag-rvnkr1/CodeClause_Internship_NEO-Voice-Assistant/blob/main/screenshots/demo%20(1).gif" alt="NeoVoice Demo Extended" width="700px"/>
</p>
</details>

## 📋 Features

<table>
  <tr>
    <td width="50%">
      <h3>🔊 Voice Recognition</h3>
      <ul>
        <li>Real-time speech recognition using Web Speech API</li>
        <li>Smooth voice processing with visual feedback</li>
        <li>Support for continuous conversation</li>
      </ul>
    </td>
    <td width="50%">
      <h3>🗣️ Text-to-Speech</h3>
      <ul>
        <li>Natural-sounding voice responses</li>
        <li>Configurable speech rate and volume</li>
        <li>Visual sound wave animation during playback</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <h3>💾 Persistent Storage</h3>
      <ul>
        <li>SQLite database integration</li>
        <li>Command history tracking</li>
        <li>Conversation storage for future analysis</li>
      </ul>
    </td>
    <td>
      <h3>🎨 Modern UI</h3>
      <ul>
        <li>Responsive glassmorphic design</li>
        <li>Interactive 3D effects and animations</li>
        <li>Clean conversation interface with bubbles</li>
      </ul>
    </td>
  </tr>
</table>

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Git

### 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/anurag-rvnkr1/CodeClause_Internship_NEO-Voice-Assistant.git
cd CodeClause_Internship_NEO-Voice-Assistant
```

2. **Create and activate a virtual environment** (recommended)

```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

> 📝 **Note for macOS/Linux users**: You might need to install additional dependencies for PyAudio:
> ```bash
> # For macOS (using Homebrew)
> brew install portaudio
> 
> # For Ubuntu/Debian
> sudo apt-get install python3-pyaudio
> ```

### 🏃‍♂️ Running the Application

1. **Initialize the database**

```bash
# Start Python interactive shell
python

# In the Python shell
>>> from app import init_db
>>> init_db()
>>> exit()
```

Alternatively, you can use this one-liner:

```bash
python -c "from app import init_db; init_db()"
```
  (OR)
```bash
flask init-db
```
2. **Start the Flask application**

```bash
flask run
```

3. **Access the application**

Open your web browser and navigate to:
```
http://127.0.0.1:5000/
```


## 💬 Usage Guide


1. **Click the microphone button** 🎙️ to start recording your voice
2. **Speak your command** clearly into your microphone
3. **Wait for processing** while the system analyzes your request
4. **Listen to the response** as NeoVoice speaks back to you
5. **View the conversation history** in the chat area

### 📝 Sample Commands

- "Hello" - Greet the assistant
- "What time is it?" - Get the current time
- "What's today's date?" - Get the current date
- "How's the weather?" - Get a (simulated) weather report
- "Who are you?" - Learn about the assistant
- "Thank you" - Express gratitude

## 🗄️ Database

NeoVoice Assistant stores all conversations in an SQLite database called `assistant.db`. The database schema is as follows:

```sql
CREATE TABLE conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    command TEXT NOT NULL,
    response TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
```

You can view the database contents using any SQLite database browser or with the following command:

```bash
sqlite3 assistant.db "SELECT * FROM conversations"
```

## 🎨 Customization

### Modifying the Assistant's Responses

To customize how the assistant responds to different commands, edit the `process_command()` function in `app.py`:

```python
def process_command(command):
    command = command.lower()
    
    # Add your custom command handling here
    if "your_custom_command" in command:
        return "Your custom response"
    
    # Existing commands...
```

### Voice Settings

You can adjust the voice settings in the `get_tts_engine()` function:

```python
def get_tts_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed: higher = faster
    engine.setProperty('volume', 1.0)  # Volume: 0.0 to 1.0
    
    # Get available voices and set a preferred one
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0=male, 1=female
    
    return engine
```

### UI Customization

The UI is highly customizable through the CSS in `templates/index.html`. You can change colors by modifying the CSS variables:

```css
:root {
    --bg-dark: #111927;
    --bg-darker: #0a101e;
    --primary: #6d5acd;  /* Change this for main accent color */
    --primary-light: #8a7ee0;
    --primary-dark: #4e3ca9;
    --accent: #00ccb1;   /* Change this for secondary accent color */
    /* Other variables... */
}
```

## 🔍 Project Structure

```
CodeClause_Internship_NEO-Voice-Assistant/
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── assistant.db          # SQLite database (created on init)
└── templates/
    └── index.html        # Frontend interface
```

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request

### Coding Standards

- Follow PEP 8 for Python code
- Add comments for complex logic
- Update documentation for new features

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Flask team for the wonderful web framework
- Web Speech API for voice recognition capabilities
- All contributors who have helped improve this project

---

<div align="center">
  Made with ❤️ by <a href="https://github.com/anurag-rvnkr1">Anurag Revankar</a>
  <br><br>
  <img src="https://forthebadge.com/images/badges/built-with-love.svg" alt="Built with Love">
</div>
