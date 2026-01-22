
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

# Verifica si la asignación de color es válida
def es_valida(nodo, color, asignacion):
    for vecino in grafo[nodo]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

# Algoritmo de salto atrás con detección de conflictos
def salto_atras(asignacion={}, conflictos=[]):
    if len(asignacion) == len(nodos):
        return asignacion

    nodo = [n for n in nodos if n not in asignacion][0]
    for color in colores:
        if es_valida(nodo, color, asignacion):
            asignacion[nodo] = color
            resultado = salto_atras(asignacion, conflictos)
            if resultado:
                return resultado
            asignacion.pop(nodo)
        else:
            conflictos.append(nodo)  # Registrar el conflicto

    # Saltar atrás al nodo de conflicto más reciente
    if conflictos:
        ultimo_conflicto = conflictos.pop()
        if ultimo_conflicto in asignacion:
            asignacion.pop(ultimo_conflicto)

# Ejemplo de uso
solucion = salto_atras()
print("Solución encontrada:", solucion)
