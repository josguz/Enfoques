
# Definición de nodos y conexiones en el grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Función para aplicar el acondicionamiento del corte
def acondicionamiento_del_corte(grafo, nodos_eliminar):
    # Crear una copia del grafo original
    grafo_acondicionado = {nodo: vecinos[:] for nodo, vecinos in grafo.items()}
    
    # Eliminar los nodos especificados y sus conexiones
    for nodo in nodos_eliminar:
        if nodo in grafo_acondicionado:
            del grafo_acondicionado[nodo]
        for vecinos in grafo_acondicionado.values():
            if nodo in vecinos:
                vecinos.remove(nodo)
    
    return grafo_acondicionado

# Ejemplo de uso eliminando los nodos 'C' y 'E'
nodos_a_eliminar = ['C', 'E']
grafo_acondicionado = acondicionamiento_del_corte(grafo, nodos_a_eliminar)
print("Grafo después del acondicionamiento del corte:", grafo_acondicionado)
