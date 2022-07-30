from app.models.alerta import Alerta
from flask import request, jsonify

def apiCreate():
    try:
        content=request.json
        alerta=Alerta.create(content["name"], content["latitude"], content["longitud"], "media", int(content["user"]))
        if (alerta is None):
            return jsonify(errores={"errores": "Por favor intente nuevamente"})
        return jsonify(alerta=Alerta.toString(alerta))
    except: 
        return jsonify(errores={"errores": "no se pudo crear la alerta. Por favor intente nuevamente"})

def apiGet(user):
    try:
        dict={}
        alertas = user.getAlarmas(user)
        for alerta in alertas:
            dict.push(Alerta.getJsonAlerta(alerta))
    except:
        return jsonify(errores={"errores": "no se pudo cargar la lista de alertas configuradas. Por favor intente nuevamente"}) 