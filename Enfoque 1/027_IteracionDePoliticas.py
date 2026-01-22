
# Definición de los estados, acciones, transiciones y recompensas
estados = ['A', 'B', 'C']
acciones = ['Mover', 'Esperar']
transiciones = {
    'A': {'Mover': {'B': 0.8, 'A': 0.2}, 'Esperar': {'A': 1.0}},
    'B': {'Mover': {'C': 0.9, 'B': 0.1}, 'Esperar': {'B': 1.0}},
    'C': {'Esperar': {'C': 1.0}}
}
recompensas = {'A': 0, 'B': 1, 'C': 10}

# Parámetros
gamma = 0.9  # Factor de descuento
iteraciones = 10

# Inicialización de valores y política
valores = {estado: 0 for estado in estados}
politica = {estado: 'Esperar' for estado in estados}

# Evaluación de política
def evaluar_politica():
    for _ in range(iteraciones):
        nuevos_valores = valores.copy()
        for estado in estados:
            accion = politica[estado]
            if accion in transiciones[estado]:
                nuevos_valores[estado] = sum(
                    prob * (recompensas[siguiente] + gamma * valores[siguiente])
                    for siguiente, prob in transiciones[estado][accion].items()
                )
        return nuevos_valores

# Mejoramiento de política
def mejorar_politica():
    for estado in estados:
        valores_accion = {}
        for accion in acciones:
            if accion in transiciones[estado]:
                valores_accion[accion] = sum(
                    prob * (recompensas[siguiente] + gamma * valores[siguiente])
                    for siguiente, prob in transiciones[estado][accion].items()
                )
        politica[estado] = max(valores_accion, key=valores_accion.get)

# Iteración de políticas
def iteracion_de_politicas():
    global valores
    for _ in range(iteraciones):
        valores = evaluar_politica()
        mejorar_politica()
    return politica
    
# Ejemplo de uso
politica_optima = iteracion_de_politicas()
print("Política óptima encontrada:", politica_optima)

