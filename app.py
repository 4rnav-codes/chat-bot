from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot logic
def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi there! How can I help you?"
    elif "how are you" in user_input:
        return "I am fine 😊 What about you?"
    elif "name" in user_input:
        return "I am your AI Chatbot!"
    elif"college timing" in user_input:
        return "College timing was 10AM to 5PM "
    elif "college fee" in user_input:
        return "fee was Rs.11001 per year"
    elif "Branch available in college" in user_input:
        return "Available Branches are 1:- C.S.E. \n 2:- E.E. \n 3:- electrical engineering"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day 😊"
    else:
        return "Sorry, I don't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = get_response(user_message)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)