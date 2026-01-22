
# Definición de los estados, acciones, recompensas y transiciones
estados = ['A', 'B', 'C', 'D']
acciones = ['Izquierda', 'Derecha']
transiciones = {
    'A': {'Izquierda': ('B', 0.8), 'Derecha': ('C', 0.2)},
    'B': {'Izquierda': ('A', 1.0), 'Derecha': ('D', 0.9)},
    'C': {'Izquierda': ('A', 0.5), 'Derecha': ('D', 0.5)},
    'D': {'Izquierda': ('B', 1.0), 'Derecha': ('C', 1.0)}
}
recompensas = {'A': 0, 'B': 1, 'C': -1, 'D': 5}
# Parámetros
gamma = 0.9  # Factor de descuento
iteraciones = 10
# Inicialización de valores y política
valores = {estado: 0 for estado in estados}
politica = {estado: 'Izquierda' for estado in estados}

# Evaluación de la política
def evaluar_politica():
    for _ in range(iteraciones):
        nuevos_valores = valores.copy()
        for estado in estados:
            accion = politica[estado]
            siguiente_estado, prob = transiciones[estado][accion]
            nuevos_valores[estado] = recompensas[siguiente_estado] + gamma * prob * valores[siguiente_estado]
        valores.update(nuevos_valores)

# Mejora de la política
def mejorar_politica():
    for estado in estados:
        valor_accion = {}
        for accion in acciones:
            siguiente_estado, prob = transiciones[estado][accion]
            valor_accion[accion] = recompensas[siguiente_estado] + gamma * prob * valores[siguiente_estado]
        politica[estado] = max(valor_accion, key=valor_accion.get)

# Búsqueda de la política óptima
def busqueda_de_la_politica():
    for _ in range(iteraciones):
        evaluar_politica()
        mejorar_politica()
    return politica
# Ejemplo de uso

politica_optima = busqueda_de_la_politica()
print("Política óptima encontrada:", politica_optima)
