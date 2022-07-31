from app.models.perimetro import Perimetro


def getZonas():
	return Perimetro.getJsonPorZonas()


def getZonaPunto(punto):
	col=punto.split(",")
	return Perimetro.checkZone(float(col[0]),float(col[1]))