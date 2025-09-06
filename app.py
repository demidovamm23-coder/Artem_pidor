from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Загружаем стихи
with open("poems.json", "r", encoding="utf-8") as f:
    poems = json.load(f)

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.json
    return jsonify({
        "version": "1.0",
        "session": req.get("session", {}),
        "response": {"text": "Привет! Давай читать стихи.", "end_session": False}
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
