
import random

# Definición de nodos y colores
nodos = ['A', 'B', 'C', 'D']
colores = ['Rojo', 'Verde', 'Azul']

# Grafo con conexiones entre nodos (adyacencias)
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Función para contar el número de conflictos de un nodo
def contar_conflictos(nodo, color, asignacion):
    return sum(1 for vecino in grafo[nodo] if asignacion.get(vecino) == color)

# Algoritmo de mínimos-conflictos
def minimos_conflictos(iteraciones=1000):
    # Asignación inicial aleatoria
    asignacion = {nodo: random.choice(colores) for nodo in nodos}
    
    for _ in range(iteraciones):
        # Verificar si se ha resuelto el problema sin conflictos
        conflictos = [(nodo, color) for nodo, color in asignacion.items() if contar_conflictos(nodo, color, asignacion) > 0]
        if not conflictos:
            return asignacion
        
        # Elegir un nodo con conflictos y cambiarlo al color con menos conflictos
        nodo, _ = random.choice(conflictos)
        mejor_color = min(colores, key=lambda color: contar_conflictos(nodo, color, asignacion))
        asignacion[nodo] = mejor_color
    
    return None  # Si no se encuentra solución en el número de iteraciones

# Ejemplo de uso
solucion = minimos_conflictos()
print("Solución encontrada:", solucion)
