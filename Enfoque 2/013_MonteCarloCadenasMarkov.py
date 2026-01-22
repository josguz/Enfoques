
import random

# Definición de los estados y las probabilidades de transición
estados = ['A', 'B', 'C']
transiciones = {
    'A': {'A': 0.2, 'B': 0.5, 'C': 0.3},
    'B': {'A': 0.1, 'B': 0.6, 'C': 0.3},
    'C': {'A': 0.3, 'B': 0.4, 'C': 0.3}
}

# Función para simular la cadena de Markov usando Monte Carlo
def monte_carlo_markov(estado_inicial, pasos):
    estado_actual = estado_inicial
    trayectoria = [estado_actual]
    
    for _ in range(pasos):
        siguiente_estado = random.choices(
            population=list(transiciones[estado_actual].keys()),
            weights=list(transiciones[estado_actual].values())
        )[0]
        trayectoria.append(siguiente_estado)
        estado_actual = siguiente_estado
        
    return trayectoria

# Ejemplo de uso
trayectoria_simulada = monte_carlo_markov('A', 10)
print("Trayectoria simulada de la cadena de Markov:", trayectoria_simulada)
