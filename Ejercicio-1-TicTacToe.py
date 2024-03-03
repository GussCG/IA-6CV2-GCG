
#Autor: Gustavo Cerda García
#Ejericio 1. Tic Tac Toe "Tonto"

#Programa que simula el juego de Tic Tac Toe
#El juego se puede jugar entre dos jugadores o contra la computadora
#La computadora juega de forma aleatoria (no tiene un tipo de inteligencia)

#Librerias
import os
import random
import time
from collections import deque

#Variables globales
#tablero: Arreglo que representa el tablero del juego
tablero = [" ", " ", " "],[" ", " ", " "],[" ", " ", " "]
#turno: Cola que representa el turno de los jugadores
turno = deque(["O", "X"])
#jugador1: Nombre del jugador 1
jugador1 = ""
#jugador2: Nombre del jugador 2
jugador2 = ""

#Nombre: menuInicio
#Descripción: Muestra el menú de inicio del juego
#Salidas: opcion
def menuInicio():
    os.system("cls")
    print("|---------------------------------|")
    print("|          TIC TAC TOE            |")
    print("|---------------------------------|")
    print("| 1. Jugador vs Jugador           |")
    print("| 2. Jugador vs Computadora       |")
    print("| 3. Computadora vs Computadora   |")    
    print("| 4. Salir                        |")
    print("|---------------------------------|")
    print("| Ingrese una opción              |")
    print("|---------------------------------|")
    opcion = int(input("| Opcion:  ")) 
    print("|---------------------------------|")
    return opcion

#Nombre: mostrarTablero
#Descripción: Muestra el tablero del juego
def mostrarTablero():
    print("")
    print("   ", tablero[0][0], " |  ", tablero[0][1], " |  ", tablero[0][2])
    print(" ------|------|------")
    print("   ", tablero[1][0], " |  ", tablero[1][1], " |  ", tablero[1][2])
    print(" ------|------|------")
    print("   ", tablero[2][0], " |  ", tablero[2][1], " |  ", tablero[2][2])
    print("")

#Nombre: resetTablero
#Descripción: Reinicia el tablero del juego
def resetTablero():
    for i in range(3):
        for j in range(3):
            tablero[i][j] = " "

#Nombre: rotarTurno
#Descripción: Cambia el turno de los jugadores
#Salidas: turno[0] <- Jugador actual
def rotarTurno():
    turno.rotate()
    return turno[0]

#Nombre: procesarPosicion
#Descripción: Procesa la posición ingresada por el jugador y la convierte a una posición en el tablero
#Entradas: posicion
#Salidas: posicion_l
def procesarPosicion(posicion):
    posicion = int(posicion)
    if posicion == 1:
        return 0, 0
    elif posicion == 2:
        return 0, 1
    elif posicion == 3:
        return 0, 2
    elif posicion == 4:
        return 1, 0
    elif posicion == 5:
        return 1, 1
    elif posicion == 6:
        return 1, 2
    elif posicion == 7:
        return 2, 0
    elif posicion == 8:
        return 2, 1
    elif posicion == 9:
        return 2, 2
    else:
        return -1, -1

#Nombre: posicion_correcta
#Descripción: Verifica si la posición ingresada por el jugador es correcta (no está ocupada) o se encuentra dentro del tablero
#Entradas: posicion
#Salidas: True si la posición es correcta, False en otro caso
def posicion_correcta(posicion):
    if 0 <= posicion[0] < 3 and 0 <= posicion[1] < 3:
        if tablero[posicion[0]][posicion[1]] == " ":
            return True
    return False

#Nombre: actualizar_tablero
#Descripción: Actualiza el tablero con la jugada del jugador
#Entradas: posicion, jugador
def actualizar_tablero(posicion, jugador):
    tablero[posicion[0]][posicion[1]] = jugador

#Nombre: verificarGanador
#Descripción: Verifica si un jugador ha ganado el juego (3 en raya)
#Entradas: jugador
#Salidas: True si el jugador ha ganado, False en otro caso
def verificarGanador(jugador):
    #Verificar filas
    for i in range(3):
        if tablero[i][0] == jugador and tablero[i][1] == jugador and tablero[i][2] == jugador:
            return True
    #Verificar columnas
    for i in range(3):
        if tablero[0][i] == jugador and tablero[1][i] == jugador and tablero[2][i] == jugador:
            return True
    #Verificar diagonales
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True
    return False

#Nombre: esEmpate
#Descripción: Verifica si el juego ha terminado en empate (no hay más movimientos posibles)
#Salidas: True si el juego ha terminado en empate, False en otro caso
def esEmpate():
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                return False
    return True

