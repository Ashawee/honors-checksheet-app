# third-party imports
from flask import Flask
from 

#local imports
from config import app_config

# database variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    return(app)
    
