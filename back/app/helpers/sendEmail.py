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
    # "MAIL_USERNAME": os.environ['EMAIL_USER'],
    # "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
    "MAIL_USERNAME": 'alertainundaciones.laplata@gmail.com',
    "MAIL_PASSWORD": 'mhbqtbguqgduzrhi'
}
def enviarMail(alertas):
    app.config.update(mail_settings)
    mail = Mail(app)
    for alerta in alertas:
        with app.app_context():
            msg = Message(subject="Notificacion de Alerta",
                sender="alertainundaciones.laplata@gmail.com",
                recipients=[alerta.user_email], # replace with your email for testing
                body="Alerta por fuertes lluvias en `{alerta.name}`. Riesgo de la zona: `{alerta.zona}`")
            mail.send(msg)