#Nombre: jugadorVsJugador
#Descripción: Juego de Tic Tac Toe entre dos jugadores
def jugadorVsJugador():
    os.system("cls")
    print("|---------------------------------|")
    print("|       JUGADOR VS JUGADOR        |")
    print("|---------------------------------|")
    print("| Ingrese el nombre del jugador 1 |")
    print("|---------------------------------|")
    jugador1 = input("| Nombre: ")
    os.system("cls")
    print("|---------------------------------|")
    print("|       JUGADOR VS JUGADOR        |")
    print("|---------------------------------|")
    print("| Ingrese el nombre del jugador 2 |")
    print("|---------------------------------|")
    jugador2 = input("| Nombre: ")
    print("|---------------------------------|")
    os.system("cls")
    #Se muestran las instrucciones
    print("|---------------------------------|")
    print("|       JUGADOR VS JUGADOR        |")
    print("|---------------------------------|")
    print("|         INSTRUCCIONES           |")
    print("|---------------------------------|")
    print("| El tablero se muestra de la     |")
    print("| siguiente forma:                |")
    print("|---------------------------------|")
    print("|        1   |  2   |  3          |")
    print("|      ------|------|------       |")
    print("|        4   |  5   |  6          |")
    print("|      ------|------|------       |")
    print("|        7   |  8   |  9          |")
    print("|---------------------------------|")
    print("| Cada jugador deberá ingresar    |")
    print("| el número de la casilla en la   |")
    print("| que desea colocar su ficha      |")
    print("|---------------------------------|")
    print("| Presione enter para continuar   |")
    print("|---------------------------------|")
    input()
    os.system("cls")
    mostrarTablero()
    jugador = rotarTurno()
    print("|---------------------------------|")
    print("|       JUGADOR VS JUGADOR        |")
    print("|---------------------------------|")
    print("|        Comienza el juego        |")
    print("|---------------------------------|")

    #Ciclo principal del juego
    while True:
        #Se obtiene el nombre del jugador actual
        nombreJugador = (jugador1 if jugador == "X" else jugador2)
        posicion = input("| "+ nombreJugador +" --> "+ (jugador) +" ingrese la casilla: ")
        print("|---------------------------------|")
        #Se procesa la posición ingresada por el jugador
        try:
            posicion_l = procesarPosicion(posicion)
        except:
            #Si la posición no es válida se muestra un mensaje de error
            print("|       POSICION NO VALIDA        |")
            print("|---------------------------------|")            
            continue
        if posicion_correcta(posicion_l):
            #Si la posición es válida se actualiza el tablero
            actualizar_tablero(posicion_l, jugador)
            os.system("cls")
            mostrarTablero()
            print("|---------------------------------|")
            print("|       JUGADOR VS JUGADOR        |")
            print("|---------------------------------|")
            if verificarGanador(jugador):
                os.system("cls")
                print("|---------------------------------|")
                print("|         JUGADOR GANADOR         |")
                print("|---------------------------------|")
                print("|  {}                             |".format(nombreJugador))
                print("|---------------------------------|")
                input("Enter para continuar")
                break
            elif esEmpate():
                os.system("cls")
                print("|---------------------------------|")
                print("|            EMPATE                |")
                print("|---------------------------------|")
                input("Enter para continuar")
                break
            jugador = rotarTurno()
        else:
            print("|      POSICION INCORRECTA        |")
            print("|---------------------------------|")
    
#Nombre: jugadorVsComputadora
#Descripción: Juego de Tic Tac Toe entre un jugador y la computadora
def jugadorVsComputadora():
    os.system("cls")
    print("|---------------------------------|")
    print("|     JUGADOR VS COMPUTADORA      |")
    print("|---------------------------------|")
    print("| Ingrese el nombre del jugador   |")
    print("|---------------------------------|")
    jugador1 = input("| Nombre: ")
    jugador2 = "Computadora"
    os.system("cls")
    #Se muestran las instrucciones
    print("|---------------------------------|")
    print("|     JUGADOR VS COMPUTADORA      |")
    print("|---------------------------------|")
    print("|         INSTRUCCIONES           |")
    print("|---------------------------------|")
    print("| El tablero se muestra de la     |")
    print("| siguiente forma:                |")
    print("|---------------------------------|")
    print("|        1   |  2   |  3          |")
    print("|      ------|------|------       |")
    print("|        4   |  5   |  6          |")
    print("|      ------|------|------       |")
    print("|        7   |  8   |  9          |")
    print("|---------------------------------|")
    print("| Cada jugador deberá ingresar    |")
    print("| el número de la casilla en la   |")
    print("| que desea colocar su ficha      |")
    print("|---------------------------------|")
    print("| Presione enter para continuar   |")
    print("|---------------------------------|")
    input()
    os.system("cls")
    mostrarTablero()
    jugador = rotarTurno()
    print("|---------------------------------|")
    print("|     JUGADOR VS COMPUTADORA      |")
    print("|---------------------------------|")
    print("|        Comienza el juego        |")
    print("|---------------------------------|")

    while True:
        nombreJugador = (jugador1 if jugador == "X" else jugador2)
        if nombreJugador == "Computadora":
            #Hacer jugada de la computadora
            #Se elige una casilla aleatoria
            posicion = random.randint(1, 9)
        else:
            posicion = input("| "+ nombreJugador +" --> "+ (jugador) +" ingrese la casilla: ")
        print("|---------------------------------|")
        try:
            posicion_l = procesarPosicion(posicion)
        except:
            print("|       POSICION NO VALIDA        |")
            print("|---------------------------------|")            
            continue
        if posicion_correcta(posicion_l):
            actualizar_tablero(posicion_l, jugador)
            os.system("cls")
            mostrarTablero()
            print("|---------------------------------|")
            print("|     JUGADOR VS COMPUTADORA      |")
            print("|---------------------------------|")
            if verificarGanador(jugador):
                os.system("cls")
                print("|---------------------------------|")
                print("|         JUGADOR GANADOR         |")
                print("|---------------------------------|")
                print("|  {}                             |".format(nombreJugador))
                print("|---------------------------------|")
                input("Enter para continuar")
                break
            elif esEmpate():
                os.system("cls")
                print("|---------------------------------|")
                print("|            EMPATE                |")
                print("|---------------------------------|")
                input("Enter para continuar")
                break
            jugador = rotarTurno()
        else:
            print("|      POSICION INCORRECTA        |")
            print("|---------------------------------|")

