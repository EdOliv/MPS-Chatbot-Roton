from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.get("/")
def index():
  # Apenas envia a página HTML
  return render_template('index.html')


@app.post("/ask")
def ask():
  # Aqui ocorre o processamento da pergunta
  request_data = request.get_json()
  question = request_data["question"]
  return jsonify(answer="Olá!"), 200
