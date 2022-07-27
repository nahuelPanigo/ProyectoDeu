import datetime
from app.db_sqlalchemy import db_sqlalchemy as db
from app.models.config import Config
from sqlalchemy import null, or_, and_
from datetime import date
import re


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False, unique=True) 
    password = db.Column(db.String(30), nullable=False)
    active = db.Column(db.Integer)
    update_at = db.Column(db.DateTime,nullable=True)
    created_at = db.Column(db.DateTime,default=datetime.datetime.utcnow) 



    #realiza la busqueda por username
    def search(name):
        users = User.query
        users = users.filter(User.username.like('%' + name + '%'))
        users = users.order_by(User.username).all()
        return users

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
    def exist(email, username):
        errores = {}
        if(User.query.filter_by(email = email).first() is not None):
            errores["error_email"] = "El email ya existe"
        if(User.query.filter_by(username = username).first() is not None):
            errores["error_username"] = "El nombre de usuario ya existe"
        return errores
    
    #crea a un usuario y guarda los cambios en la db
    def create(username, password, email):
        user = User(password = password,email = email,username= username, active=1, update_at=date.today().strftime('%Y-%m-%d %H:%M:%S'),created_at=date.today().strftime('%Y-%m-%d %H:%M:%S'))
        db.session.add(user)
        db.session.commit()

    #valida que el email y el nombre de usuario no exista exceptuando al mismo usuario que modifica
    def validateModify(email, username , user_id):
        errores = {}
        if(User.query.filter(and_(User.email==email, User.id!=user_id)).first() is not None):
            errores["error_email"] = "El mail ya existe"
        if(User.query.filter(and_(User.username==username, User.id!=user_id)).first() is not None):
            errores["error_username"] = "El nombre de usuario ya existe"
        return errores

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
                "username":user.username,
                "active":user.active,
                "update_at":user.update_at,
                "created_at":user.created_at
            }
        return my_dict

    #valida el formulario del create
    def validateForm(form):
        errores = {}
        if Validator.email(form.get("email")) is not None:
            errores["error_email"] = Validator.email(form.get("email"))
        
        if Validator.username(form.get("username")) is not None:
            errores["error_username"] = Validator.username(form.get("username"))
        
        if Validator.password(form.get("password")) is not None:
            errores["error_password"] = Validator.password(form.get("password"))

        return errores    
min = 5
max = 30
class Validator():    
    def email(email):
        if not re.match('^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+([.]\w{2,4})+$', email):
            return "Email incorrecto"
        return None
    
    def username(username):
        if not min <= len(username) <= max:
            return "El nombre de usuario debe tener entre 5 y 30 caracteres"
        return None
    
    def password(password):
        if not 6 <= len(password) <= max:
            return "La contraseña debe tener entre 6 y 30 caracteres"
        return None
