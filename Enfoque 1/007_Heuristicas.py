
import math

# Representación del grafo como coordenadas de cada nodo
coordenadas = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (4, 0),
    'D': (6, 1),
    'E': (3, 4),
    'F': (5, 5)
}

def heuristica_euclidiana(nodo1, nodo2):
    # Obtener las coordenadas de los nodos
    x1, y1 = coordenadas[nodo1]
    x2, y2 = coordenadas[nodo2]
    
    # Calcular la distancia euclidiana
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

# Ejemplo de uso de la heurística

inicio = 'A'
objetivo = 'F'
print(f"Distancia heurística entre '{inicio}' y '{objetivo}': {heuristica_euclidiana(inicio, objetivo):.2f}")
