
import random

# Definición de los estados, acciones, transiciones y recompensas
estados = ['A', 'B', 'C']
acciones = ['Mover', 'Esperar']
observaciones = ['Obs_A', 'Obs_B', 'Obs_C']
transiciones = {
    'A': {'Mover': {'B': 0.8, 'A': 0.2}, 'Esperar': {'A': 1.0}},
    'B': {'Mover': {'C': 0.9, 'B': 0.1}, 'Esperar': {'B': 1.0}},
    'C': {'Esperar': {'C': 1.0}}
}
recompensas = {'A': 0, 'B': 1, 'C': 10}
observacion_prob = {
    'A': {'Obs_A': 0.7, 'Obs_B': 0.2, 'Obs_C': 0.1},
    'B': {'Obs_A': 0.1, 'Obs_B': 0.7, 'Obs_C': 0.2},
    'C': {'Obs_A': 0.2, 'Obs_B': 0.1, 'Obs_C': 0.7}
}

# Parámetros
gamma = 0.9
iteraciones = 5

# Creencias iniciales (probabilidades de estar en cada estado)
creencias = {estado: 1 / len(estados) for estado in estados}

# Actualización de creencias basadas en observación
def actualizar_creencias(observacion):
    for estado in estados:
        creencias[estado] *= observacion_prob[estado][observacion]
    normalizar_creencias()

# Normalización de las creencias
def normalizar_creencias():
    suma = sum(creencias.values())
    for estado in creencias:
        creencias[estado] /= suma

# Cálculo del valor esperado basado en las creencias actuales
def valor_esperado():
    return sum(creencias[estado] * recompensas[estado] for estado in estados)

# Simulación POMDP con actualización de creencias y valor esperado
def pomdp():
    for i in range(iteraciones):
        observacion = random.choices(observaciones, k=1)[0]
        print(f"Iteración {i+1}, Observación: {observacion}")
        actualizar_creencias(observacion)
        print("Creencias:", creencias)
        print("Valor esperado:", valor_esperado())

# Ejemplo de uso
pomdp()