#Nombre: computadoraVsComputadora
#Descripción: Juego de Tic Tac Toe entre dos computadoras
def computadoraVsComputadora():
    os.system("cls")
    print("|---------------------------------|")
    print("|   COMPUTADORA VS COMPUTADORA    |")
    print("|---------------------------------|")
    jugador1 = "Computadora 1"
    jugador2 = "Computadora 2"
    os.system("cls")
    #Se muestran las instrucciones
    print("|---------------------------------|")
    print("|   COMPUTADORA VS COMPUTADORA    |")
    print("|---------------------------------|")
    print("|         INSTRUCCIONES           |")
    print("|---------------------------------|")
    print("| El tablero se muestra de la     |")
    print("| siguiente forma:                |")
    print("|---------------------------------|")
    print("|        1   |  2   |  3          |")
    print("|      ------|------|------       |")
    print("|        4   |  5   |  6          |")
    print("|      ------|------|------       |")
    print("|        7   |  8   |  9          |")
    print("|---------------------------------|")
    print("| Cada jugador deberá ingresar    |")
    print("| el número de la casilla en la   |")
    print("| que desea colocar su ficha      |")
    print("|---------------------------------|")
    print("| Presione enter para continuar   |")
    print("|---------------------------------|")
    input()
    os.system("cls")
    mostrarTablero()
    jugador = rotarTurno()
    print("|---------------------------------|")
    print("|   COMPUTADORA VS COMPUTADORA    |")
    print("|---------------------------------|")
    print("|        Comienza el juego        |")
    print("|---------------------------------|")

    while True:
        nombreJugador = (jugador1 if jugador == "X" else jugador2)
        #Hacer jugada de la computadora
        #Se elige una casilla aleatoria
        posicion = random.randint(1, 9)
        print("|---------------------------------|")
        try:
            posicion_l = procesarPosicion(posicion)
        except:
            print("|       POSICION NO VALIDA        |")
            print("|---------------------------------|")            
            continue
        if posicion_correcta(posicion_l):
            actualizar_tablero(posicion_l, jugador)
            time.sleep(1)
            os.system("cls")
            mostrarTablero()
            print("|---------------------------------|")
            print("|   COMPUTADORA VS COMPUTADORA    |")
            print("|---------------------------------|")
            if verificarGanador(jugador):
                time.sleep(1)
                os.system("cls")
                print("|---------------------------------|")
                print("|         JUGADOR GANADOR         |")
                print("|---------------------------------|")
                print("|  {}                             |".format(nombreJugador))
                print("|---------------------------------|")
                input("Enter para continuar")
                break
            elif esEmpate():
                os.system("cls")
                print("|---------------------------------|")
                print("|            EMPATE                |")
                print("|---------------------------------|")
                input("Enter para continuar")
                break
            jugador = rotarTurno()
        else:
            print("|      POSICION INCORRECTA        |")
            print("|---------------------------------|")

#Nombre: juego
#Descripción: Función principal del juego            
def juego():
    while True:
        opcion = menuInicio()
        resetTablero()
        if opcion == 1:
            jugadorVsJugador()  
        elif opcion == 2:
            jugadorVsComputadora()
        elif opcion == 3:
            computadoraVsComputadora()
        elif opcion == 4:
            break
        else:
            print("Opcion no valida")

#Inicio del programa
juego()
        
        

    
