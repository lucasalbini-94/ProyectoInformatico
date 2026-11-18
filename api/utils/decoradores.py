from functools import wraps
from flask import request
from api.utils.excepciones_request import CuerpoInvalidoError, DatosNoValidosError


def validar_json(modelo_validar):
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            datos = request.get_json(silent=True)

            if datos is None:
                raise CuerpoInvalidoError()

            es_valido, error = modelo_validar(datos)
            if not es_valido:
                raise DatosNoValidosError(error)

            return func(*args, datos=datos, **kwargs)
        return wrapper
    return decorador