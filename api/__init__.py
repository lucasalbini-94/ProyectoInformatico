from flask import Flask
from flask import jsonify
from api.manejadores import registrar_manejadores

# Crear una instancia de Flask
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def test():
    return jsonify({'mensaje': 'Conectado a la API'})

registrar_manejadores(app)

import api.routes.usuario
import api.routes.lenguajes
import api.routes.tecnologias
import api.routes.proyectos