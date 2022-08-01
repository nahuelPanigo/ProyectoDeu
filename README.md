crear el network

docker network create  my-net

craer el directorio raiz con 3 carpetas: front, back, base en todos crear la carpeta data donde alojaremos los respectivos volumenes

correr la base de datos con

	Descargamos la img:
		docker pull mysql:8

	ejecutamos el container:
		docker run --name servidor_mysql --network=my-net -e MYSQL_ROOT_PASSWORD=passDeu  -e MYSQL_DATABASE=deu -e MYSQL_USER=usuarioDeu -e MYSQL_PASSWORD=passDeu -v /data:/var/lib/mysql -p 3306:3306 mysql:8

correr el backend:
	
	Descargamos la img:
		docker build --tag python-docker:dev .

	ejecutamos el container:
		docker run --name backend --network my-net  -v ${PWD}:/app -e DB_HOST=servidor_mysql -e DB_USER=usuarioDeu -e DB_PASS=passDeu -e DB_NAME=deu -p 5000:5000 python-docker:dev 

correr el front:

	Descargamos la img:
		nos movemos a la carpeta front
		y ejecutamos docker build -t my-app:dev .


	ejecutamos el container:
		docker run --network=my-net -v ${PWD}:/app -v /app/node_modules -p 8080:8080 -e myhost=backend my-app:dev




URL para los mapas:
http://omlp.sedici.unlp.edu.ar/dataset/informe-final
http://omlp.sedici.unlp.edu.ar/dataset/informe-final/resource/178e69b1-8d50-4250-88a7-203ff0326930?inner_span=True
https://www.memoria.fahce.unlp.edu.ar/trab_eventos/ev.11310/ev.11310.pdf

PARA CARGAR LOS PUNTOS:
https://www.keene.edu/campus/maps/tool/

webscrapp:
https://meteo.fcaglp.unlp.edu.ar/

apiClima:
weatherbit.io/account/dashboard
https://weatherstack.com/quickstart