
import random

# Definición de estados, acciones, recompensas y transiciones
estados = ['A', 'B', 'C', 'D']
acciones = ['Izquierda', 'Derecha']
recompensas = {'A': 0, 'B': 1, 'C': -1, 'D': 5}
transiciones = {
    'A': {'Izquierda': 'B', 'Derecha': 'C'},
    'B': {'Izquierda': 'A', 'Derecha': 'D'},
    'C': {'Izquierda': 'A', 'Derecha': 'D'},
    'D': {'Izquierda': 'B', 'Derecha': 'C'}
}

# Parámetros de aprendizaje
gamma = 0.9  # Factor de descuento
alpha = 0.1  # Tasa de aprendizaje
epsilon = 0.1  # Probabilidad de exploración

# Inicialización de valores Q
q_valores = {(estado, accion): 0 for estado in estados for accion in acciones}

# Función para seleccionar una acción con política epsilon-greedy
def seleccionar_accion(estado):
    if random.random() < epsilon:
        return random.choice(acciones)
    else:
        return max(acciones, key=lambda accion: q_valores[(estado, accion)])

# Aprendizaje por refuerzo activo
def aprendizaje_refuerzo_activo(episodios=100):
    for _ in range(episodios):
        estado = random.choice(estados)
        while estado != 'D':  # Suponemos 'D' como estado terminal
            accion = seleccionar_accion(estado)
            siguiente_estado = transiciones[estado][accion]
            recompensa = recompensas[siguiente_estado]
            # Actualización del valor Q usando la fórmula de actualización Q-learning
            q_valores[(estado, accion)] += alpha * (recompensa + gamma * max(q_valores[(siguiente_estado, a)] for a in acciones) - q_valores[(estado, accion)])
            estado = siguiente_estado

# Ejemplo de uso

aprendizaje_refuerzo_activo()
print("Valores Q después del aprendizaje:", q_valores)
