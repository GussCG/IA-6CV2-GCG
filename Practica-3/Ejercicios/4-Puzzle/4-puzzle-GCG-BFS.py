
#Autor: Gustavo Cerda García
#Ejericio 1. BFS - 4 Puzzle"

#Programa que resuelve el problema del 4-puzzle utilizando el algoritmo de búsqueda en amplitud (BFS).

#Librerías
from arbol import Nodo
import sys

# Variables globales
nodos_visitados = [] # Lista de nodos visitados
nodos_frontera = [] # Cola de nodos frontera

# Función para buscar la solución al 4x1 Puzzle utilizando BFS
# Entrada:
#   - estado_inicial (Lista): Estado inicial del 4x1 Puzzle
#   - solucion (Lista): Estado solución del 4x1 Puzzle
# Salida:
#   - nodo_actual (Nodo): Nodo solución
def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado = False

    # Creamos el nodo inicial del árbol de búsqueda
    nodoInicial = Nodo(estado_inicial)

    # Añadimos el nodo inicial a la lista de nodos frontera 
    nodos_frontera.append(nodoInicial)

    # Mientras haya nodos en la frontera y no se haya encontrado la solución
    while (not solucionado) and len(nodos_frontera) != 0:
        # Extraemos el nodo actual de la cola (usamos una cola para BFS)
        nodo = nodos_frontera.pop(0)

        # Si el nodo actual es la solución, marcamos como solucionado
        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        
        # Añadimos el nodo actual a la lista de nodos visitados
        nodos_visitados.append(nodo)
        
        # Generar hijos del nodo actual y añadirlos a la frontera
        hijos = generar_hijos_BFS(nodo)
        for hijo in hijos:
            if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo)

# Función para generar los hijos de un nodo en el 4x1 Puzzle
# Hace movimientos de los dos elementos de la izquierda
# También de los dos elementos de la derecha
# Y también los dos elementos del centro
# No hay espacio en blanco, solo se intercambian los elementos
# Entrada:
#   - nodo (Nodo): Nodo padre
# Salida:
#  - hijos (Lista): Lista de nodos hijos
def generar_hijos_BFS(nodo):
    hijos = []

    # Obtenemos el estado actual del nodo
    estado = nodo.get_datos()

    # Intercambiamos los dos elementos de la izquierda
    hijo = [estado[1], estado[0], estado[2], estado[3]]
    nodo_hijo = Nodo(hijo)
    hijos.append(nodo_hijo)

    # Intercambiamos los dos elementos de la derecha
    hijo = [estado[0], estado[2], estado[1], estado[3]]
    nodo_hijo = Nodo(hijo)
    hijos.append(nodo_hijo)

    # Intercambiamos los dos elementos del centro
    hijo = [estado[0], estado[1], estado[3], estado[2]]
    nodo_hijo = Nodo(hijo)
    hijos.append(nodo_hijo)

    # Añadimos los hijos al nodo actual
    nodo.set_hijos(hijos)

    # Le asignamos como padre al nodo actual
    for hijo in hijos:
        hijo.set_padre(nodo)

    return hijos


if __name__ == "__main__":
    print("Ejercicio 1: BFS - 4 Puzzle")
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]

    # Buscamos la solución utilizando BFS
    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)
    
    resultado = []

    # Obtenemos el camino de la solución
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)

    # Ver el uso de memoria de este algoritmo
    print("Uso de memoria: ")
    print("Nodos visitados: ", sys.getsizeof(nodos_visitados))
    print("Nodos frontera: ", sys.getsizeof(nodos_frontera))


