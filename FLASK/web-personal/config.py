class Config:
    # Configuración base
    DEBUG = True
    TESTING = True

    # Configuración de la conexión a la Base de Datos
    # Siempre así: "mysql+pymysql://user:pass@server:port/DB"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/webpersonal_db"

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
