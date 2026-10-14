import os
from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=BASE_DIR, static_url_path="")

@app.get("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()
    if not message:
        return jsonify(error="Bitte gib eine Frage ein."), 400
    if len(message) > 4000:
        return jsonify(error="Die Nachricht ist zu lang."), 400
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return jsonify(error="OPENAI_API_KEY ist auf dem Server nicht gesetzt."), 503
    try:
        client = OpenAI(api_key=api_key)
        history = data.get("history", [])
        msgs = [{"role": "system", "content": (
            "Du bist Jannoo Lernhilfe für Schüler. Antworte auf Deutsch, freundlich, "
            "verständlich und altersgerecht. Erkläre Aufgaben Schritt für Schritt, "
            "stelle Rückfragen wenn etwas fehlt und unterstütze beim Lernen, statt "
            "nur Lösungen hinzuklatschen. Erfinde keine Fakten. Halte Antworten meist kurz."
        )}]
        if isinstance(history, list):
            for item in history[-8:]:
                if isinstance(item, dict) and item.get("role") in ("user", "assistant"):
                    content = item.get("content", "")
                    if isinstance(content, str):
                        msgs.append({"role": item["role"], "content": content[:4000]})
        msgs.append({"role": "user", "content": message})
        response = client.chat.completions.create(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"), messages=msgs, max_tokens=700)
        return jsonify(reply=response.choices[0].message.content or "Ich konnte gerade keine Antwort formulieren.")
    except Exception:
        app.logger.exception("Chat request failed")
        return jsonify(error="Die Lernhilfe ist gerade nicht erreichbar."), 502

if __name__ == "__main__":
    # Lokal testen: http://127.0.0.1:5000
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=False)
