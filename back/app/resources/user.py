from app.models.user import User
from flask import request, jsonify


def apiCreate():
	try:
		content=request.json
		if(content["password"] != content["repeatPassword"]):
			return jsonify(errores={"errores":"las contraseñas no son iguales"})
		errores=User.validateForm(content["email"], content["password"])
		if bool(errores):
			return jsonify(errores=errores)
		user=User.create(content["email"], content["password"])
		if (user is None):
			return jsonify(errores={"errores": "no se pudo crear el usuario intente nuevamente el usuario y/o el mail ya se encuentran en la base"})
		return jsonify(user=User.toString(user))
	except:
		return jsonify(errores={"errores": "no se pudo crear el usuario intente nuevamente el usuario y/o el mail ya se encuentran en la base"})

def apiLogin():
	try:
		content=request.json
		user=User.findByEmail(content["email"])
		if(user is not None):
			if(user.password == content["password"]):
				return jsonify(token=User.toString(user))
		return jsonify(errores={"error_login":"el usuario y/o la contraseña  son incorrectos"})
	except:	
		return jsonify(errores={"error_login":"el usuario y/o la contraseña  son incorrectos"})