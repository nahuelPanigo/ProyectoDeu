FROM python:3-alpine

RUN pip install --upgrade pip

COPY requirements.txt ./requirements.txt
RUN pip3 install -r ./requirements.txt

COPY . .

CMD [ "python3", "worker.py"]

