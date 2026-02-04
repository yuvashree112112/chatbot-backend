from flask import Flask, request, jsonify
from flask_cors import CORS
print(__name__)

app = Flask(__name__)
CORS(app)  # allow frontend to connect

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    # simple bot responses
    responses = {
        "hello": "Hi! How can I help you?",
        "hi": "Hello! Ask me anything.",
        "how are you": "I'm doing great! How are you?",
        "bye": "Goodbye! Have a nice day.",
        "your name": "I'm your Flask chatbot!",
    }

    for key in responses:
        if key in user_message:
            return jsonify({"reply": responses[key]})

    return jsonify({"reply": "Sorry, I don't understand that yet."})

if __name__ == "__main__":
    app.run(debug=True)
