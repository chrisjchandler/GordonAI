from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]

conversation_history = "AI: Hi! My name is Gordon, how can I help you today?\n"
total_tokens = 4096

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    user_input = request.json["user_input"]
    conversation_history += f"User: {user_input}\nAI:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=conversation_history,
        max_tokens=total_tokens - len(conversation_history),
        n=1,
        stop=None,
        temperature=0.8,
    )
    message = response.choices[0].text.strip()
    conversation_history += message + "\n"

    remaining_tokens = total_tokens - len(conversation_history)

    is_code_block = message.startswith("```") and message.endswith("```")
    if is_code_block:
        message = message[3:-3]

    return jsonify({"message": message, "remaining_tokens": remaining_tokens, "is_code_block": is_code_block})

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

