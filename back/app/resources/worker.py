from app.helpers.sendEmail import enviarMail 
from app.models.clima import Clima

def actualizarClima():
    Clima.updateInfoClima()
    enviarMail()
    return "ok"