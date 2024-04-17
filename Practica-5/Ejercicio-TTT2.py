import os
import random
import time
from collections import deque

tablero = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]
turno = deque(["O", "X"])
jugador1 = ""
jugador2 = ""

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

def mostrarTablero():
    print("")
    print("   ", tablero[0][0], " |  ", tablero[0][1], " |  ", tablero[0][2])
    print(" ------|------|------")
    print("   ", tablero[1][0], " |  ", tablero[1][1], " |  ", tablero[1][2])
    print(" ------|------|------")
    print("   ", tablero[2][0], " |  ", tablero[2][1], " |  ", tablero[2][2])
    print("")

def resetTablero():
    for i in range(3):
        for j in range(3):
            tablero[i][j] = " "

def rotarTurno():
    turno.rotate()
    return turno[0]

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

def posicion_correcta(posicion):
    if 0 <= posicion[0] < 3 and 0 <= posicion[1] < 3:
        if tablero[posicion[0]][posicion[1]] == " ":
            return True
    return False

def actualizar_tablero(posicion, jugador):
    tablero[posicion[0]][posicion[1]] = jugador

def verificarGanador(jugador):
    for i in range(3):
        if tablero[i][0] == jugador and tablero[i][1] == jugador and tablero[i][2] == jugador:
            return True
    for i in range(3):
        if tablero[0][i] == jugador and tablero[1][i] == jugador and tablero[2][i] == jugador:
            return True
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True
    return False

def esEmpate():
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                return False
    return True

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

    while True:
        nombreJugador = (jugador1 if jugador == "X" else jugador2)
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
            posicion = elegirMovimientoComputadora(jugador)
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

def computadoraVsComputadora():
    os.system("cls")
    print("|---------------------------------|")
    print("|   COMPUTADORA VS COMPUTADORA    |")
    print("|---------------------------------|")
    jugador1 = "Computadora 1"
    jugador2 = "Computadora 2"
    os.system("cls")
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
        posicion = elegirMovimientoComputadora(jugador)
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

#! CAMBIOS
def elegirMovimientoComputadora(jugador):
    # Estrategia heurística
    # 1. Ganar si es posible
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                tablero[i][j] = jugador
                if verificarGanador(jugador):
                    tablero[i][j] = " "
                    return (i * 3) + j + 1
                tablero[i][j] = " "

    # 2. Bloquear al oponente si está a punto de ganar
    oponente = "O" if jugador == "X" else "X"
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                tablero[i][j] = oponente
                if verificarGanador(oponente):
                    tablero[i][j] = " "
                    return (i * 3) + j + 1
                tablero[i][j] = " "

    # 3. Si no se puede ganar ni bloquear, elegir una casilla aleatoria
    movimientos_disponibles = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                movimientos_disponibles.append((i * 3) + j + 1)
    return random.choice(movimientos_disponibles)

juego()
