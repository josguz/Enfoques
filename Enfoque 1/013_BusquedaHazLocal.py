
import math
import random

# Coordenadas de los nodos
coordenadas = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (4, 0),
    'D': (6, 1),
    'E': (3, 4),
    'F': (5, 5)
}

# Grafo representado con conexiones
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def heuristica(nodo, objetivo):
    x1, y1 = coordenadas[nodo]
    x2, y2 = coordenadas[objetivo]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def busqueda_haz_local(grafo, inicio, objetivo, k=2):
    # Inicializar el conjunto de caminos (haz)
    haz = [(inicio, heuristica(inicio, objetivo))]
    while haz:
        print("Haz actual:", [nodo for nodo, _ in haz])
        # Comprobar si se ha alcanzado el objetivo en alguno de los caminos del haz
        for nodo, _ in haz:
            if nodo == objetivo:
                print("Objetivo encontrado!")
                return True
        
        # Expansión del haz para los vecinos de cada nodo
        nuevo_haz = []
        for nodo, _ in haz:
            vecinos = grafo.get(nodo, [])
            for vecino in vecinos:
                nuevo_haz.append((vecino, heuristica(vecino, objetivo)))
        
        # Ordenar los nodos expandidos por su heurística y seleccionar los mejores k
        nuevo_haz = sorted(nuevo_haz, key=lambda x: x[1])[:k]
        
        # Si no hay mejoras, terminamos
        if not nuevo_haz:
            print("No hay camino mejor disponible.")
            return False
        
        haz = nuevo_haz  # Actualizar el haz con los mejores caminos

    print("No se alcanzó el objetivo.")
    return False

# Ejemplo de uso
busqueda_haz_local(grafo, 'A', 'F')
