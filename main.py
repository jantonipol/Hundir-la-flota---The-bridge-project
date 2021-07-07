import numpy as np
import random
import time



def poner_barco(eslora, contador_barco, tablero):
    while contador_barco > 0:
        # Orientacion aleatoria

        orient = random.choice(["N", "S", "E", "O"])

        # Posicion inicial del barco

        current_pos = np.random.randint(9, size=2)
        fila = current_pos[0]
        col = current_pos[1]

        # Recogemos las 4 posiciones candidatas
        coors_posIN = tablero[fila:fila - eslora: -1, col]  # fila-eslora por que va hacia el norte. Hacia el sur seria fila+eslora

        coors_posIE = tablero[fila, col:col + eslora]

        coors_posIS = tablero[fila:fila + eslora, col]

        coors_posIO = tablero[fila, col: col - eslora:-1]
        # Compruebo norte
        if (orient == "N") and (len(coors_posIN) == eslora) and ("O" not in coors_posIN):
            tablero[fila:fila - eslora:-1, col] = "O"
            contador_barco = contador_barco - 1


        # Compruebo este

        elif (orient == "E") and (len(coors_posIE) == eslora) and ("O" not in coors_posIE):
            tablero[fila, col:col + eslora] = "O"
            contador_barco = contador_barco - 1


        # compruebo Sur

        elif (orient == "S") and (len(coors_posIS) == eslora) and ("O" not in coors_posIS):
            tablero[fila:fila + eslora, col] = "O"
            contador_barco = contador_barco - 1

        # Compruebo O
        elif (orient == "O") and (len(coors_posIO) == eslora) and ("O" not in coors_posIO):
            tablero[fila, col: col - eslora:-1] = 'O'
            contador_barco = contador_barco - 1

    return tablero


# Función para crear los tableros
def crear_tablero():
    return np.full((10, 10), " ")


# 4 variables para los 4 tablerose
tablero_usuario1 = crear_tablero()
tablero_usuario1_disparos = crear_tablero()
tablero_usuario2 = crear_tablero()
tablero_usuario2_disparos = crear_tablero()

# barcos añadido de forma aleatoria

# barcos jugador1
poner_barco(4,1,tablero_usuario1)
poner_barco(3,2,tablero_usuario1)
poner_barco(2,3,tablero_usuario1)
poner_barco(1,4,tablero_usuario1)

# barcos jugador2
poner_barco(4,1,tablero_usuario2)
poner_barco(3,2,tablero_usuario2)
poner_barco(2,3,tablero_usuario2)
poner_barco(1,4,tablero_usuario2)


#contadores de disparos acertados de cada jugador. El contador_1 para el usuario y el contador_2 para el ordenador
contador_1 = 0
contador_2 = 0

#True es el usuario1 y False es el ordenador
tipo_jugador = True

#Mensaje de inicio

print("Introduce fila y columna para acabar con los barcos del enemigo. Por cada acierto se repite disparo hasta que falles. Victoria con 20 aciertos. Suerte!")

while contador_1 < 20 and contador_2 < 20:

    # turno usuario 1
    if tipo_jugador == True:

        try:
            x = int(input("Elige un numero de fila entre 0 y 9: "))
            y = int(input("Elige un numero de columna entre 0 y 9: "))

            if tablero_usuario2[x, y] == "O":
                tablero_usuario1_disparos[x, y] = "X"
                tablero_usuario2[x, y] = "X"
                contador_1 += 1
                print("Tocado!!\nTablero de disparos usuario 1\n", tablero_usuario1_disparos, "\n")

            elif tablero_usuario2[x, y] == " ":
                tablero_usuario1_disparos[x, y] = "-"
                tablero_usuario2[x, y] = "-"
                tipo_jugador = False
                print("Al agua!!\nTablero de disparos usuario 1\n", tablero_usuario1_disparos, "\n")
            else:
                tipo_jugador = False
                print("Ya has eligido esta coordenada...\nTablero de disparos usuario 1\n", tablero_usuario1_disparos, "\n")

        except (NameError, ValueError, IndexError):
            print("----Tienes que eligir un numero entero entre 0 y 9. Intentalo de nuevo.----")
            continue



    # turno ordenador
    elif tipo_jugador == False:

        # disparo de forma aleatoria
        x2 = random.randint(0, 9)
        y2 = random.randint(0, 9)

        if tablero_usuario1[x2, y2] == "O":
            tablero_usuario2_disparos[x2, y2] = "X"
            tablero_usuario1[x2, y2] = "X"
            contador_2 += 1
            time.sleep(0.5)
            print("El ordenador ha tocado uno de tus barcos!!\nTablero de barcos usuario 1\n", tablero_usuario1, "\n")

        elif tablero_usuario1[x2, y2] == " ":
            tablero_usuario2_disparos[x2, y2] = "-"
            tablero_usuario1[x2, y2] = "-"
            tipo_jugador = True
            time.sleep(0.5)
            print("El ordenador ha disparado al agua!\nTablero de barcos usuario 1\n", tablero_usuario1,
                  "\n Tablero de disparos usuario 1\n", tablero_usuario1_disparos, "\n")
        else:
            tipo_jugador = True
            time.sleep(0.5)
            print("El ordenador le ha vuelto a dar a la misma coordenada...\nTablero de barcos usuario 1\n",
                  tablero_usuario1, "\nTablero de disparos usuario 1\n", tablero_usuario1_disparos, "\n")

# Mensaje final para proclamar si el usuario ha ganado o perdido
if contador_1 > contador_2:
    print("Has ganado al ordenador! Enhorabuena!!")
elif contador_2 > contador_1:
    print("Has perdido! El ordenador te ha vencido")