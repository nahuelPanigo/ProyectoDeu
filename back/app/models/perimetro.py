from sqlalchemy.orm import relationship
from app.db_sqlalchemy import db_sqlalchemy as db

class Perimetro(db.Model):
    __tablename__ = 'perimetro'
    id = db.Column(db.Integer, primary_key=True)
    nroPunto = db.Column(db.Integer)
    ordenPunto= db.Column(db.Integer)
    latitud = db.Column(db.Integer)
    longitud = db.Column(db.Integer)


 
    
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
        return perimetros
