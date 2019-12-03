from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # ....

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    
    