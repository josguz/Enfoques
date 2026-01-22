
import random

# Definición de las opciones (por simplicidad, cada opción tiene una recompensa aleatoria)
opciones = ['Opción 1', 'Opción 2', 'Opción 3']
recompensas_opciones = {opcion: random.randint(1, 10) for opcion in opciones}

# Parámetros
epsilon = 0.1   # Probabilidad de exploración
aprendizaje = 0.5   # Tasa de aprendizaje

# Inicialización de valores Q para cada opción
q_valores = {opcion: 0 for opcion in opciones}

# Función para seleccionar una opción con política epsilon-greedy
def seleccionar_opcion():
    if random.random() < epsilon:
        return random.choice(opciones)  # Explora una opción aleatoria
    else:
        return max(opciones, key=lambda opcion: q_valores[opcion])  # Explota la mejor opción

# Función para ejecutar episodios de exploración vs. explotación
def ejecutar_exploracion_explotacion(episodios=100):
    for _ in range(episodios):
        opcion = seleccionar_opcion()
        recompensa = recompensas_opciones[opcion]
        # Actualizar el valor Q usando la recompensa obtenida
        q_valores[opcion] += aprendizaje * (recompensa - q_valores[opcion])

# Ejemplo de uso
ejecutar_exploracion_explotacion()
print("Valores Q después del aprendizaje:", q_valores)
