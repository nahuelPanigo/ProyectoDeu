import datetime
from app.db_sqlalchemy import db_sqlalchemy as db
from sqlalchemy.orm import relationship
from app.models.config import Config
from datetime import date
import re
from app.models.alerta import Alerta


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    active = db.Column(db.Integer)
    alerta = relationship("Alerta")
    update_at = db.Column(db.DateTime,nullable=True)
    created_at = db.Column(db.DateTime,default=datetime.datetime.utcnow) 

    #busca un usuario por email
    def findByEmail(email):
        try:
            return User.query.filter_by(email = email).first()
        except:
            return None


    #busca un usuario por id
    def findById(user_id):
        return User.query.filter_by(id=user_id).first()

    #Este metodo retorna erroes en caso de que exista el email y/o el nombre de usuario
    def exist(email):
        errores = {}
        if(User.query.filter_by(email = email).first() is not None):
            errores["error_email"] = "El email ya existe"
        return errores
    
    #crea a un usuario y guarda los cambios en la db
    def create(email, password):
        try:
            user = User(password = password,email = email, active=1, update_at=date.today().strftime('%Y-%m-%d %H:%M:%S'),created_at=date.today().strftime('%Y-%m-%d %H:%M:%S'))
            db.session.add(user)
            db.session.commit()
            return user
        except:
            return None

    #pone al usuario en un diccionario para despues pasarlo a json
    def tostringUsers(users):
        newUsers=[]
        for user in users:
            newUsers.append(toString(user))
        return  newUsers

    def toString(user):
        my_dict = {
                "id":user.id,
                "email":user.email,
                "active":user.active,
                "update_at":user.update_at,
                "created_at":user.created_at
            }
        return my_dict

    #valida el formulario del create
    def validateForm(email, password):
        errores = {}
        if Validator.email(email) is not None:
            errores["errores"] = Validator.email(email)        
        if Validator.password(password) is not None:
            errores["errores"] = Validator.password(password)
        return errores    
min = 5
max = 30
class Validator():    
    def email(email):
        if not re.match('^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+([.]\w{2,4})+$', email):
            return "Email incorrecto"
        return None
    
    def password(password):
        if not 6 <= len(password) <= max:
            return "La contraseña debe tener entre 6 y 30 caracteres"
        return None
