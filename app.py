from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    message = data.get("message", "Signal")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, json=payload)

    return {"status": "ok"}

@app.route('/')
def home():
    return "Bot Running"

app.run(host="0.0.0.0", port=5000)