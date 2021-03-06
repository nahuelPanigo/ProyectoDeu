from app.db_sqlalchemy import db_sqlalchemy as db
from flask import session
from flask import jsonify

class Config(db.Model):
    __tablename__ = 'configurations'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    contact = db.Column(db.String(30), nullable=False)
    state = db.Column(db.Integer, nullable=False)

    

    # El setattr setea el valor de un campo de una instancia.
	# setattr (objeto, campo, valor)
    def modify(form):
        data = Config.query.first()
        for campo in form: 
            if(form.get(campo) is not None):
                setattr(data,campo,form.get(campo))
                setattr(session["informationPage"],campo,form.get(campo))
        db.session.commit()

    def parseJson(config):
        dict = {}
        dict ["title"] = config.title
        dict ["description"] = config.description
        dict ["contact"] = config.contact
        dict ["state"] = config.state
        return dict


    def getApi():
        return jsonify(config=Config.parseJson(Config.query.first()))
         

    def getConfiguration():
        data = Config.query.first()
        return data

    def getState():
        return Config.query.first().state

