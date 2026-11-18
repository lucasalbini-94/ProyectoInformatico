class RequestError(Exception):
    """Excepción base para errores relacionados con la petición HTTP en sí,
    antes de llegar a la lógica de negocio."""
    pass


class CuerpoInvalidoError(RequestError):
    """El cuerpo de la petición no es JSON válido."""
    def __init__(self):
        super().__init__("El cuerpo de la petición debe ser JSON válido")


class DatosNoValidosError(RequestError):
    """El cuerpo es JSON, pero no cumple con el schema del recurso."""
    def __init__(self, detalle):
        super().__init__(f"Datos inválidos: {detalle}")