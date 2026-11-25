from api.db.db_config import get_db_connection
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import json

API_EXTERNA = "https://carlosdevuni.pythonanywhere.com/api/v1"

def obtener_json(recurso):
    url = f"{API_EXTERNA}/{recurso}"
    request = Request(url, headers={
        "content-type": "application/json",
        "Grupo-Access-Key": "grupo21-TALM-ab38b6c8"
        })

    # verificar si la respuesta es correcta
    try:
        with urlopen(request, timeout=15) as response:
           return json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        raise Exception(f"Error HTTP {error.code} al consultar {recurso}: error.reason")
    except URLError as error:
        raise Exception(f"Error de red al consultar {recurso}: {error.reason}")

def sincronizar():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    try:
        # Verificar si existe al menos un registro
        cursor.execute("SELECT * FROM sincronizacion_api LIMIT 1")
        fila = cursor.fetchone()

        if fila is None:
            cargar_lenguajes(cursor)
            cargar_tecnologias(cursor)

            # Registrar que la sincronizacion se completó
            cursor.execute("INSERT INTO sincronizacion_api (fecha_sincronizacion) VALUES (NOW())")
            connection.commit()
        else:
            # Lógica para verificación de fecha
            pass

    except Exception as error:
        # Si falla la API o algún INSERT, deshace todo para no dejar datos inconsistentes
        connection.rollback()
        raise error

    finally:
        cursor.close()
        connection.close()
    

def cargar_lenguajes(cursor):
    datos = obtener_json("lenguajes")

    if not datos:
        return

    valores = [(item["id"], item["nombre"]) for item in datos]
    cursor.executemany("INSERT INTO lenguajes (id, nombre) VALUES (%s, %s)", valores)

def cargar_tecnologias(cursor):
    datos = obtener_json("tecnologias")

    if not datos:
        return

    valores = [(item["id"], item["nombre"], item["categoria"]) for item in datos]
    cursor.executemany("INSERT INTO tecnologias (id, nombre, categoria) VALUES (%s, %s, %s)", valores)