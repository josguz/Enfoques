
import random

# Definición de los estados, acciones, recompensas y transiciones
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

# Inicialización de valores de estados
valores = {estado: 0 for estado in estados}

# Función de aprendizaje por refuerzo pasivo
def aprendizaje_refuerzo_pasivo(episodios=100):
    for _ in range(episodios):
        estado = random.choice(estados)  # Selecciona un estado inicial aleatorio
        while estado != 'D':  # Suponemos 'D' como estado terminal
            accion = random.choice(acciones)
            siguiente_estado = transiciones[estado][accion]
            recompensa = recompensas[siguiente_estado]
            # Actualización del valor del estado usando la fórmula de actualización
            valores[estado] += alpha * (recompensa + gamma * valores[siguiente_estado] - valores[estado])
            estado = siguiente_estado

# Ejemplo de uso
aprendizaje_refuerzo_pasivo()
print("Valores de los estados después del aprendizaje:", valores)
