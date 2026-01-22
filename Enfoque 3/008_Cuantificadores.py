
# Definir un conjunto de individuos
universo = ['Juan', 'Maria', 'Pedro']

# Definir un predicado
def es_estudiante(nombre):
    return nombre in ['Juan', 'Maria']  # Juan y Maria son estudiantes


# Cuantificadores
def cuantificador_existencial():
    for persona in universo:
        if es_estudiante(persona):
            return f"Existen estudiantes: {persona}"
    return "No hay estudiantes."

def cuantificador_universal():
    for persona in universo:
        if not es_estudiante(persona):
            return f"No todos son estudiantes: {persona} no es estudiante."
    return "Todos son estudiantes."

# Evaluar los cuantificadores
print(cuantificador_existencial())
print(cuantificador_universal())
