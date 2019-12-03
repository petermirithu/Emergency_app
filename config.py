import os

class Config:
    '''
    General configuration parent class
    '''
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
  
    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    CAT_API_URL='https://newsapi.org/v2/top-headlines?country=kenya&category={}&apiKey={}'

    @staticmethod
    def init_app(app):
        pass

    # @staticmethod
    # def init_app(app):
    #     pass
    

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://pyra:lotus@localhost/e_may'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://pyra:lotus@localhost/e_may_test'
    DEBUG =True 

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
} 