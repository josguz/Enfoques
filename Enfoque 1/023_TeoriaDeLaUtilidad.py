
# Definición de las opciones con sus respectivos beneficios y probabilidades
opciones = {
    "Opción 1": {"beneficio": 100, "probabilidad": 0.8},
    "Opción 2": {"beneficio": 150, "probabilidad": 0.6},
    "Opción 3": {"beneficio": 200, "probabilidad": 0.4}
}

# Función de utilidad para calcular el valor esperado
def calcular_utilidad(beneficio, probabilidad, coeficiente_riesgo=0.5):
    utilidad = probabilidad * (beneficio ** coeficiente_riesgo)
    return utilidad

# Evaluar cada opción según la función de utilidad
def evaluar_opciones(opciones, coeficiente_riesgo=0.5):
    utilidades = {}
    for opcion, valores in opciones.items():
        beneficio = valores["beneficio"]
        probabilidad = valores["probabilidad"]
        utilidades[opcion] = calcular_utilidad(beneficio, probabilidad, coeficiente_riesgo)
    return utilidades

# Ejemplo de uso con un coeficiente de riesgo moderado
utilidades = evaluar_opciones(opciones, coeficiente_riesgo=0.5)
print("Utilidades de cada opción:", utilidades)
