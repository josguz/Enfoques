
from collections import deque

# Grafo representado como un diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def busqueda_bidireccional(grafo, inicio, objetivo):
    # Colas para la búsqueda desde ambos extremos
    cola_inicio = deque([inicio])  # Desde el nodo inicial
    
    cola_objetivo = deque([objetivo])  # Desde el nodo objetivo
    
    # Conjuntos de nodos visitados
    visitados_inicio = {inicio}
    visitados_objetivo = {objetivo}
    
    # Realizar la búsqueda hasta que ambas colas se encuentren
    while cola_inicio and cola_objetivo:
        # Expansión desde el inicio
        if busqueda_nivel(cola_inicio, visitados_inicio, visitados_objetivo, grafo):
            print("Se encontraron los caminos desde ambos extremos.")
            return True
        
        # Expansión desde el objetivo
        if busqueda_nivel(cola_objetivo, visitados_objetivo, visitados_inicio, grafo):
            print("Se encontraron los caminos desde ambos extremos.")
            return True
    
    print("No hay camino que conecte el inicio y el objetivo.")
    return False

def busqueda_nivel(cola, visitados_origen, visitados_destino, grafo):
    # Sacamos el nodo actual de la cola
    nodo_actual = cola.popleft()
    
    # Revisamos todos los vecinos del nodo actual
    for vecino in grafo.get(nodo_actual, []):
        if vecino in visitados_destino:
            # Si el vecino ya ha sido visitado desde el otro extremo, encontramos el camino
            return True
        if vecino not in visitados_origen:
            # Marcar el vecino como visitado y agregarlo a la cola para futuras expansiones
            visitados_origen.add(vecino)
            cola.append(vecino)
    return False

# Ejemplo de uso para probar la búsqueda bidireccional
resultado = busqueda_bidireccional(grafo, 'A', 'F')
print("Resultado de la búsqueda:", resultado)
