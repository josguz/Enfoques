
import math

# Coordenadas de cada nodo en un grafo
coordenadas = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (4, 0),
    'D': (6, 1),
    'E': (3, 4),
    'F': (5, 5)
}

# Grafo representado con nodos y sus vecinos
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def heuristica(nodo, objetivo):
    # Calcula la distancia euclidiana como heurística
    x1, y1 = coordenadas[nodo]
    x2, y2 = coordenadas[objetivo]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def ascension_colinas(grafo, inicio, objetivo):
    nodo_actual = inicio
    while True:
        print(f"Nodo actual: {nodo_actual}")
        if nodo_actual == objetivo:
            print("Objetivo encontrado!")
            return True
        
        # Encontrar el vecino con la mejor (menor) heurística
        vecinos = grafo.get(nodo_actual, [])
        mejor_vecino = None
        mejor_heuristica = float('inf')
        
        for vecino in vecinos:
            h = heuristica(vecino, objetivo)
            if h < mejor_heuristica:
                mejor_heuristica = h
                mejor_vecino = vecino

        # Si el vecino actual es peor que el nodo actual, detén la búsqueda
        if mejor_heuristica >= heuristica(nodo_actual, objetivo):
            print("No se puede avanzar hacia un mejor nodo.")
            return False
        
        nodo_actual = mejor_vecino

# Ejemplo de uso
ascension_colinas(grafo, 'A', 'F')
