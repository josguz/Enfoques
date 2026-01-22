
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
        return

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            busqueda_en_profundidad_limitada(grafo, vecino, limite - 1, visitados)

def busqueda_en_profundidad_iterativa(grafo, inicio, profundidad_maxima):
    for limite in range(profundidad_maxima + 1):
        print(f"\nLímite de profundidad: {limite}")
        busqueda_en_profundidad_limitada(grafo, inicio, limite)

# Ejemplo de uso con profundidad máxima 3
busqueda_en_profundidad_iterativa(grafo, 'A', 3)
