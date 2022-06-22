from os import path, environ
from flask import Flask, render_template, g, request
from flask_session import Session
from config import config
from app.db_sqlalchemy import db_sqlalchemy as db


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

		db.create_all()

	return app