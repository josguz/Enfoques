
import random

# Definición de probabilidades iniciales
prob_lluvia = 0.3
prob_sprinkler_dado_lluvia = 0.1
prob_sprinkler_dado_no_lluvia = 0.5

# Muestreo directo de la variable Sprinkler dado Lluvia
def muestreo_directo():
    if random.random() < prob_lluvia:
        return 'Lluvia', 'Sprinkler' if random.random() < prob_sprinkler_dado_lluvia else 'No Sprinkler'
    else:
        return 'No Lluvia', 'Sprinkler' if random.random() < prob_sprinkler_dado_no_lluvia else 'No Sprinkler'

# Muestreo por rechazo con la condición de que ocurra Lluvia
def muestreo_por_rechazo(condicion, muestras=1000):
    resultados = []
    for _ in range(muestras):
        muestra = muestreo_directo()
        if muestra[0] == condicion:
            resultados.append(muestra[1])
    return resultados

# Ejemplo de uso
muestras_directas = [muestreo_directo() for _ in range(5)]
muestras_rechazo = muestreo_por_rechazo('Lluvia', muestras=1000)
print("Muestras directas:", muestras_directas)
print("Muestras por rechazo dado Lluvia:", muestras_rechazo[:10])  # Mostrando las primeras 10 muestras
