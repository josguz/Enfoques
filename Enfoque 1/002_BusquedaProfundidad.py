
# Grafo representado como un diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def busqueda_en_profundidad(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    
    print(inicio, end=" ")
    visitados.add(inicio)

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            busqueda_en_profundidad(grafo, vecino, visitados)

# Ejemplo de uso
busqueda_en_profundidad(grafo, 'A')
