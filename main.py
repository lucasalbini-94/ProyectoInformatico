from api import app
from api.services.sincronizacion_api import sincronizar


# Inicio de la aplicación
if __name__ == "__main__":
    app.run(debug=True, port=5000)
    sincronizar()