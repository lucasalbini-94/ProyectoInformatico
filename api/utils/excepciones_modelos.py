class ModelosError(Exception):
    """Excepción base para errores de validación de modelos."""
    pass

class IdInexistenteError(ModelosError):
    """Excepción para indicar que el id no existe en la tabla asociada al recurso en la base de datos."""
    def __init__(self, recurso, id):
        super().__init__(f"No existe el recurso '{recurso}' con id {id}.")

class ColumnaUnicaDuplicadaError(ModelosError):
    """Excepción para indicar que se ha intentado insertar un valor duplicado en una columna única."""
    def __init__(self, campo, valor):
        super().__init__(f"Ya existe un recurso con el valor '{valor}' en el campo '{campo}'.")

class ColumnaNoNulaError(ModelosError):
    """Excepción para indicar que se ha intentado insertar un valor nulo en una columna que no permite nulos."""
    def __init__(self, campo):
        super().__init__(f"El valor en el campo '{campo}' no puede ser nulo.")