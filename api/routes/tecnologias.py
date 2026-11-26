from flask import jsonify
from api.models.tecnologia.tecnologia import Tecnologia
from api import app

@app.route('/tecnologias', methods=['GET'])
def get_tecnologias():
    lista = Tecnologia.get_tecnologias()
    return jsonify(lista), 200

@app.route('/tecnologias/<int:id>', methods=['GET'])
def get_tecnologias_por_id(id):
    tecnologia = Tecnologia.get_tecnologias_por_id(id)
    return jsonify(tecnologia), 200