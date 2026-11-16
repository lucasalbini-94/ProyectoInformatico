from flask import Blueprint, jsonify, request
from api.models.usuarios import Usuario
from functools import wraps
import jwt
import datetime

auth_bp = Blueprint("auth", __name__)

SECRET_KEY = "mi_clave_secreta_super_segura"

def validar_json(modelo_validar):
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            datos = request.get_json()
            es_valido, error = modelo_validar(datos)
            if not es_valido:
                return jsonify({"mensaje": error}), 400
            return func(*args, **kwargs)
        return wrapper
    return decorador

@auth_bp.route("/api/login", methods=["POST"])
@validar_json(Usuario.validar_login)
def login():
    try:
        datos = request.get_json()
        email = datos.get("email")
        password = datos.get("password")

        usuario = Usuario.buscar_por_email(email)

        if usuario and Usuario.verificar_password(password, usuario["password_hash"]):
            payload = {
                "id_usuario": usuario["id"],
                "email": usuario["email"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

            return jsonify({
                "mensaje": "Login exitoso",
                "token": token,
                "usuario": {
                    "id": usuario["id"],
                    "nombre": usuario["nombre"],
                    "email": usuario["email"]
                }
            }), 200
        else:
            return jsonify({"mensaje": "Credenciales incorrectas"}), 401
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500


@auth_bp.route("/api/registro", methods=["POST"])
@validar_json(Usuario.validar_registro)
def registro():
    try:
        datos = request.get_json()
        usuario = Usuario.crear_usuario(datos)

        return jsonify({
            "mensaje": "Usuario creado correctamente",
            "usuario": {
                "id": usuario["id"],
                "nombre_usuario": usuario["nombre_usuario"],
                "email": usuario["email"]
            }
        }), 201
    except ValueError as e:
        return jsonify({"mensaje": str(e)}), 400
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500