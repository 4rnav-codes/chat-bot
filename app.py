from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import google.generativeai as genai
import random, re

app = Flask(__name__)

limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["50 per hour"] 
)

genai.configure(api_key="AIzaSyBICKj3JVvhgJAlbA153Cfrzqh4Dqtg1Lw")
model = genai.GenerativeModel("gemini-pro")

def gemini_reply(message):
    try:
        response = model.generate_content(
            f"You are a helpful college assistant:\nUser: {message}"
        )
        return response.text
    except:
        return "AI is busy right now."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
@limiter.limit("10 per minute") 
def chat():
    user_message = request.json.get("message", "")

    if not user_message.strip():
        return jsonify({"reply": "Type something first."})

    return jsonify({"reply": gemini_reply(user_message)})

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({
        "reply": "Too many requests 🚫 Please slow down."
    }), 429

if __name__ == "__main__":
    app.run(debug=True)
