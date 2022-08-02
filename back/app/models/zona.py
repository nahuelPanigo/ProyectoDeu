from re import M
from app.db_sqlalchemy import db_sqlalchemy as db
from app.models.clima import Clima
import datetime
from datetime import date, timedelta
from sqlalchemy import event


class Zona(db.Model):
    __tablename__ = 'zonas'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    send_email_at = db.Column(db.DateTime,nullable=True)

    def create(name):
        try:
            yesterday = date.today()-timedelta(days=1)
            zona = Zona(name=name, send_email_at=datetime.datetime.strftime(yesterday,'%Y-%m-%d %H:%M:%S'))
            db.session.add(zona)
            return zona
        except:
            return None

    def chequeoEnviarMail(namezona):
        zona = Zona.query.filter_by(name=namezona).first()
        lastTime = datetime.datetime.now()
        difference = lastTime - zona.send_email_at 
        duration_in_s = difference.total_seconds()
        return divmod(duration_in_s, 3600)[0] > 1        


    def zonasCriticas():
        clima = Clima.getClima()
        # milimetros = clima.milimetrosxDia
        # print('milimetros x dia: ', milimetros)
        milimetros = 130
        rangos=[100, 120, 140, 160, 180]
        zonasCriticas = []
        if (milimetros >= rangos[0]):
            if (Zona.chequeoEnviarMail("muyAlta")):
                zonasCriticas.append("muyAlta")
            if (milimetros >= rangos[1]):
                if (Zona.chequeoEnviarMail("alta")):
                    zonasCriticas.append("alta")
                if (milimetros >= rangos[2]):
                    if (Zona.chequeoEnviarMail("media")):
                        zonasCriticas.append("media")
                    if (milimetros >= rangos[3]):
                        if (Zona.chequeoEnviarMail("baja")):
                            zonasCriticas.append("baja")
                        if (milimetros >= rangos[4]):
                            if (Zona.chequeoEnviarMail("zona-no-determinada-peligrosa")):
                                zonasCriticas.append("zona-no-determinada-peligrosa")
        return zonasCriticas
    
@event.listens_for(Zona.__table__, 'after_create')
def create_zonas(*args, **kwargs):
    Zona.create("muyAlta")
    Zona.create("alta")
    Zona.create("media")
    Zona.create("baja")
    Zona.create("zona-no-determinada-peligrosa")
    db.session.commit()