from flask import Flask, jsonify, request
import random, os
app = Flask(__name__)
id_base = 100000
@app.route("/")
def home():
    return jsonify({"status": "API ON"})
@app.route("/criar")
def criar():
    global id_base
    id_base += 1
    senha = random.randint(100000, 999999)
    return jsonify({"status": "sucesso", "id": id_base, "senha": senha, "texto": f"ID: {id_base} | SENHA: {senha}"})
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
