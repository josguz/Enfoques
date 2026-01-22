
from collections import deque
# Grafo representado como un diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def busqueda_en_anchura(grafo, inicio):
    visitados = set()  # Nodos visitados
    cola = deque([inicio])  # Cola de búsqueda (FIFO)

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            print(nodo, end=" ")  # Procesar nodo
            visitados.add(nodo)
            cola.extend(grafo[nodo])  # Agregar vecinos a la cola
# Ejemplo de uso
busqueda_en_anchura(grafo, 'A')
