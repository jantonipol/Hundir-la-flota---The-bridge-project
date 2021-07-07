# Hundir-la-flota---The-bridge-project

--------------- CODIGO HUNDIR LA FLOTA EXPLICADO ORDEN DESCENDENTE ---------------

Código desarrollado por Laurent Jacquet y Antonio Pol Fuentes

-Primero importamos las librerías necesarias para que funcione el juego (numpy, random y time)

-Desarrollamos la función "poner_barco" para crear los distintos barcos necesarios en el juego, tanto para el jugador como para la maquina.
Consta de tres argumentos de entrada ("eslora" -> determina el tamaño del barco; "contador_barco" -> el numero de barcos que se crean;
"tablero" -> tablero donde actúa la función
	Dentro de la función mediante un bucle while mientras que "contador_barco" sea mayor a 0 calcula aleatoriamente la orientación del barco
	y su posición inicial (fila y columna, también aleatorio). A continuación mediante un if y una serie de elif
	comprueba la orientación y en la que coincida posicionara el barco. Cuando coincida la orientación con las condiciones
	realiza un -1 a "contador_barco" y vuelve a iniciarse el bucle hasta que el valor de "contador_barco" sea 0.

-Desarrollamos la función "crear_tablero" donde mediante numpy elabora un tablero de 10x10 con el carácter " ".

-Con esta función creamos cuatro variables para los cuatro tableros necesarios para el juego (tablero_usuario1, tablero_usuario1_disparos, tablero_usuario2
y tablero_usuario2_disparos) a cada variable le asignamos la función "crear_tablero()" para generarlos.

-A continuación generamos los barcos para el jugador 1 (el usuario) con la función "poner_barco". Lo que establece que son los barcos
del jugador 1 (la persona) es el argumento de entrada tablero mediante "tablero_usuario1"
	
	poner_barco(4,1,tablero_usuario1) -> Eslora 4, 1 barco para el usuario
	poner_barco(3,2,tablero_usuario1) -> Eslora 3, 2 barcos para el usuario
	poner_barco(2,3,tablero_usuario1) -> Eslora 2, 3 barcos para el usuario
	poner_barco(1,4,tablero_usuario1) -> Eslora 1, 4 barcos para el usuario

-Turno de los barcos del jugador 2 (la maquina) asignados mediante tablero_usuario2

  poner_barco(4,1,tablero_usuario2) -> Eslora 4, 1 barco para la maquina
	poner_barco(3,2,tablero_usuario2) -> Eslora 3, 2 barcos para la maquina
	poner_barco(2,3,tablero_usuario2) -> Eslora 2, 3 barcos para la maquina

poner_barco(1,4,tablero_usuario2) -> Eslora 1, 4 barcos para la maquina

-contadores de disparos acertados de cada jugador. El contador_1 para el usuario y el contador_2 para la maquina
  contador_1 = 0
  contador_2 = 0

-Un booleano para establecer el usuario y la maquina. True es el usuario1 y False es el ordenador
tipo_jugador = True

-Un print con un mensaje de inicio explicando el funcionamiento del juego.

-Bucle while que da inicio al juego el si. El bucle funcionara mientras que el contador_1 y el contador_2 sean menores de 20.
Una vez que cualquiera de los contadores alcanza 20 se termina el bucle while y finaliza el juego.

-El funcionamiento del bucle while viene determinado por el booleano "tipo_jugador". Si "tipo_jugador" es True (el usuario) se declaran dos variables (x, y)
donde se pide que introduzcan un numero del 0 al 9 con lo que se determinan las coordenadas con las que atacar a la maquina. Con estas coordenadas
compara la fila y columna introducidas con el "tablero_usuario2" y en caso de que en esa posición este el carácter "O" (un barco) se realiza un +1 a contador_1
(acierto del jugador al barco enemigo) y vuelve a repetirse la introducción de coordenadas. Un elif para los casos en que la coordenada tenga el carácter " " (agua) cambia el tipo de jugador a False y imprime mensaje
disparo fallido. Un else que recoge el caso de coordenada que ya se ha introducido anteriormente, cambia a False pasando turno a la maquina.
Un except con un continue en el que se incluye NameError, ValueError y IndexError para evitar que introducir un carácter que no este entre el rango de 0 y 9 rompa el programa
(por ejemplo, introducir "a" o 77)

En caso de fallo de disparo o introducción de coordenada que ya se ha utilizado se pasa a False siendo el turno de la maquina. El funcionamiento del código es el mismo que en el if con el valor True pero en
este caso se dispara de forma aleatoria con dos variables x2 e y2 asignados a random.randint(0,9) para generar la fila y la columna aleatoria con la que disparar al tablero del jugador sumando +1 a contador_2 en caso de acertar.

El código del turno de la maquina es igual que el de el jugador añadiendo un time.sleep de medio segundo para añadir un delay al disparo de la maquina. La otra diferencia es que en las ocasiones que impacte en agua o se
introduzca una coordenada ya registrada el "tipo_jugador" se asigne a True volviendo el turno al usuario.

-Este proceso de disparos entre la maquina y el jugador se repetirá por el bucle While hasta que el contador de uno de los jugadores llegue a 20 (acierto en todos los barcos del enemigo) momento en que se sale del bucle
y mediante un if (contador_1 > contador_2 -> Victoria del jugador) y un elif (contador_2 > contador_1 -> Victoria de la maquina) se lanza un mensaje de victoria según el caso que corresponda finalizando el juego.
