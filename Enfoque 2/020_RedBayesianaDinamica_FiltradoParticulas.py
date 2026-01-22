
import numpy as np

# Inicialización de partículas y pesos
num_particulas = 1000
particulas = np.random.uniform(-10, 10, num_particulas)
pesos = np.ones(num_particulas) / num_particulas

# Simulación de movimiento y observación con ruido
def evolucion_estado(particulas):
    return particulas + np.random.normal(0, 1, num_particulas)

def peso_observacion(particulas, observacion):
    return np.exp(-0.5 * (observacion - particulas)**2)

# Filtrado de Partículas
def filtrado_de_particulas(observaciones):
    estimaciones = []
    global particulas, pesos
    for observacion in observaciones:
        particulas = evolucion_estado(particulas)
        pesos *= peso_observacion(particulas, observacion)
        pesos /= np.sum(pesos)  # Normalización de pesos
        indices = np.random.choice(range(num_particulas), size=num_particulas, p=pesos)
        particulas = particulas[indices]
        pesos = np.ones(num_particulas) / num_particulas
        estimaciones.append(np.mean(particulas))
    return estimaciones

# Generación de observaciones con ruido
np.random.seed(0)
observaciones = np.linspace(0, 10, 20) + np.random.normal(0, 1, 20)

# Ejemplo de uso
estimaciones = filtrado_de_particulas(observaciones)
print("Estimaciones de posición con Filtrado de Partículas:", estimaciones)
