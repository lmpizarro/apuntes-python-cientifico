Requiere:

Debian Wheezy con Python instalado

python control 0.6 con sus dependencias

17/09/2014:  comienzo del desarrollo de una prueba de concepto.
             llevar la aplicación de simulación de sistema de control
	     realimentado a aplicación web.
	     El núcleo de simulación sigue siendo python que publica
	     datos en Redis, un consumidor subscripto a Redis, envía
	     esos datos de simulación en "tiempo real", usando websockets.
	     Este último servidor está hecho en node.js con el framework 
	     express.







Un trabajo de lmpizarro 
