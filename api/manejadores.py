# api/manejadores.py
from werkzeug.exceptions import HTTPException
from flask import jsonify

# Errores provenientes de mysql.connector
from mysql.connector.errors import (
    IntegrityError, OperationalError, ProgrammingError, DataError, Error as MySQLError
)

# Errores personalizados de los modelos
from api.utils.excepciones_modelos import (
    ModelosError, IdInexistenteError, ColumnaUnicaDuplicadaError, ColumnaNoNulaError
)

# Errores personalizados de los request
from api.utils.excepciones_request import RequestError

# Mapeo de errores de modelos a códigos de estado HTTP
MAPEO_STATUS = {
    IdInexistenteError: 404,
    ColumnaUnicaDuplicadaError: 409,
    ColumnaNoNulaError: 400,
}


def registrar_manejadores(app):

    @app.errorhandler(ModelosError)
    def manejar_modelos_error(error):
        status = MAPEO_STATUS.get(type(error), 400)
        return jsonify({"message": str(error)}), status

    @app.errorhandler(IntegrityError)
    def manejar_integrity_error(error):
        return jsonify({"message": "El recurso ya existe o viola una restricción de datos"}), 409

    @app.errorhandler(DataError)
    def manejar_data_error(error):
        return jsonify({"message": "Uno o más valores no son válidos para la base de datos"}), 400

    @app.errorhandler(OperationalError)
    def manejar_operational_error(error):
        return jsonify({"message": "Servicio no disponible, intente más tarde"}), 503

    @app.errorhandler(ProgrammingError)
    def manejar_programming_error(error):
        return jsonify({"message": "Error interno del servidor"}), 500

    @app.errorhandler(MySQLError)
    def manejar_mysql_error_generico(error):
        return jsonify({"message": "Error interno del servidor"}), 500

    @app.errorhandler(RequestError)
    def manejar_request_error(error):
        return jsonify({"message": str(error)}), 400

    @app.errorhandler(HTTPException)
    def manejar_http_exception(error):
        # 404 de ruta inexistente, 405 de metodo no implementado: conservan su código, pero en JSON
        return jsonify({"message": error.description}), error.code

    @app.errorhandler(Exception)
    def manejar_error_inesperado(error):
        return jsonify({"message": "Error interno del servidor"}), 500