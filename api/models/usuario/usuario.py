import json
from pathlib import Path
from api.db.db_config import get_db_connection
from api.models.usuario.usuario_mapping import COLUMNA_DB
from api.utils.excepciones_modelos import IdInexistenteError, ColumnaUnicaDuplicadaError, ColumnaNulaError
from api.models.base import ModeloBase

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schemas" / "usuario_schema.json"

with open(SCHEMA_PATH, encoding="utf-8") as f:
    USUARIO_SCHEMA = json.load(f)

class Usuario(ModeloBase):
    schema = USUARIO_SCHEMA
    _columna_db = COLUMNA_DB

    @classmethod
    def get_usuario_por_id(cls, id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM usuario WHERE id = %s", (id,))
        datos = cursor.fetchone()
        cursor.close()
        connection.close()

        if datos is not None:
            return Usuario(datos).to_json()

        raise IdInexistenteError("Usuario", id)

    @classmethod
    def post_usuario(cls, datos):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        nombre_usuario = datos["nombre_usuario"]
        cursor.execute("SELECT * FROM usuario WHERE db_nombre_usuario = %s", (nombre_usuario,))
        if cursor.fetchone() is not None:
            raise ColumnaUnicaDuplicadaError("nombre_usuario", nombre_usuario)

        email = datos["email"]
        cursor.execute("SELECT * FROM usuario WHERE db_email = %s", (email,))
        if cursor.fetchone() is not None:
            raise ColumnaUnicaDuplicadaError("email", email)

        columnas = [cls._columna_db[campo] for campo in cls._campos]
        valores = [datos[campo] for campo in cls._campos]
        placeholders = ", ".join(["%s"] * len(valores))

        cursor.execute(
            f"INSERT INTO usuario ({', '.join(columnas)}) VALUES ({placeholders})",
            valores
        )
        connection.commit()

        id_nuevo = cursor.lastrowid
        cursor.execute("SELECT * FROM usuario WHERE id = %s", (id_nuevo,))
        nuevo = cursor.fetchone()

        cursor.close()
        connection.close()
        return Usuario(nuevo).to_json()

    