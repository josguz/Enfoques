
# Grafo representado como un diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def busqueda_en_profundidad_limitada(grafo, inicio, limite, visitados=None):
    if visitados is None:
        visitados = set()
    
    print(inicio, end=" ")
    visitados.add(inicio)

    if limite <= 0:
        return  # Detener la búsqueda si se alcanza el límite

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            busqueda_en_profundidad_limitada(grafo, vecino, limite - 1, visitados)

# Ejemplo de uso con límite de profundidad 2
busqueda_en_profundidad_limitada(grafo, 'A', 2)
