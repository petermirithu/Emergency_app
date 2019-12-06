import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
        
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # SIMPLEMDE_JS_IIFE = True
    # SIMPLEMDE_USE_CDN = True
      
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    CAT_API_URL='https://newsapi.org/v2/everything?q=kenya&apiKey={}'
        
class ProdConfig(Config):    
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://pyra:lotus@localhost/e_may'

class TestConfig(Config):
    DEBUG =True 
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://pyra:lotus@localhost/e_may_test'

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
} 