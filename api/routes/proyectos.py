from flask import jsonify
from api.models.proyectos.proyectos import Proyecto
from api import app
from api.utils.decoradores import validar_json


@app.route("/proyectos", methods=["GET"])
def get_proyectos():
    lista = Proyecto.get_proyectos()
    return jsonify(lista), 200

@app.route('/proyectos/<int:id>', methods = ["GET"])
def get_proyectos_por_id(id):
    proyecto = Proyecto.get_proyecto_por_id(id)
    return jsonify(proyecto), 200

@app.route("/proyectos/<int:id_usuario>/proyectos", methods=["GET"])
def get_proyectos_por_usuario(id_usuario):
    proyectos = Proyecto.get_proyectos_por_usuario(id_usuario)
    return jsonify(proyectos), 200

@app.route('/proyectos', methods=['POST'])
@validar_json(Proyecto.validar)
def post_proyectos(datos):
    nuevo = Proyecto.post_proyecto(datos)
    return jsonify(nuevo), 201

@app.route('/proyectos/<int:id>', methods=['PUT'])
@validar_json(Proyecto.validar)
def put_proyecto(id, datos):
    actualizado = Proyecto.put_proyecto(id, datos)
    return jsonify(actualizado), 200

@app.route('/proyectos/<int:id>', methods=['DELETE'])
def delete_proyectos(id):
    eliminado = Proyecto.delete_proyectos(id)
    return jsonify(eliminado), 200