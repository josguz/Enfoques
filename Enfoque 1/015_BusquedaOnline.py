
import random

# Representación del grafo como un diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def busqueda_online(grafo, inicio, objetivo):
    nodo_actual = inicio
    visitados = set()
    
    while nodo_actual != objetivo:
        print(f"Nodo actual: {nodo_actual}")
        visitados.add(nodo_actual)
        
        # Escoge un vecino no visitado al azar
        vecinos_no_visitados = [vecino for vecino in grafo[nodo_actual] if vecino not in visitados]
        
        if vecinos_no_visitados:
            nodo_actual = random.choice(vecinos_no_visitados)
        else:
            print("No hay vecinos no visitados. Terminando búsqueda.")
            return False
        
    print("Objetivo encontrado!")
    return True

# Ejemplo de uso
busqueda_online(grafo, 'A', 'F')
