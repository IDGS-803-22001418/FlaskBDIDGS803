class Config(object):
    SECRET_kEY = "clave-secreta"
    SESSION_COOKIE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/bdidgs803'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
