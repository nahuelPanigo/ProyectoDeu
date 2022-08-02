import requests
import time
from os import environ

def job():
    myhost = environ.get("myhost", "localhost")
    r=""
    try:
        r = requests.get('http://'+myhost+':5000/api/worker')
    except:
        print("imptime la salida del request worker",r)


while True:
    time.sleep(10)
    job()


