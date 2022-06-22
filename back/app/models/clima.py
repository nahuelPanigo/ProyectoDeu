from sqlalchemy.orm import relationship
from app.db_sqlalchemy import db_sqlalchemy as db

class Clima(db.Model):
    __tablename__ = 'clima'
    id = db.Column(db.Integer, primary_key=True)
    milimetrosxDia = db.Column(db.Integer)
    milimetrosxSemana= db.Column(db.Integer)
    probabilidadDePrecipitaciones = db.Column(db.Integer)
    EstimacionDePrecipitaciones = db.Column(db.Integer)
    ultimaActualizacion = db.Column(db.DateTime,nullable=False)



    def findByName(name):
        rol = Rol.query.filter_by(name = name).first()
        return rol    
    
    def getAll():
        roles = Rol.query.all()
        return roles
