
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

# Función para aplicar el algoritmo de propagación de restricciones (AC-3)
def ac3(dominio):
    cola = [(nodo, vecino) for nodo in grafo for vecino in grafo[nodo]]
    
    while cola:
        nodo, vecino = cola.pop(0)
        if revisar_arco(dominio, nodo, vecino):
            if not dominio[nodo]:
                return False  # Fallo si el dominio está vacío
            for otro_vecino in grafo[nodo]:
                if otro_vecino != vecino:
                    cola.append((otro_vecino, nodo))
    
    return True

# Revisa y ajusta el dominio para que sea consistente entre nodos adyacentes
def revisar_arco(dominio, nodo, vecino):
    eliminado = False
    for color in dominio[nodo][:]:
        if all(color == vecino_color for vecino_color in dominio[vecino]):
            dominio[nodo].remove(color)
            eliminado = True
    return eliminado

# Algoritmo de coloración con propagación de restricciones
def coloracion_con_ac3():
    dominio = {nodo: list(colores) for nodo in nodos}
    if ac3(dominio):
        return dominio
    else:
        return None

# Ejemplo de uso
solucion = coloracion_con_ac3()
print("Solución con propagación de restricciones:", solucion)
