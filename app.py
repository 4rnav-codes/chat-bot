from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])

genai.configure(api_key=os.getenv("AIzaSyBICKj3JVvhgJAlbA153Cfrzqh4Dqtg1Lw"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
@limiter.limit("5 per minute")
def chat():
    user_msg = request.json.get("message")

    try:
        response = model.generate_content(user_msg)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": "Error: " + str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
