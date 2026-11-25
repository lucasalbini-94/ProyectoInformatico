from api.db.db_config import get_db_connection
from urllib.request import Request, urlopen
import json

API_EXTERNA = "https://carlosdevuni.pythonanywhere.com/api/v1"

def obtener_json(recurso):
    url = f"{API_EXTERNA}/{recurso}"
    request = Request(url, headers={"content-type": "application-json", "Grupo-Access-Key": "grupo21-TALM-ab38b6c8"})

    # verificar si la respuesta es correcta
    with urlopen(request, timeout=15) as response:
        if response.status != 200:
            raise Exception(
                f"La API respondió con código HTTP {response.status}"
            )

        return json.loads(response.read().decode("utf-8"))

def sincronizar():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sincronizacion_api")
    fila = cursor.fetchall()
    cursor.close()
    connection.close()
    
    if len(fila) == 0:
        cargar_lenguajes()
        cargar_tecnologias()
    else:
        # Lógica de verificación de fecha
        pass

def cargar_lenguajes():
    datos = obtener_json("lenguajes")

    return datos

def cargar_tecnologias():
    datos = obtener_json("tecnologias")

    return datos