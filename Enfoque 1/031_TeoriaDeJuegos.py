
import numpy as np

# Definición de las estrategias y las matrices de pagos para los jugadores
estrategias = ['A', 'B']
pagos_jugador1 = np.array([[3, 1], [0, 2]])  # Matriz de pagos para el Jugador 1
pagos_jugador2 = np.array([[2, 0], [3, 1]])  # Matriz de pagos para el Jugador 2

# Función para encontrar el equilibrio de Nash
def equilibrio_nash(pagos1, pagos2):
    equilibrios = []
    for i in range(len(estrategias)):
        for j in range(len(estrategias)):
            if (pagos1[i, j] >= pagos1[i, 1 - j]) and (pagos2[i, j] >= pagos2[1 - i, j]):
                equilibrios.append((estrategias[i], estrategias[j]))
    return equilibrios

# Ejemplo de uso
equilibrios = equilibrio_nash(pagos_jugador1, pagos_jugador2)
print("Equilibrios de Nash encontrados:", equilibrios)
