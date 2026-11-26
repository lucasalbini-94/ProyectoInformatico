from api.db.db_config import get_db_connection
from api.utils.excepciones_modelos import IdInexistenteError
from api.models.base import ModeloBase

class Lenguaje(ModeloBase):
    schema = {
        "type": "object",
        "properties": {
            "nombre": {"type": "string"}
        }
    }
    _columna_db = {"nombre": "nombre"}

    @classmethod
    def get_lenguajes(cls):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM lenguajes")
        datos = cursor.fetchall()
        cursor.close()
        connection.close()

        return [cls(dato).to_json() for dato in datos]

    @classmethod
    def get_lenguajes_por_id(cls, id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM lenguajes WHERE id = %s", (id,))
        datos = cursor.fetchone()
        cursor.close()
        connection.close()

        if datos is not None:
            return Lenguaje(datos).to_json()

        raise IdInexistenteError("Lenguaje", id)

    