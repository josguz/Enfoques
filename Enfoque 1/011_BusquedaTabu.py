
import math
from collections import deque

# Representación del grafo con coordenadas
coordenadas = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (4, 0),
    'D': (6, 1),
    'E': (3, 4),
    'F': (5, 5)
}

# Grafo con conexiones entre nodos
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

def busqueda_tabu(grafo, inicio, objetivo, max_tabu=3):
    nodo_actual = inicio
    lista_tabu = deque(maxlen=max_tabu)
    
    while True:
        print(f"Nodo actual: {nodo_actual}")
        if nodo_actual == objetivo:
            print("Objetivo encontrado!")
            return True
        
        lista_tabu.append(nodo_actual)
        vecinos = grafo.get(nodo_actual, [])
        mejor_vecino = None
        mejor_heuristica = float('inf')
        
        for vecino in vecinos:
            if vecino not in lista_tabu:
                h = heuristica(vecino, objetivo)
                if h < mejor_heuristica:
                    mejor_heuristica = h
                    mejor_vecino = vecino

        if mejor_vecino is None:
            print("No se puede avanzar a un mejor nodo.")
            return False
        
        nodo_actual = mejor_vecino

# Ejemplo de uso
busqueda_tabu(grafo, 'A', 'F')
