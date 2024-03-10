
#Autor: Gustavo Cerda García
#Ejericio 1. DFS - 4 Puzzle"

#Programa que resuelve el problema del 4-puzzle utilizando el algoritmo de búsqueda en profundidad (DFS).

#Librerías
from arbol import Nodo

# Función para buscar la solución al 4x1 Puzzle utilizando DFS
# Entrada:
#   - estado_inicial (Lista): Estado inicial del 4x1 Puzzle
#   - solucion (Lista): Estado solución del 4x1 Puzzle
# Salida:
#   - nodo_actual (Nodo): Nodo solución
def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []  # lista de nodos visitados
    nodos_frontera = []  # pila de nodos frontera

    # Creamos el nodo inicial del árbol de búsqueda
    nodoInicial = Nodo(estado_inicial)

    # Añadimos el nodo inicial a la lista de nodos frontera
    nodos_frontera.append(nodoInicial)

    # Mientras haya nodos en la frontera y no se haya encontrado la solución
    while (not solucionado) and len(nodos_frontera) != 0:
        # Extraemos el nodo actual de la pila (usamos una pila para DFS)
        nodo_actual = nodos_frontera.pop()

        # Si el nodo actual es la solución, marcamos como solucionado
        if nodo_actual.get_datos() == solucion:
            solucionado = True
            return nodo_actual

        # Añadimos el nodo actual a la lista de nodos visitados
        nodos_visitados.append(nodo_actual)

        # Generamos los hijos del nodo actual y los añadimos a la frontera
        hijos = generar_hijos(nodo_actual)
        for hijo in hijos:
            if (not hijo.en_lista(nodos_visitados)) and (not hijo.en_lista(nodos_frontera)):
                nodos_frontera.append(hijo)

    # Si llegamos aquí, no se encontró solución
    print("No se encontró una solución.")
    return None

# Función para generar los hijos de un nodo en el 4x1 Puzzle
# Hace movimientos de los dos elementos de la izquierda
# También de los dos elementos de la derecha
# Y también los dos elementos del centro
# No hay espacio en blanco, solo se intercambian los elementos
# Entrada:
#   - nodo (Nodo): Nodo padre
# Salida:
#  - hijos (Lista): Lista de nodos hijos
def generar_hijos(nodo):
    hijos = []

    # Obtenemos el estado actual del nodo
    estado = nodo.get_datos()

    # Intercambiamos los dos elementos de la izquierda
    hijo = [estado[1], estado[0], estado[2], estado[3]]
    hijo_izquierdo = Nodo(hijo)
    hijos.append(hijo_izquierdo)

    # Intercambiamos los dos elementos del centro
    hijo = [estado[0], estado[2], estado[1], estado[3]]
    hijo_central = Nodo(hijo)
    hijos.append(hijo_central)

    # Intercambiamos los dos elementos de la derecha
    hijo = [estado[0], estado[1], estado[3], estado[2]]
    hijo_derecho = Nodo(hijo)
    hijos.append(hijo_derecho)

    # Añadimos los hijos al nodo actual
    nodo.set_hijos(hijos)

    # Les asignamos el nodo padre a los hijos
    for h in hijos:
        h.set_padre(nodo)

    return hijos

if __name__ == "__main__":
    estado_inicial=[4,2,3,1]
    solucion=[1,2,3,4]

    # Buscamos la solución al 4x1 Puzzle
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)

    # Mostramos el resultado y el camino a la solución
    resultado=[]
    resultado.append(nodo_solucion.get_datos())
    print("Estado Inicial: ", estado_inicial)
    print("Resultado:")
    print(resultado)

    # Calculamos el camino a la solución
    # Recorremos el árbol de búsqueda desde el nodo solución hasta el nodo inicial
    nodo = nodo_solucion

    while nodo.get_padre() != None:
        nodo = nodo.get_padre()
        resultado.append(nodo.get_datos())

    print("Camino a la solución:")
    resultado.reverse()

    for r in resultado:
        print("-> ", r)


