
# Conjunto de datos: eventos y sus probabilidades condicionales
eventos = {
    'sol': {'verano': 0.8, 'invierno': 0.2},
    'lluvia': {'verano': 0.1, 'invierno': 0.6},
    'nieve': {'verano': 0.1, 'invierno': 0.2}
}

# Probabilidades a priori de las estaciones
probabilidad_estaciones = {'verano': 0.5, 'invierno': 0.5}

# Cálculo de la probabilidad condicionada y normalización
def probabilidad_condicionada_normalizacion(evento, estacion):
    if evento in eventos and estacion in probabilidad_estaciones:
        prob_cond = eventos[evento][estacion] * probabilidad_estaciones[estacion]
        prob_total = sum(eventos[ev][estacion] * probabilidad_estaciones[estacion] for ev in eventos)
        return prob_cond / prob_total  # Normalización
    else:
        return None

# Ejemplo de uso
evento = 'sol'
estacion = 'invierno'
prob_cond_normalizada = probabilidad_condicionada_normalizacion(evento, estacion)
print(f"Probabilidad condicionada y normalizada de '{evento}' dado '{estacion}':", prob_cond_normalizada)
