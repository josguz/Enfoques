
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

# Función para comprobar si una asignación de color es válida
def es_valida(nodo, color, asignacion):
    for vecino in grafo[nodo]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

# Algoritmo de comprobación hacia adelante para el problema de coloración
def comprobacion_hacia_adelante(asignacion={}, dominio=None):
    if dominio is None:
        dominio = {nodo: list(colores) for nodo in nodos}
    
    if len(asignacion) == len(nodos):
        return asignacion
    
    nodo = [n for n in nodos if n not in asignacion][0]
    for color in dominio[nodo]:
        if es_valida(nodo, color, asignacion):
            asignacion[nodo] = color
            # Reducir el dominio de los vecinos
            nuevo_dominio = {n: d[:] for n, d in dominio.items()}
            for vecino in grafo[nodo]:
                if color in nuevo_dominio[vecino]:
                    nuevo_dominio[vecino].remove(color)
            
            resultado = comprobacion_hacia_adelante(asignacion, nuevo_dominio)
            if resultado:
                return resultado
            asignacion.pop(nodo)
    
    return None

# Ejemplo de uso
solucion = comprobacion_hacia_adelante()
print("Solución encontrada:", solucion)
