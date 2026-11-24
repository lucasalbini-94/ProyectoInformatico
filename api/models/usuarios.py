from api.db.db_config import get_db_connection
from pathlib import Path
import json
from jsonschema import validate, ValidationError, FormatChecker
from werkzeug.security import generate_password_hash, check_password_hash

SCHEMA_DIR = Path(__file__).resolve().parent.parent / "schemas"

with open(SCHEMA_DIR / "login.schema.json", encoding="utf-8") as f:
    LOGIN_SCHEMA = json.load(f)

with open(SCHEMA_DIR / "usuario.schema.json", encoding="utf-8") as f:
    USUARIO_SCHEMA = json.load(f)


class Usuario:
    _schema_login = LOGIN_SCHEMA
    _schema_usuario = USUARIO_SCHEMA

    @classmethod
    def validar_login(cls, datos):
        try:
            validate(instance=datos, schema=cls._schema_login, format_checker=FormatChecker())
            return True, None
        except ValidationError as error:
            return False, error.message

    @classmethod
    def validar_registro(cls, datos):
        try:
            validate(instance=datos, schema=cls._schema_usuario, format_checker=FormatChecker())
            return True, None
        except ValidationError as error:
            return False, error.message

    @classmethod
    def buscar_por_email(cls, email):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()
        cursor.close()
        connection.close()
        return usuario

    @classmethod
    def crear_usuario(cls, datos):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Verificar email duplicado
        cursor.execute("SELECT id FROM usuarios WHERE email = %s", (datos["email"],))
        if cursor.fetchone() is not None:
            cursor.close()
            connection.close()
            raise ValueError("El email ya está registrado")

        # Verificar nombre de usuario duplicado
        cursor.execute("SELECT id FROM usuarios WHERE nombre_usuario = %s", (datos["nombreUsuario"],))
        if cursor.fetchone() is not None:
            cursor.close()
            connection.close()
            raise ValueError("El nombre de usuario ya está en uso")

        # Hashear la contraseña
        password_hash = generate_password_hash(datos["password"])

        # Insertar
        cursor.execute(
            """INSERT INTO usuarios (nombre_usuario, email, nombre, apellido, password_hash)
               VALUES (%s, %s, %s, %s, %s)""",
            (datos["nombreUsuario"], datos["email"], datos["nombre"], datos["apellido"], password_hash)
        )
        connection.commit()

        id_nuevo = cursor.lastrowid
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id_nuevo,))
        usuario = cursor.fetchone()

        cursor.close()
        connection.close()
        return usuario

    @classmethod
    def verificar_password(cls, password_plano, password_hash):
        return check_password_hash(password_hash, password_plano)