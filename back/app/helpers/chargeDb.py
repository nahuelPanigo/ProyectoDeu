import csv
import os


def readCsv():
    perimetros=[]
    csv_path = "../app/app/Public/PuntosPerimetros.csv"
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            perimetros.append((int(row[0]),int(row[1]),str(row[2]),str(row[3]),row[4]))
    return perimetros


