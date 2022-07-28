from app.db_sqlalchemy import db_sqlalchemy as db
from datetime import date
from sqlalchemy import Column, Integer, ForeignKey


class Alerta(db.Model):
    __tablename__ = 'alerts'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    latitude = db.Column(db.String(100))
    length = db.Column(db.String(100))
    zone = db.Column(db.String(30), nullable=False)
    user_id  = Column(Integer, ForeignKey('users.id'))
