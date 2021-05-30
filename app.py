from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import bot

app = Flask(__name__)
CORS(app)


@app.get("/")
def index():
  # Apenas envia a página HTML
  return render_template('index.html')


@app.post("/ask")
def ask():
  # Aqui ocorre o processamento da pergunta
  request_data = request.get_json()
  question = request_data["question"]
  answer = bot.generate_answer(question)
  return jsonify(answer=answer), 200
