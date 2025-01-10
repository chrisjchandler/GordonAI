from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
import os
import requests
import json
import sqlite3

app = Flask(__name__)
openai_api_key = os.environ["OPENAI_API_KEY"]

# Flask-Session configuration
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key
Session(app)

# SQLite database initialization
def init_db():
    conn = sqlite3.connect('conversations.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            assistant_message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Initialize session history if it doesn't exist
    if 'conversation_history' not in session:
        session['conversation_history'] = []

    user_input = request.json["user_input"]

    # Build payload with user-specific history
    conversation_history = session['conversation_history']
    payload = {
        "model": "gpt-4o-mini",
        "messages": conversation_history + [{"role": "user", "content": user_input}]
    }

    headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json'
    }
    
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        data = response.json()
        raw_message = data['choices'][0]['message']['content'].strip()

        # Wrap response in code block formatting if it's code-like
        if "```" not in raw_message:
            formatted_message = f"```\n{raw_message}\n```"
        else:
            formatted_message = raw_message

        # Append to session-specific conversation history
        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "assistant", "content": formatted_message})
        session['conversation_history'] = conversation_history  # Save back to session

        return jsonify({"message": formatted_message})
    else:
        return jsonify({"message": "An error occurred."})

@app.route("/history", methods=["GET"])
def history():
    # Return session-specific conversation history
    conversation_history = session.get('conversation_history', [])
    return jsonify(conversation_history)

@app.route("/clear_session", methods=["POST"])
def clear_session():
    session.pop('conversation_history', None)  # Remove user-specific history
    return jsonify({"message": "Session cleared!"})

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

