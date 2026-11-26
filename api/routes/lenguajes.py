from flask import jsonify
from api.models.lenguaje.lenguaje import Lenguaje
from api import app

@app.route('/lenguajes', methods=['GET'])
def get_lenguajes():
    lista = Lenguaje.get_lenguajes()
    return jsonify(lista), 200

@app.route('/lenguajes/<int:id>', methods=['GET'])
def get_lenguajes_por_id(id):
    lenguaje = Lenguaje.get_lenguajes_por_id(id)
    return jsonify(lenguaje), 200