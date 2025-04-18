# app.py
from flask import Flask, render_template, request, jsonify
import pyttsx3
import datetime
import sqlite3
import os
import json
import random

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('assistant.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        command TEXT NOT NULL,
        response TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

# Initialize TTS engine
def get_tts_engine():
    engine = pyttsx3.init()
    # Adjust voice settings if needed
    engine.setProperty('rate', 150)  # Speed of speech
    return engine

# Process the command and return a response
def process_command(command):
    command = command.lower()
    
    # Basic command processing logic
    if "hello" in command or "hi" in command:
        return "Hello! How can I help you today?"
    
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}."
    
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today is {current_date}."
    
    elif "weather" in command:
        # In a real app, this would call a weather API
        weather_conditions = ["sunny", "cloudy", "rainy", "windy", "snowy"]
        temperatures = range(0, 35)
        condition = random.choice(weather_conditions)
        temp = random.choice(temperatures)
        return f"It's currently {condition} with a temperature of {temp} degrees Celsius."
    
    elif "who are you" in command:
        return "I'm your voice assistant, created to help you with various tasks and answer your questions."
    
    elif "thank you" in command or "thanks" in command:
        return "You're welcome! Is there anything else I can help you with?"
    
    else:
        return "I'm not sure how to respond to that. Could you phrase it differently?"

# Save conversation to database
def save_conversation(command, response):
    conn = sqlite3.connect('assistant.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO conversations (command, response) VALUES (?, ?)', 
                  (command, response))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-voice', methods=['POST'])
def process_voice():
    data = request.get_json()
    command = data.get('command', '')
    
    if not command:
        return jsonify({"error": "No command provided"}), 400
    
    response = process_command(command)
    
    # Save to database
    save_conversation(command, response)
    
    return jsonify({
        "command": command,
        "response": response
    })

if __name__ == '__main__':
    init_db()
    app.run(debug=True)