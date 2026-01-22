
# Definición de probabilidades conjuntas de ejemplo
probabilidades = {
    ('A', 'B', 'C'): 0.15,
    ('A', 'B', '¬C'): 0.05,
    ('A', '¬B', 'C'): 0.25,
    ('A', '¬B', '¬C'): 0.1,
    ('¬A', 'B', 'C'): 0.05,
    ('¬A', 'B', '¬C'): 0.1,
    ('¬A', '¬B', 'C'): 0.2,
    ('¬A', '¬B', '¬C'): 0.1
}

# Eliminación de la variable C para obtener la probabilidad conjunta de A y B
def eliminacion_de_variables():
    probabilidad_ab = {}
    for (a, b, c), prob in probabilidades.items():
        if (a, b) not in probabilidad_ab:
            probabilidad_ab[(a, b)] = 0
        probabilidad_ab[(a, b)] += prob  # Sumar sobre la variable C eliminada
    return probabilidad_ab

# Ejemplo de uso
resultado = eliminacion_de_variables()
print("Probabilidad conjunta de A y B después de eliminar C:", resultado)
