
# Definición de nodos de decisión, probabilidad y utilidad
opciones = {
    "Opción 1": {"probabilidad": 0.7, "utilidad": 100},
    "Opción 2": {"probabilidad": 0.5, "utilidad": 150},
    "Opción 3": {"probabilidad": 0.3, "utilidad": 200}
}

# Función para calcular el valor esperado de cada opción
def calcular_valor_esperado(opcion):
    probabilidad = opcion["probabilidad"]
    utilidad = opcion["utilidad"]
    return probabilidad * utilidad

# Función para evaluar las opciones y decidir la mejor
def mejor_opcion(opciones):
    valores_esperados = {nombre: calcular_valor_esperado(opcion) for nombre, opcion in opciones.items()}
    mejor = max(valores_esperados, key=valores_esperados.get)
    return mejor, valores_esperados

# Ejemplo de uso
mejor, valores = mejor_opcion(opciones)
print("Valor esperado de cada opción:", valores)
print("La mejor opción es:", mejor)
