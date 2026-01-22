
import math
import random

# Coordenadas de cada nodo
coordenadas = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (4, 0),
    'D': (6, 1),
    'E': (3, 4),
    'F': (5, 5)
}

# Grafo con conexiones
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

def temple_simulado(grafo, inicio, objetivo, temperatura=1000, enfriamiento=0.95):
    nodo_actual = inicio
    while temperatura > 1:
        print(f"Nodo actual: {nodo_actual}, Temperatura: {temperatura:.2f}")
        
        if nodo_actual == objetivo:
            print("Objetivo encontrado!")
            return True
        
        vecinos = grafo.get(nodo_actual, [])
        if not vecinos:
            print("No hay vecinos disponibles.")
            return False
        
        siguiente_nodo = random.choice(vecinos)
        delta_heuristica = heuristica(siguiente_nodo, objetivo) - heuristica(nodo_actual, objetivo)
        
        if delta_heuristica < 0 or random.random() < math.exp(-delta_heuristica / temperatura):
            nodo_actual = siguiente_nodo
        
        temperatura *= enfriamiento  # Reducir la temperatura

    print("No se alcanzó el objetivo.")
    return False

# Ejemplo de uso
temple_simulado(grafo, 'A', 'F')
