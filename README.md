crear el network

docker network create deu-red

craer el directorio raiz con 3 carpetas: front, back, base en todos crear la carpeta data donde alojaremos los respectivos volumenes

correr la base de datos con

	Descargamos la img:
		docker pull mysql:8

	ejecutamos el container:
		docker run --name servidor_mysql --network=my-net -e MYSQL_ROOT_PASSWORD=passDeu  -e MYSQL_DATABASE=deu -e MYSQL_USER=usuarioDeu -e MYSQL_PASSWORD=passDeu -v /data:/var/lib/mysql -p 3306:3306 mysql:8

correr el backend:
	
	Descargamos la img:
		docker build --tag python-docker .

	ejecutamos el container:
		docker run --name backend --network my-net  -v back:/app -e DB_HOST=servidor_mysql -e DB_USER=usuarioDeu -e DB_PASS=passDeu -e DB_NAME=deu -p 5000:5000 python-docker

correr el front:
	para empezar de 0:
		npm install -g @vue/cli@3.7.0
		vue create app --default
	sino descargamos el codigo de git con nuestra app


	Descargamos la img:
		copiamos el Dockerfile en la carpeta front/app (la recien creada por vue)
		y ejecutamos docker build -t my-app


	ejecutamos el container:
		docker run --network=my-net -v ${PWD}:/app -v /app/node_modules -p 8080:8080 -e myhost=backend my-app:dev


