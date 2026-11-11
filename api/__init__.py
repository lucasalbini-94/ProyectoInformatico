from flask import Flask
from flask import jsonify
from flask import request

# Crear una instancia de Flask
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def test():
    return jsonify({'mensaje': 'Conectado a la API'})
