
# Definición de variables y dominios
variables = ['A', 'B', 'C']
dominios = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}

# Restricciones: valores distintos para cada variable
restricciones = {
    ('A', 'B'): lambda a, b: a != b,
    ('B', 'C'): lambda b, c: b != c,
    ('A', 'C'): lambda a, c: a != c
}

# Función para verificar si la asignación cumple todas las restricciones
def es_valida(asignacion):
    for (var1, var2), restriccion in restricciones.items():
        if var1 in asignacion and var2 in asignacion:
            if not restriccion(asignacion[var1], asignacion[var2]):
                return False
    return True

# Resolución mediante búsqueda en profundidad
def resolver_csp(asignacion={}):
    if len(asignacion) == len(variables):
        return asignacion

    var = [v for v in variables if v not in asignacion][0]
    for valor in dominios[var]:
        asignacion[var] = valor
        if es_valida(asignacion):
            resultado = resolver_csp(asignacion)
            if resultado:
                return resultado
        asignacion.pop(var)

# Ejemplo de uso
solucion = resolver_csp()
print("Solución encontrada:", solucion)
