import os
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["user_input"]
    conversation_history = request.json["conversation_history"]
    prompt = f"{conversation_history}User: {user_input}\nAI:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3750,
        n=1,
        stop=None,
        temperature=0.8,
    )

    message = response.choices[0].text.strip()
    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

