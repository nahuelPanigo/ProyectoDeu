insert into configurations (title, description, contact, state)
VALUES ("Alertas las plata", "el sitio web trata de alertar a los ciudadanos ante posibles inundaciones mediante alertas configurables dea acuerdo a los puntos de interes. Ademas muestra informacion de precipitaciones actuales proximas, pasadas y mapas de informacion", "DEU@info.unlp.com.ar",1);



insert into clima (milimetrosXDia, milimetrosxSemana, probabilidadDePrecipitaciones, estimacionDePrecipitaciones,ultimaActualizacion)
VALUES (0,5,20,0,CAST(N'2012-06-18 10:34:09.000' AS DateTime));


insert into users (email, username ,password ,active)
VALUES ("nahpanigo99@gmail.com","npanigo","contra1",1);

insert into users (email, username ,password ,active)
VALUES ("villanuevajimena39@gmail.com","jvillanueva","contra2",1);

insert into users (email, username ,password ,active)
VALUES ("admin@DEU.com","userDeu","contra",1);
