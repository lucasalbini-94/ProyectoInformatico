import json
from pathlib import Path
from api.db.db_config import get_db_connection
from api.models.proyectos.proyectos_mapping import COLUMNA_DB
from api.utils.excepciones_modelos import IdInexistenteError
from api.models.base import ModeloBase


SCHEMA_PATH = Path(__file__).resolve().parent.parent.parent / "schemas" / "proyecto.schema.json"

with open(SCHEMA_PATH, encoding="utf-8") as file:
    PROYECTO_SCHEMA = json.load(file)


class Proyecto(ModeloBase):
    schema = PROYECTO_SCHEMA
    _columna_db = COLUMNA_DB

    @classmethod
    def get_proyectos(cls):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proyectos")
        datos = cursor.fetchall()
        cursor.close()
        connection.close()

        return [cls(dato).to_json() for dato in datos]

    @classmethod
    def get_proyecto_por_id(cls, id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proyectos WHERE id = %s", (id,))
        proyecto = cursor.fetchone()
        cursor.close()
        connection.close()

        if proyecto is not None:
            return Proyecto(proyecto).to_json()

        raise IdInexistenteError("Proyecto", id)

    @classmethod
    def get_proyectos_por_usuario(cls, id_usuario):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        columna_usuario = cls._columna_db["idUsuario"]
        cursor.execute(
            f"SELECT * FROM proyectos WHERE {columna_usuario} = %s",
            (id_usuario,)
        )

        filas = cursor.fetchall()
        cursor.close()
        connection.close()
        
        return [cls(fila).to_json() for fila in filas]

    @classmethod
    def post_proyecto(cls, datos):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        campos = [campo for campo in cls._campos if campo in datos]
        columnas = [cls._columna_db[campo] for campo in campos]
        valores = [datos[campo] for campo in campos]
        placeholders = ", ".join(["%s"] * len(valores))

        cursor.execute(
            f"INSERT INTO proyectos ({', '.join(columnas)}) VALUES ({placeholders})",
            valores
        )
        connection.commit()

        id_nuevo = cursor.lastrowid
        cursor.execute("SELECT * FROM proyectos WHERE id = %s", (id_nuevo,))
        nuevo = cursor.fetchone()

        cursor.close()
        connection.close()
        return Proyecto(nuevo).to_json()

    @classmethod
    def put_proyecto(cls, id, datos):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        campos = [campo for campo in cls._campos if campo in datos]
        asignaciones = ', '.join(f"{cls._columna_db[campo]} = %s" for campo in campos)
        valores = [datos[campo] for campo in campos] + [id]

        cursor.execute(
            f"UPDATE proyectos SET {asignaciones} WHERE id = %s",
            valores
        )
        connection.commit()

        cursor.execute("SELECT * FROM proyectos WHERE id = %s", (id,))
        actualizado = cursor.fetchone()
        cursor.close()
        connection.close()

        return Proyecto(actualizado).to_json()

    @classmethod
    def delete_proyectos(cls, id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM proyectos WHERE id = %s", (id,))
        eliminado = cursor.fetchone()

        if eliminado is None:
            cursor.close()
            connection.close()
            raise IdInexistenteError("Proyecto", id)

        cursor.execute("DELETE FROM proyectos WHERE id = %s", (id,))
        connection.commit()

        cursor.close()
        connection.close()
        return Proyecto(eliminado).to_json()