# text-summarizer
AI-powered text summarizer built with Python and Flask. Uses Hugging Face Transformers to generate concise summaries of long text. 🚀
# 📝 AI Text Summarizer

A simple Python + Flask project that summarizes long text using Hugging Face Transformers.

---

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Start the server:
   ```bash
   python app.py
curl -X POST http://127.0.0.1:5000/summarize \
  -H "Content-Type: application/json" \
  -d '{"text":"Artificial Intelligence is transforming industries by automating tasks, improving decision-making, and enabling personalized experiences."}'
{"summary": "AI is transforming industries by automating tasks, improving decisions, and creating personalized experiences."}
