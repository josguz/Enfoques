
import heapq
import math

# Representación del grafo con vecinos y distancias
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 1},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

# Coordenadas de los nodos para calcular la heurística
coordenadas = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (4, 0),
    'D': (6, 1),
    'E': (3, 4),
    'F': (5, 5)
}

def heuristica(nodo, objetivo):
    # Calcula la distancia euclidiana como heurística
    x1, y1 = coordenadas[nodo]
    x2, y2 = coordenadas[objetivo]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def busqueda_voraz(grafo, inicio, objetivo):
    # Cola de prioridad basada en la heurística
    cola_prioridad = [(heuristica(inicio, objetivo), inicio)]
    visitados = set()
    
    while cola_prioridad:
        _, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == objetivo:
            print(f"Objetivo '{objetivo}' encontrado.")
            return True
        
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            # Agregar vecinos a la cola con la heurística como prioridad
            for vecino in grafo.get(nodo_actual, {}):
                if vecino not in visitados:
                    heapq.heappush(cola_prioridad, (heuristica(vecino, objetivo), vecino))
    
    print("Objetivo no encontrado.")
    return False

# Ejemplo de uso
busqueda_voraz(grafo, 'A', 'F')
