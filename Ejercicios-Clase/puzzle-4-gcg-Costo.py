from arbol import Nodo
import sys

# Variables globales
nodos_visitados = []  # lista de nodos visitados
nodos_frontera = []  # lista de nodos frontera

# Función para buscar la solución al 4x1 Puzzle utilizando A* con heurística
def buscar_solucion_Astar(estado_inicial, solucion):
    # Creamos el nodo inicial del árbol de búsqueda
    nodoInicial = Nodo(estado_inicial)
    nodoInicial.set_costo(0)  # Costo inicial

    # Añadimos el nodo inicial a la lista de nodos frontera
    nodos_frontera.append(nodoInicial)

    # Mientras haya nodos en la frontera
    while len(nodos_frontera) != 0:
        # Seleccionamos el nodo con menor costo total de la frontera
        nodo_actual = nodos_frontera[0]
        idx = 0
        for i, nodo in enumerate(nodos_frontera):
            if nodo.get_costo() < nodo_actual.get_costo():
                nodo_actual = nodo
                idx = i

        # Movemos el nodo seleccionado de la frontera a los nodos visitados
        nodos_frontera.pop(idx)
        nodos_visitados.append(nodo_actual)

        # Si el nodo actual es la solución, retornamos
        if nodo_actual.get_datos() == solucion:
            return nodo_actual

        # Generamos los hijos del nodo actual
        hijos = generar_hijos(nodo_actual)

        # Para cada hijo, calculamos su costo total y lo añadimos a la frontera
        for hijo in hijos:
            costo = nodo_actual.get_costo() + 1  # Costo por movimiento
            hijo.set_costo(costo)
            if not hijo.en_lista(nodos_visitados):
                if hijo.en_lista(nodos_frontera):
                    # Si ya está en la frontera, verificamos si este nuevo camino es mejor
                    for nodo in nodos_frontera:
                        if nodo.get_datos() == hijo.get_datos() and nodo.get_costo() > hijo.get_costo():
                            nodo.set_costo(hijo.get_costo())
                            nodo.set_padre(hijo.get_padre())
                else:
                    # Si no está en la frontera, lo añadimos
                    nodos_frontera.append(hijo)

    # Si llegamos aquí, no se encontró solución
    print("No se encontró una solución.")
    return None

# Función para generar los hijos de un nodo en el 4x1 Puzzle
def generar_hijos(nodo):
    hijos = []
    estado = nodo.get_datos()

    # Movimiento izquierdo
    hijo_izquierdo = [estado[1], estado[0], estado[2], estado[3]]
    hijos.append(Nodo(hijo_izquierdo))

    # Movimiento derecho
    hijo_derecho = [estado[0], estado[2], estado[1], estado[3]]
    hijos.append(Nodo(hijo_derecho))

    # Movimiento central
    hijo_central = [estado[0], estado[1], estado[3], estado[2]]
    hijos.append(Nodo(hijo_central))

    for hijo in hijos:
        hijo.set_padre(nodo)

    return hijos

if __name__ == "__main__":
    print("Ejercicio 1: A* - 4 Puzzle")
    estado_inicial = [4, 3, 2, 1]
    solucion = [1, 2, 3, 4]

    # Buscamos la solución al 4x1 Puzzle con A*
    nodo_solucion = buscar_solucion_Astar(estado_inicial, solucion)

    resultado = []

    # Obtenemos el camino de la solución
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)

    # Imprimir el costo total de la solución
    print("Costo total de la solución:", nodo_solucion.get_costo())
