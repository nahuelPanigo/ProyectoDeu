from os import path, environ
from flask import Flask, render_template, g, request
from flask_session import Session
from config import config
from app.db_sqlalchemy import db_sqlalchemy as db
from app.resources import user
from app.resources import perimetro
from app.resources import config as configuration
from app.resources import clima
from flask_cors import CORS


def create_app(environment="development"):
    app = Flask(__name__)

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])


    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    db.init_app(app)

    conf = app.config
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"+conf["DB_USER"]+":"+conf["DB_PASS"]+"@"+conf["DB_HOST"]+"/"+conf["DB_NAME"]
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

    with app.app_context():
        #importamos los modelos y ejecutamos el create all
        from app.models import config as configModel
        from app.models import user as userModel
        from app.models import perimetro as perimetroModel
        from app.models import clima as climaModel

        db.create_all()


    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    #rutas del config
    app.add_url_rule("/api/config", "config_get_configuration", configuration.getConfiguration)
    
    #rutas de usuario login,registrarse
    app.add_url_rule("/api/user/registrarse","user_ApiCreate",user.apiCreate, methods=["POST"])
    app.add_url_rule("/api/user/login","user_ApiLogin",user.apiLogin, methods=["POST"])    

    #rutas del clima

    return app