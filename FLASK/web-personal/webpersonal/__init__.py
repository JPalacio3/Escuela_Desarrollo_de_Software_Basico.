from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Configuración de la aplicación
app.config.from_object('config.DevelopmentConfig')

# Base de datos
db = SQLAlchemy(app)

# Cargar las vistas
from webpersonal.views import base  # noqa
from webpersonal.project.views import project  # noqa

# Registrar el Blueprint
app.register_blueprint(base)
app.register_blueprint(project)
# IMPORTANTE RECORDAR QUE LA LÍNEA# import webpersonal.views #SE ENCUENTRE DEBAJO DE app = Flask(__name__) usando  "# noqa" al final de las líneas que no queremos que se reacomoden al guardar los cambios
# import webpersonal.views  # noqa

# Ejecutar todas las consultas
with app.app_context():
    db.create_all()

# Este orden siempre se tiene que respetar para evitar confictos con las beses de datos
