from flask import Flask, request
import requests
import os

TOKEN = os.environ.get("BOT_TOKEN")
URL = https://api.telegram.org/bo7984880246:AAHl6hcrprel6GLQ5mti6xeioPA0IaGWQSU/setWebhook?url=https://seu-bot.onrender.com/7984880246:AAHl6hcrprel6GLQ5mti6xeioPA0IaGWQSU


app = Flask(__name__)

def send_message(chat_id, text):
    requests.post(URL + "sendMessage", data={"chat_id": chat_id, "text": text})

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id]"]
        text = data["message"].get("text", "")

        if text.startswith("/cpf"):
            send_message(chat_id, "🔍 Consulta de CPF não implementada ainda.")
        elif text.startswith("/telefone"):
            send_message(chat_id, "📞 Consulta de telefone não implementada ainda.")
        else:
            send_message(chat_id, "Comandos disponíveis: /cpf, /telefone")

    return {"ok": True}

@app.route("/")
def home():
    return "Bot online!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

