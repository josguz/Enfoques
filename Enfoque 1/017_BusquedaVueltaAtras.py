
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

# Función para verificar si el color asignado es válido
def es_valida(asignacion, nodo, color):
    for vecino in grafo[nodo]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

# Algoritmo de vuelta atrás para resolver el problema de coloración
def vuelta_atras(asignacion={}):
    if len(asignacion) == len(nodos):
        return asignacion

    nodo = [n for n in nodos if n not in asignacion][0]
    for color in colores:
        if es_valida(asignacion, nodo, color):
            asignacion[nodo] = color
            resultado = vuelta_atras(asignacion)
            if resultado:
                return resultado
            asignacion.pop(nodo)

# Ejemplo de uso
solucion = vuelta_atras()
print("Solución encontrada:", solucion)
