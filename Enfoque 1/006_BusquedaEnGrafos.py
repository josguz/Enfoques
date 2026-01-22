
# Grafo representado como un diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def busqueda_en_grafo(grafo, inicio, objetivo, metodo='anchura'):
    # Uso de búsqueda en anchura o profundidad en función del parámetro 'metodo'
    if metodo == 'anchura':
        return busqueda_en_anchura(grafo, inicio, objetivo)
    elif metodo == 'profundidad':
        return busqueda_en_profundidad(grafo, inicio, objetivo)
    else:
        raise ValueError("Método no válido. Usa 'anchura' o 'profundidad'.")

def busqueda_en_anchura(grafo, inicio, objetivo):
    cola = [inicio]
    visitados = set()
    
    while cola:
        nodo = cola.pop(0)  # Extraemos el primer nodo (FIFO)
        if nodo == objetivo:
            print(f"Objetivo '{objetivo}' encontrado.")
            return True
        if nodo not in visitados:
            visitados.add(nodo)
            cola.extend(grafo.get(nodo, []))  # Agregamos vecinos
    print("Objetivo no encontrado.")
    return False

def busqueda_en_profundidad(grafo, inicio, objetivo, visitados=None):
    if visitados is None:
        visitados = set()
    if inicio == objetivo:
        print(f"Objetivo '{objetivo}' encontrado.")
        return True
    visitados.add(inicio)
    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            if busqueda_en_profundidad(grafo, vecino, objetivo, visitados):
                return True
    return False

# Ejemplo de uso
busqueda_en_grafo(grafo, 'A', 'F', metodo='anchura')
