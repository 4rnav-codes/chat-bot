from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()

app = Flask(__name__)

limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])

genai.configure(api_key=os.getenv("AIzaSyBNQgqfuY9oJy2XACIwy9Cm37HY1H5X9z8"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
@limiter.limit("5 per minute")
def chat():
    user_msg = request.json.get("message")

    try:
        response = model.generate_content(user_msg)
        reply = response.text
    except Exception as e:
        reply = "Error: " + str(e)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
