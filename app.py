from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("8829161990:AAEsDZYnmtmwCPqat9QHrnaeiZ0nKXH-Xas")
CHAT_ID = os.environ.get("7650979922")


@app.route("/")
def home():
    return "Bot Running"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    message = data.get("message", "Signal")

    telegram_url = f"https://api.telegram.org/bot{8829161990:AAEsDZYnmtmwCPqat9QHrnaeiZ0nKXH-Xas}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(telegram_url, json=payload)

    return {"status": "success"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)