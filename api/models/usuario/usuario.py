import json
from pathlib import Path
from api.db.db_config import get_db_connection
from api.models.usuario.usuario_mapping import COLUMNA_DB
from api.utils.excepciones_modelos import IdInexistenteError, ColumnaUnicaDuplicadaError
from api.models.base import ModeloBase

SCHEMA_PATH = Path(__file__).resolve().parent.parent.parent / "schemas" / "usuario.schema.json"

with open(SCHEMA_PATH, encoding="utf-8") as f:
    USUARIO_SCHEMA = json.load(f)

class Usuario(ModeloBase):
    schema = USUARIO_SCHEMA
    _columna_db = COLUMNA_DB

    @classmethod
    def get_usuarios(cls):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios")
        datos = cursor.fetchall()
        cursor.close()
        connection.close()

        return [Usuario(dato).to_json() for dato in datos]

    @classmethod
    def get_usuario_por_id(cls, id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM usuarios WHERE id = %s", (id,))
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

        nombre_usuario = datos["nombreUsuario"]
        cursor.execute("SELECT * FROM usuarios WHERE db_nombre_usuario = %s", (nombre_usuario,))
        if cursor.fetchone() is not None:
            raise ColumnaUnicaDuplicadaError("nombre_usuario", nombre_usuario)

        email = datos["email"]
        cursor.execute("SELECT * FROM usuarios WHERE db_email = %s", (email,))
        if cursor.fetchone() is not None:
            raise ColumnaUnicaDuplicadaError("email", email)

        columnas = [cls._columna_db[campo] for campo in cls._campos]
        valores = [datos[campo] for campo in cls._campos]
        placeholders = ", ".join(["%s"] * len(valores))

        cursor.execute(
            f"INSERT INTO usuarios ({', '.join(columnas)}) VALUES ({placeholders})",
            valores
        )
        connection.commit()

        id_nuevo = cursor.lastrowid
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id_nuevo,))
        nuevo = cursor.fetchone()

        cursor.close()
        connection.close()
        return Usuario(nuevo).to_json()

    @classmethod
    def put_usuario(cls, datos, id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
        fila = cursor.fetchone()

        if fila is None:
            raise IdInexistenteError("Usuario", id)

        nombre_usuario = datos["nombreUsuario"]
        cursor.execute("SELECT * FROM usuarios WHERE db_nombre_usuario = %s AND id != %s", (nombre_usuario, id))
        fila = cursor.fetchone()

        if fila is not None:
            raise ColumnaUnicaDuplicadaError("nombre_usuario", nombre_usuario)

        email = datos["email"]
        cursor.execute("SELECT * FROM usuarios WHERE db_email = %s AND id != %s", (email, id))
        fila = cursor.fetchone()

        if fila is not None:
            raise ColumnaUnicaDuplicadaError("email", email)

        asignaciones = ", ".join(f"{cls._columna_db[campo]} = %s" for campo in cls._campos)

        # Ajuste de fecha para enviar el formato requerido en MySQL
        from datetime import timezone
        from email.utils import parsedate_to_datetime

        fecha = parsedate_to_datetime(datos['fechaCreacion'])
        fecha_db = fecha.astimezone(timezone.utc).replace(tzinfo=None)
        
        valores = [fecha_db if campo == "fechaCreacion" else datos[campo] for campo in cls._campos] + [id]

        cursor.execute(
            f"UPDATE usuarios SET {asignaciones} WHERE id = %s",
            valores
        )
        connection.commit()

        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
        actualizado = cursor.fetchone()
        cursor.close()
        connection.close()

        return Usuario(actualizado).to_json()

        