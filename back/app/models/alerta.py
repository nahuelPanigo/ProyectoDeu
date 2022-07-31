from app.db_sqlalchemy import db_sqlalchemy as db
from sqlalchemy import Column, Integer, ForeignKey
from flask import redirect, url_for, flash


class Alerta(db.Model):
    __tablename__ = 'alerts'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    latitude = db.Column(db.String(100))
    length = db.Column(db.String(100))
    zone = db.Column(db.String(30), nullable=False)
    user_id  = Column(Integer, ForeignKey('users.id'))

    def create(nombre, latitud, long, zone, user):
        try:
            alerta = Alerta(name=nombre, latitude=latitud, length=long, zone=zone, user_id=user )
            db.session.add(alerta)
            db.session.commit()
            return alerta
        except:
            return None

    def toString(alerta):
        my_dict = {
            "id":alerta.id,
            "name":alerta.name,
            "latitud":alerta.latitud,
            "longitud":alerta.length,
            "zona":alerta.zone,
            "user":alerta.user_id
        }
        return my_dict

    #busca las alertas del usuario
    def getAlertas(user):
        try:
            return db.session.query(Alerta).filter(Alerta.user_id == user).all()
        except:
            return None

    def getJsonAlert(alerta):
        dict={}
        dict["name"]=alerta.name
        dict["latitude"]=alerta.latitude
        dict["length"]=alerta.length
        dict["id"]=alerta.id
        return dict

    def delete(id):
        try:
            alerta = Alerta.query.filter_by(id=id).first()
            db.session.delete(alerta)
            db.session.commit()
            return "ok"
        except: 
            return None