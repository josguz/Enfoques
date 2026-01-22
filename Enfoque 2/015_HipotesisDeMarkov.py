
import random

# Definición de los estados y las probabilidades de transición de primer orden (Markov)
estados = ['Soleado', 'Nublado', 'Lluvioso']
transiciones = {
    'Soleado': {'Soleado': 0.7, 'Nublado': 0.2, 'Lluvioso': 0.1},
    'Nublado': {'Soleado': 0.3, 'Nublado': 0.4, 'Lluvioso': 0.3},
    'Lluvioso': {'Soleado': 0.2, 'Nublado': 0.3, 'Lluvioso': 0.5}
}

# Función para simular el proceso de Markov usando la hipótesis de primer orden
def proceso_markov(estado_inicial, pasos):
    estado_actual = estado_inicial
    secuencia = [estado_actual]
    
    for _ in range(pasos):
        siguiente_estado = random.choices(
            population=list(transiciones[estado_actual].keys()),
            weights=list(transiciones[estado_actual].values())
        )[0]
        secuencia.append(siguiente_estado)
        estado_actual = siguiente_estado
        
    return secuencia

# Ejemplo de uso
secuencia_simulada = proceso_markov('Soleado', 10)
print("Secuencia simulada del proceso de Markov:", secuencia_simulada)
