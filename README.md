Ejecutar la aplicacion:

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
y ejecutamos 
				docker build -t my-app:dev .


ejecutamos el container:
				docker run --network=my-net -v ${PWD}:/app -v /app/node_modules -p 8080:8080 -e myhost=backend my-app:dev

correr worker:

Descargamos la imagen :
nos movemos a la carpeta worker
ejecutamos : 
				docker build -t worker:dev .

ejecutamos el container: 
				docker run --network=my-net -e myhost=backend  worker:dev 



 Configuraciones extas:
  en el archivo sendEmail.py ubicado en back/app/helpers se encuentra la configuracion para la cuenta de mail a configurar.
  dentro del archivo esta el diccionario mail_settings  al cual se le tienen que configurar las entradas MAIL_USERNAME y MAIL_PASSWORD con las respectivas a utilizar en el proyecto(cabe aclarar que mail_password no es la contrasena en si de la cuenta sino una generada desde la cuenta de google para poder enviar por la aplicacion) se puede realizar siguiendo los pasos como mejor opcion habilitar el MFA https://support.google.com/a/answer/6260879?hl=en#zippy=%2Cif-you-allow-sign-ins-from-less-secure-apps%2Cuse-alternatives-to-less-secure-apps

  
  Por otro lado se tiene que configurar la api_key de la api del clima, la cual se encuentra en el archivo back/app/models/clima.py y el metodo getProbabilitiesAndAlerts se debe modificar la variable: access_key para esta variable se debe hacer una en la app https://weatherstack.com/quickstart solo se necesita registrarse y es de uso gratuito.



Otra info relevante del proyecto:


URL para los mapas:
http://omlp.sedici.unlp.edu.ar/dataset/informe-final/resource/178e69b1-8d50-4250-88a7-203ff0326930?inner_span=True
https://www.memoria.fahce.unlp.edu.ar/trab_eventos/ev.11310/ev.11310.pdf

PARA CARGAR LOS PUNTOS:
https://www.keene.edu/campus/maps/tool/

webscrapp:
https://meteo.fcaglp.unlp.edu.ar/

apiClima:
https://weatherstack.com/quickstart
