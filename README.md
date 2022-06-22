crear el network

docker network create deu-red

craer el directorio raiz con 3 carpetas: front, back, base en todos crear la carpeta data donde alojaremos los respectivos volumenes

correr la base de datos con

	Descargamos la img:
		docker pull mysql:8

	ejecutamos el container:
		docker run --name some-mysql --network=my-net -e MYSQL_ROOT_PASSWORD=passDeu  MYSQL_DATABASE=deu MYSQL_USER=usuarioDeu MYSQL_PASS=passDeu -v /home/nahue/Documents/DEU/ProyectoFinal/base/data:/var/lib/mysql/data/ mysql:8

correr el backend:
	
	Descargamos la img:
		docker pull mysql:8


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


