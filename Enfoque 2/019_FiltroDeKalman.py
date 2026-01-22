
import numpy as np

# Definición de los parámetros del Filtro de Kalman
estado = np.array([[0], [0]])  # Estado inicial: posición y velocidad
P = np.array([[1, 0], [0, 1]])  # Matriz de covarianza inicial
A = np.array([[1, 1], [0, 1]])  # Matriz de transición de estado
H = np.array([[1, 0]])  # Matriz de observación
Q = np.array([[0.1, 0], [0, 0.1]])  # Ruido de proceso
R = np.array([[1]])  # Ruido de observación

# Filtro de Kalman
def filtro_de_kalman(estado, P, observaciones):
    estimaciones = []
    for observacion in observaciones:
        # Predicción
        estado_priori = A @ estado
        P_priori = A @ P @ A.T + Q
        
        # Actualización
        K = P_priori @ H.T @ np.linalg.inv(H @ P_priori @ H.T + R)
        estado = estado_priori + K @ (observacion - H @ estado_priori)
        P = (np.eye(len(K)) - K @ H) @ P_priori
        
        estimaciones.append(estado[0, 0])  # Guardar posición estimada
    return estimaciones

# Generación de observaciones con ruido
np.random.seed(0)
observaciones = np.array([[i + np.random.normal(0, 1)] for i in range(10)])

# Ejemplo de uso
estimaciones = filtro_de_kalman(estado, P, observaciones)
print("Estimaciones de posición:", estimaciones)
