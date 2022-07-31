import imp
from venv import create
from sqlalchemy.orm import relationship
from app.db_sqlalchemy import db_sqlalchemy as db
import json
from sqlalchemy import event, null
from app.helpers.chargeDb import readCsv
from sqlalchemy import text



class Perimetro(db.Model):
    __tablename__ = 'perimetro'
    id = db.Column(db.Integer, primary_key=True)
    nroPunto = db.Column(db.Integer)
    ordenPunto= db.Column(db.Integer)
    latitud = db.Column(db.String(30))
    longitud = db.Column(db.String(30))
    zona =db.Column(db.String(30))

    def getAll():
        sql = text('select * from perimetro order by nroPunto, ordenPunto')
        perimetros = db.engine.execute(sql)
        perimetrosCol= []
        ordenAct=1
        for key in perimetros:
            ordenAct = key[1]
            break
        puntos = []
        print("segunda key",ordenAct)
        for per in perimetros:
            print(per[1])
            if(per[1] != ordenAct):
                ordenAct=per[1]
                perimetrosCol.append(puntos)
                puntos.clear()            
            puntos.append(Perimetro.perimetro(per[1],per[2],per[3],per[4],per[5]))
        return perimetrosCol
        
    
    def getPorZonas():
        dictZonas ={}
        dictZonas["baja"] = []
        dictZonas["alta"] = []
        dictZonas["media"] = []
        dictZonas["muyAlta"] = []
        perimetros= Perimetro.getAll()
        for each in perimetros:
            puntos =[]
            zona = each[0].zona
            for per in each:
                puntos.append(Perimetro.toString(per)) 
            dictZonas[zona].append(puntos)        
        return dictZonas

    
    def getJsonPorZonas():
        dict =Perimetro.getPorZonas()
        print(dict)
        return json.dumps(dict)

    def createAll(per):
        try:
            db.session.add(Perimetro(nroPunto=per.nroPunto,ordenPunto=per.ordenPunto,latitud=per.latitud,longitud=per.longitud,zona=per.zona))
            return per
        except:
            return None



    def checkDbEmpty():
        return len(Perimetro.query.all()) == 0 

    def chargeDb():
        perimetros= readCsv()
        for per in perimetros:
            Perimetro.createAll(Perimetro.perimetro(per[0],per[1],per[2],per[3],per[4]))
        db.session.commit()

    def perimetro(punto,orden,lat,long,zona):
        p= Perimetro
        p.latitud=lat
        p.longitud=long
        p.zona=zona
        p.nroPunto=punto
        p.ordenPunto=orden
        return p

    def toString(per):
        return (per.latitud,per.longitud)


@event.listens_for(Perimetro.__table__, 'after_create')
def create_departments(*args, **kwargs):
    Perimetro.chargeDb()