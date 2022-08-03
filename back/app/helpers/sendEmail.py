from app.models.alerta import Alerta
from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

#configuration mail
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'alertainundaciones.laplata@gmail.com',
    "MAIL_PASSWORD": 'mhbqtbguqgduzrhi'
}
def enviarMail():
    usuarios = Alerta.enviarAlertas()
    if(usuarios):
        app.config.update(mail_settings)
        mail = Mail(app)
        for usuario in usuarios:
            with app.app_context():
                msg = Message(subject="Notificacion de Alerta",
                    sender="alertainundaciones.laplata@gmail.com",
                    recipients=[usuario[0]],
                    body="Alerta por fuertes lluvias en " + usuario[2] +". Riesgo de la zona: " +usuario[1])
                mail.send(msg)