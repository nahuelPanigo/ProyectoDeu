from venv import create
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
    zona =db.Column(db.String(30))

    def perimetro(punto,orden,lat,long,zona):
        p= Perimetro
        p.latitud=lat
        p.longitud=long
        p.zona=zona
        p.nroPunto=punto
        p.ordenPunto=orden
        return p

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

    def create(per):
        try:
            db.session.add(per)
            db.session.commit()
            return per
        except:
            return None

    def checkDbEmpty():
        return len(Perimetro.query.all()) == 0 

    def chargeDb(perimetros):
        for per in perimetros:
            ok=Perimetro.create(per)
        return ok