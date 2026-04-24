from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot logic
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

responses = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there 😊 Welcome to college chatbot!",
        "Hey! Ask me anything about college."
    ],
    "admission": [
        "Admissions are open now. Visit college office or website.",
        "You can apply online through the portal."
    ],
    "courses": [
        "We offer CSE, IT, Mechanical, Civil and Electrical.",
        "Diploma and degree courses are available."
    ],
    "fees": [
        "Fees approx ₹30,000 - ₹70,000 per year.",
        "Contact accounts office for exact fees."
    ],
    "bye": [
        "Goodbye 👋",
        "See you later 😊"
    ]
}

def get_response(message):
    message = message.lower()

    if any(word in message for word in ["hello", "hi", "hey"]):
        return random.choice(responses["greeting"])

    elif "admission" in message:
        return random.choice(responses["admission"])

    elif "course" in message:
        return random.choice(responses["courses"])

    elif "fee" in message:
        return random.choice(responses["fees"])

    elif "bye" in message:
        return random.choice(responses["bye"])

    else:
        return "Sorry 🤖 I don't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_message = request.json["message"]
    return jsonify({"reply": get_response(user_message)})

if __name__ == "__main__":
    app.run(debug=True)
