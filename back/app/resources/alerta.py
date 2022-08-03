from app.models.alerta import Alerta
from app.models.user import User
from flask import request, jsonify

def apiCreate():
    try:
        content=request.json
        alerta=Alerta.create(content["name"], content["latitude"], content["longitud"],content["zona"], int(content["user"]))
        if (alerta is None):
            return jsonify(errores={"errores": "Por favor intente nuevamente"})
        return jsonify(alerta=Alerta.toString(alerta))
    except: 
        return jsonify(errores={"errores": "no se pudo crear la alerta. Por favor intente nuevamente"})

def apiGet(id):
    try:
        dict=[]
        alertas = Alerta.getAlertas(id)
        for alerta in alertas:
            dict.append(Alerta.getJsonAlert(alerta))
        return jsonify(dict)
    except:
        return jsonify(errores={"errores": "no se pudo cargar la lista de alertas configuradas. Por favor intente nuevamente"}) 

def delete(idAlerta):
    try:
        return Alerta.delete(idAlerta)
        # return jsonify("se elimino correctamente")
    except:
        return jsonify(errores={"errores": "no se pudo eliminar la alerta. Por favor intente nuevamente"})