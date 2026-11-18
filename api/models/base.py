from jsonschema import validate, ValidationError, FormatChecker

class ModeloBase:
    schema = None
    _columna_db = None

    def __init_subclass__(cls, **kwargs):
        super().__init__subclass__(**kwargs)

        if cls.schema is None or cls._columna_db is None:
            raise NotImplementedError(
                f"{cls.__name__} debe definir 'schema' y '_columna_db'."
            )

        cls._campos = list(cls.schema["properties"].keys())

        if set(cls._campos) != set(cls._columna_db):
            raise ValueError(
                f"{cls.__name__}: los campos del schema {sorted(cls._campos)} "
                f"no coinciden con los del mapeo {sorted(cls._columna_db)}."
            )

    @classmethod
    def validar(cls, datos):
        try:
            validate(instance=datos, schema=cls.schema, format_checker=FormatChecker())
            return True, None
        except ValidationError as error:
            return False, error.message

    def __init__(self, fila_dict):
        self._id = fila_dict["id"]
        self._datos = {
            campo: fila_dict[columna]
            for campo, columna in self._columna_db.items()
        }

    def to_json(self):
        return {"id": self._id, **self._datos}