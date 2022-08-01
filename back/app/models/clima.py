from urllib import request
from sqlalchemy.orm import relationship
from app.db_sqlalchemy import db_sqlalchemy as db
from datetime import datetime
from flask import jsonify
from bs4 import BeautifulSoup
import requests




class Clima(db.Model):
    __tablename__ = 'clima'
    id = db.Column(db.Integer, primary_key=True)
    milimetrosxDia = db.Column(db.Integer)
    milimetrosxSemana= db.Column(db.Integer)
    probabilidadDePrecipitaciones = db.Column(db.Integer)
    proximasAlertas = db.Column(db.String(60))
    ultimaActualizacionHora = db.Column(db.DateTime,nullable=False)
    ultimaActualizacionSemana = db.Column(db.DateTime,nullable=False)


    def getClima():
        return Clima.query.first()
        

    def updateClima(milimetroDia,ProbabilidadPrex,Alertas):
        clima=Clima.getClima()
        clima.milimetrosxSemana = Clima.milimetrosxSemana-Clima.milimetrosxDia+milimetroDia
        clima.milimetrosxDia = milimetroDia
        clima.probabilidadDePrecipitaciones = ProbabilidadPrex
        clima.proximasAlertas = Alertas
        clima.ultimaActualizacionHora = datetime.datetime.now()
        db.session.commit()

    def updateClima(milimetroDia):
        clima=Clima.getClima()
        clima.milimetrosxSemana = Clima.milimetrosxSemana-Clima.milimetrosxDia+milimetroDia
        clima.milimetrosxDia = milimetroDia
        db.session.commit()


    def updateClima(milimetroDia,MilimetroSemana,ProbabilidadPrex,Alertas):
        clima=Clima.getClima()
        clima.milimetrosxDia = milimetroDia
        clima.milimetrosxSemana = MilimetroSemana
        clima.probabilidadDePrecipitaciones = ProbabilidadPrex
        clima.proximasAlertas = Alertas
        clima.ultimaActualizacionHora = datetime.datetime.now()
        clima.ultimaActualizacionSemana = datetime.datetime.now()
        db.session.commit()



    def tipoActualizacion():
        clima=Clima.getClima()
        lastTime = datetime.datetime.now()
        difference = lastTime - clima.ultimaActualizacionSemana 
        if difference.days >7 :
            return 0
        difference = lastTime - clima.ultimaActualizacionHora 
        duration_in_s = difference.total_seconds()
        if divmod(duration_in_s, 3600)[0] > 1:
            return 1
        return 2
       


    def parseJson(clima):
        dict = {}
        dict ["milimetrosXDia"] = clima.milimetrosxDia
        dict ["milimetrosxSemana"] = clima.milimetrosxSemana
        dict ["probabilidadDePrecipitaciones"] = clima.probabilidadDePrecipitaciones
        dict ["proximasAlertas"] = clima.proximasAlertas
        return dict


    def getApi():
        return jsonify(clima=Clima.parseJson(Clima.getClima()))

    
    def updateInfoClima():
        option=Clima.tipoActualizacion()
        DatosDiarios=int(float(Clima.getPrecipitacionesAcumuladasDiarias()))
        if(option==2):
            Clima.updateClima(DatosDiarios)
        else:
            Probabilidad,alertas = Clima.getProbabilitiesAndAlerts()
            if(option==0):
                Clima.updateClima(DatosDiarios,0,Probabilidad,alertas)
            else:
                Clima.updateClima(DatosDiarios,Probabilidad,alertas)


    def getPrecipitacionesAcumuladasDiarias():
        html_doc = requests.get('https://meteo.fcaglp.unlp.edu.ar/davis/campo/campo.htm',headers={"User-Agent":"Mozilla/5.0"}).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        tags=soup.find_all("div", class_="tabla")[5].find_all("td")
        return tags[1].text.split("\xa0")


    def getProbabilitiesAndAlerts():
        access_key='a5d40d5a79e74e4798619c943b2df6a2'
        params = {
        'key': access_key,
        'city': 'Buenos Aires',
        }
        html_doc_Probability_Daily = requests.get('https://api.weatherbit.io/v2.0/forecast/daily',params)
        html_doc_Probability_Alerts = requests.get(' https://api.weatherbit.io/v2.0/alerts',params)
        data="no hay alertas"
        jsonAlerts= html_doc_Probability_Alerts.json()
        if(len(jsonAlerts["alerts"])>0):
            if("title" in jsonAlerts["alerts"][0]):
                data=jsonAlerts["alerts"][0]["title"]
        return html_doc_Probability_Daily.json()["data"][0]["pop"], data