from os import path, environ
from flask import Flask, render_template, g, request
from flask_session import Session
from app.models.perimetro import Perimetro
from config import config
from app.db_sqlalchemy import db_sqlalchemy as db
from app.resources import user
from app.resources import perimetro
from app.resources import config as configuration
from app.resources import clima
from app.resources import alerta
from flask_cors import CORS
from app.helpers.chargeDb import readCsv


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
        from app.models import alerta as alertaModel
        db.create_all()

    

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    #rutas del config
    app.add_url_rule("/api/config", "config_get_configuration", configuration.getConfiguration)
    
    #rutas de usuario login,registrarse
    app.add_url_rule("/api/user/registrarse","user_ApiCreate",user.apiCreate, methods=["POST"])
    app.add_url_rule("/api/user/login","user_ApiLogin",user.apiLogin, methods=["POST"])    

    #rutas del clima

    #rutas de alertas
    app.add_url_rule("/api/alertas/new", "alerta_ApiCreate", alerta.apiCreate, methods=["POST"])
    app.add_url_rule("/api/alertas/<id>", "alerta_ApiGet", alerta.apiGet, methods=["GET"])
    app.add_url_rule("/api/alertas/delete/<idAlerta>", "alerta_delete", alerta.delete, methods=["DELETE"] )

    #rutas de Perimetros
    app.add_url_rule("/api/zonas", "perimetro_get_zonas", perimetro.getZonas)
    app.add_url_rule("/api/zonas/<punto>", "perimetro_get_zona_punto", perimetro.getZonaPunto, methods=["GET"])
    
    return app