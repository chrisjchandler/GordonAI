from flask import Flask, render_template, request, jsonify
import os
import requests
import json

app = Flask(__name__)
openai_api_key = os.environ["OPENAI_API_KEY"]

headers = {
    'Authorization': f'Bearer {openai_api_key}',
    'Content-Type': 'application/json'
}

conversation_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    user_input = request.json["user_input"]

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": conversation_history + [{"role": "user", "content": user_input}]
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        data = response.json()
        message = data['choices'][0]['message']['content'].strip()
        conversation_history.append({"role": "assistant", "content": message})
    else:
        message = "An error occurred."

    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

