from app.models.perimetro import Perimetro


def getZonas():
	return Perimetro.getJsonPorZonas()