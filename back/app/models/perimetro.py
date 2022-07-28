from sqlalchemy.orm import relationship
from app.db_sqlalchemy import db_sqlalchemy as db
import json


class Perimetro(db.Model):
    __tablename__ = 'perimetro'
    id = db.Column(db.Integer, primary_key=True)
    nroPunto = db.Column(db.Integer)
    ordenPunto= db.Column(db.Integer)
    latitud = db.Column(db.Integer)
    longitud = db.Column(db.Integer)
    zona =db.Column(db.string(30))

 
    
    def getAll():
        perimetros = Perimetro.query.order_by(Perimetro.nroPunto.desc(),Perimetro.nroPunto.desc()).all()
        perimetrosCol= []
        ordenAct = perimetros[0].nroPunto;
        puntos = []
        for per in perimetros:
            if(per.ordenPunto != ordenAct):
                ordenAct=per.ordenPunto
                perimetrosCol.append(puntos)
                puntos.clear()            
            puntos.append(per)
        return puntos
        
    
    def getPorZonas():
        dictZonas ={}
        dictZonas["baja"] = []
        dictZonas["alta"] = []
        dictZonas["media"] = []
        dictZonas["muyAlta"] = []
        perimetros= Perimetro.getAll()
        perActual=perimetros[0].nroPunto
        puntos =[]
        zona = perimetros[0].zona
        for per in perimetros:
            if(per.ordenPunto != perActual):
                perActual=per.ordenPunto
                dictZonas[zona].append(puntos)
                puntos.clear()
                zona = per.zona            
            puntos.append(per)
        return dictZonas

    
    def getJsonPorZonas():
        json.dump(Perimetro.getJsonPorZonas())