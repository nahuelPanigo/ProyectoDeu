from sqlalchemy.orm import relationship
from app.db_sqlalchemy import db_sqlalchemy as db
from datetime import datetime
from flask import jsonify


class Clima(db.Model):
    __tablename__ = 'clima'
    id = db.Column(db.Integer, primary_key=True)
    milimetrosxDia = db.Column(db.Integer)
    milimetrosxSemana= db.Column(db.Integer)
    probabilidadDePrecipitaciones = db.Column(db.Integer)
    estimacionDePrecipitaciones = db.Column(db.Integer)
    ultimaActualizacion = db.Column(db.DateTime,nullable=False)


    def getClima():
        clima = Clima.query.first()
        return Clima

    def returnValid():
        clima=getAll()
        lastTime = datetime.datetime.now()
        difference = lastTime - Clima.ultimaActualizacion  
        duration_in_s = difference.total_seconds() 
        minutes = divmod(duration_in_s, 60)[0]
        if(minutes < 5):
            return clima
        else:
            #hay que parsear con beautifoulSoup
            return clima


    def parseJson(clima):
        dict = {}
        dict ["milimetrosXDia"] = clima.milimetrosxDia
        dict ["milimetrosxSemana"] = clima.milimetrosxSemana
        dict ["probabilidadDePrecipitaciones"] = clima.probabilidadDePrecipitaciones
        dict ["estimacionDePrecipitaciones"] = clima.estimacionDePrecipitaciones
        return dict


    def getApi():
        return jsonify(clima=clima.parseJson(getClima()))