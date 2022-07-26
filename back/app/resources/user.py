from app.models.user import User
from flask import jsonify
from flask import redirect, request, url_for, session, abort


def apiCreate():
	content=request.json
	if(content["password"] != content["repeatPassword"]):
		return jsonify(errores={"error_password":"las contraseñas no son iguales"})
	errores=User.validateForm(content["username"],content["email"], content["password"])
	if(not errores):
		return jsonify(errores=errores)
	user=User.create(content["username"],content["email"], content["password"])
	if  (user is None):
		return ({"errores": "no se pudo crear el usuario intente nuevamente el usuario y/o el mail ya se encuentran en la base"})
	return jsonify(user=User.toString(user))


def apiLogin():
	content=request.json
	user=User.findByEmail(content["email"])
	if(user is None)|(user.password != content["password"]):
		return jsonify(errores={"error_login":"el usuario y/o la contraseña  son incorrectos"})
	return jsonify(token=User.toString(user))