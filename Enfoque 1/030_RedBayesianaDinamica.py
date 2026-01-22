# Definición de estados y probabilidad de transición
estados = ['Soleado', 'Lluvioso']
transiciones = {
    'Soleado': {'Soleado': 0.8, 'Lluvioso': 0.2},
    'Lluvioso': {'Soleado': 0.3, 'Lluvioso': 0.7}
}
evidencias = {
    'Soleado': {'Agradable': 0.9, 'Desagradable': 0.1},
    'Lluvioso': {'Agradable': 0.2, 'Desagradable': 0.8}
}
# Inicialización de las creencias
creencias = {'Soleado': 0.5, 'Lluvioso': 0.5}

# Actualización de creencias basado en la observación
def actualizar_creencias(observacion):
    nuevas_creencias = {}
    for estado in estados:
        prob_evidencia = evidencias[estado][observacion]
        nuevas_creencias[estado] = prob_evidencia * sum(
            transiciones[previo][estado] * creencias[previo] for previo in estados)
    
    # Normalizar creencias
    normalizar(nuevas_creencias)
    return nuevas_creencias

# Normalización de probabilidades
def normalizar(distribucion):
    total = sum(distribucion.values())
    for key in distribucion:
        distribucion[key] /= total

# Simulación de la red bayesiana dinámica
def red_bayesiana_dinamica(observaciones):
    global creencias
    for observacion in observaciones:
        print(f"Observación: {observacion}")
        creencias = actualizar_creencias(observacion)
        print("Creencias actualizadas:", creencias)

# Ejemplo de uso con una secuencia de observaciones
observaciones = ['Agradable', 'Desagradable', 'Agradable']
red_bayesiana_dinamica(observaciones)
