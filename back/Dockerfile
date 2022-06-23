FROM ledgerhq/python-flask:lam-3.9-slim-buster

RUN pip install --upgrade pip

COPY requirements.txt app/requirements.txt
RUN pip3 install -r app/requirements.txt

WORKDIR /app

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]