from functools import wraps
from flask import request, jsonify
from api.models.usuario.usuario import Usuario
from api import app
from api.utils.decoradores import validar_json

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    lista = Usuario.get_usuarios()
    return jsonify(lista), 200

@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario_por_id(id):
    usuario = Usuario.get_usuario_por_id(id)
    return jsonify(usuario), 200

@app.route('/usuarios', methods=['POST'])
@validar_json(Usuario.validar)
def post_usuario(datos):
    nuevo = Usuario.post_usuario(datos)
    return jsonify(nuevo), 201

@app.route('/usuarios/<int:id>', methods=['PUT'])
@validar_json(Usuario.validar)
def put_usuario(datos, id):
    actualizado = Usuario.put_usuario(datos, id)
    return jsonify(actualizado), 200