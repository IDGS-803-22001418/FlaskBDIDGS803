from sqlalchemy import create_engine

class Config(object):
    SECRET_kEY = "clave-secreta"
    SESSION_COOKIE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQL_ALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/bdidgs803'
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False