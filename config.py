import os

class Config:
    SECRET_KEY = 'amos'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://dan:12345@localhost/groppy'

    # UPLOADED_PHOTOS_DEST ='app/static/photos'
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # SIMPLEMDE_JS_IIFE = True
    # SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass
    

class ProdConfig(Config):
    pass

class TestConfig(Config):
    DEBUG =True 

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
} 