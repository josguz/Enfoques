
import heapq

# Grafo representado como un diccionario con costos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

def busqueda_costo_uniforme(grafo, inicio, objetivo):
    cola_prioridad = [(0, inicio)]  # Cola de prioridad (min-heap) con costo inicial
    visitados = set()  # Nodos visitados

    while cola_prioridad:
        costo, nodo = heapq.heappop(cola_prioridad)
        if nodo in visitados:
            continue

        print(f"Visitando nodo {nodo} con costo {costo}")
        if nodo == objetivo:
            return costo

        visitados.add(nodo)
        for vecino, costo_vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                heapq.heappush(cola_prioridad, (costo + costo_vecino, vecino))

    return float('inf')  # Si no se encuentra el objetivo

# Ejemplo de uso
costo_total = busqueda_costo_uniforme(grafo, 'A', 'F')
print("Costo total al objetivo:", costo_total)
