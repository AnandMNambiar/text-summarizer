from flask import Flask, request, jsonify
from summarizer import generate_summary

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return jsonify({"ok": True, "message": "AI Text Summarizer API. POST /summarize with JSON {'text': '...'}"})

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "No text provided. Send JSON: {'text': '...'}"}), 400
    summary = generate_summary(text)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
