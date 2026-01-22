
import heapq
import math

# Representación del grafo con vecinos y costos
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 1},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

# Coordenadas de los nodos para calcular la heurística (distancia euclidiana)
coordenadas = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (4, 0),
    'D': (6, 1),
    'E': (3, 4),
    'F': (5, 5)
}

def heuristica(nodo, objetivo):
    x1, y1 = coordenadas[nodo]
    x2, y2 = coordenadas[objetivo]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def busqueda_a_estrella(grafo, inicio, objetivo):
    # Cola de prioridad para nodos basada en f(n) = g(n) + h(n)
    cola_prioridad = [(0 + heuristica(inicio, objetivo), 0, inicio)]
    visitados = set()
    costos = {inicio: 0}
    
    while cola_prioridad:
        _, costo_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == objetivo:
            print(f"Objetivo '{objetivo}' encontrado con costo total: {costo_actual}")
            return True
        
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            
            for vecino, costo_vecino in grafo.get(nodo_actual, {}).items():
                nuevo_costo = costo_actual + costo_vecino
                if vecino not in costos or nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    f_n = nuevo_costo + heuristica(vecino, objetivo)
                    heapq.heappush(cola_prioridad, (f_n, nuevo_costo, vecino))
    
    print("Objetivo no encontrado.")
    return False

# Ejemplo de uso de la búsqueda A*
busqueda_a_estrella(grafo, 'A', 'F')
