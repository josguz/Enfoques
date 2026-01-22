
import random

# Definición de probabilidades condicionales
prob_lluvia = 0.3
prob_sprinkler_dado_lluvia = 0.1
prob_sprinkler_dado_no_lluvia = 0.5

# Función para realizar ponderación de verosimilitud
def ponderacion_verosimilitud(condicion, muestras=1000):
    resultados = []
    for _ in range(muestras):
        lluvia = 'Lluvia' if random.random() < prob_lluvia else 'No Lluvia'
        peso = prob_lluvia if lluvia == condicion else (1 - prob_lluvia)
        sprinkler = 'Sprinkler' if random.random() < (prob_sprinkler_dado_lluvia if lluvia == 'Lluvia' else prob_sprinkler_dado_no_lluvia) else 'No Sprinkler'
        
        # Guardar la muestra y su peso
        resultados.append((sprinkler, peso))
    return resultados

# Ejemplo de uso
muestras_ponderadas = ponderacion_verosimilitud('Lluvia', muestras=5)
print("Muestras con ponderación de verosimilitud:", muestras_ponderadas)
