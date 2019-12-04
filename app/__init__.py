from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    '''
    function to register blueprints and imports
    '''
    
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])



    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    
    # setting config
    from .request import configure_request
    configure_request(app)
    login_manager.init_app(app)

# register auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

# register main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

  
