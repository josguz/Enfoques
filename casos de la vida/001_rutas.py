import heapq
from collections import deque

# Grafo representando calles de una ciudad con tiempos de recorrido (en minutos)
ciudad = {
    'Almacén': {'A': 10, 'B': 15},  # Desde el almacén podemos ir a A y B
    'A': {'C': 5, 'D': 10},  # Desde A podemos ir a C y D
    'B': {'D': 20, 'E': 30},  # Desde B podemos ir a D y E
    'C': {'F': 10},  # Desde C podemos ir a F
    'D': {'F': 5},  # Desde D podemos ir a F
    'E': {'F': 15},  # Desde E podemos ir a F
    'F': {'Casa': 5},  # Desde F podemos ir a la Casa
    'Casa': {}  # La Casa es el destino final
}

# Algoritmo de búsqueda en anchura (encuentra cualquier ruta sin importar costos)
def busqueda_anchura(grafo, inicio, objetivo):
    cola = deque([[inicio]])  # Cola para explorar rutas
    visitados = set()  # Conjunto para marcar nodos visitados
    while cola:
        camino = cola.popleft()  # Sacamos el primer camino de la cola
        nodo = camino[-1]  # Último nodo del camino actual
        if nodo == objetivo:
            return camino  # Si llegamos al destino, devolvemos el camino
        if nodo not in visitados:
            visitados.add(nodo)  # Marcamos el nodo como visitado
            for vecino in grafo[nodo]:
                nuevo_camino = list(camino)  # Copiamos el camino actual
                nuevo_camino.append(vecino)  # Agregamos el vecino al camino
                cola.append(nuevo_camino)  # Lo añadimos a la cola para explorarlo
    return None  # Si no encontramos un camino, devolvemos None

# Algoritmo de búsqueda de costo uniforme (encuentra la ruta más rápida en términos de tiempo)
def busqueda_costo_uniforme(grafo, inicio, objetivo):
    cola_prioridad = [(0, [inicio])]  # Cola de prioridad con (costo acumulado, camino)
    visitados = set()  # Conjunto de nodos visitados
    while cola_prioridad:
        costo, camino = heapq.heappop(cola_prioridad)  # Sacamos la ruta con menor costo
        nodo = camino[-1]  # Último nodo en la ruta
        if nodo == objetivo:
            return camino, costo  # Si llegamos al destino, devolvemos la ruta y su costo
        if nodo not in visitados:
            visitados.add(nodo)  # Marcamos el nodo como visitado
            for vecino, costo_vecino in grafo[nodo].items():
                heapq.heappush(cola_prioridad, (costo + costo_vecino, camino + [vecino]))  # Añadimos nuevas rutas con su costo acumulado
    return None, float('inf')  # Si no encontramos el destino, devolvemos None y un costo infinito

# Prueba de los algoritmos
inicio, destino = 'Almacén', 'Casa'
print("Ruta por búsqueda en anchura:", busqueda_anchura(ciudad, inicio, destino))
ruta_optima, costo = busqueda_costo_uniforme(ciudad, inicio, destino)
print("Ruta más rápida (costo uniforme):", ruta_optima, "Tiempo total:", costo, "minutos")