import csv
from app.models.perimetro import Perimetro


def readCsv():
    perimetros=[]
    with open('../Public/PuntosPerimetros.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            per = Perimetro.perimetro(row[0],row[1],str(row[2]),str(row[3]),row[4])
            perimetros.append(per)
    return perimetros


