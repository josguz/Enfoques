
# Función para unificar dos términos
def unify(term1, term2):
    if term1 == term2:
        return {}
    elif isinstance(term1, str) and term1.islower():  # Variable
        return {term1: term2}
    elif isinstance(term2, str) and term2.islower():  # Variable
        return {term2: term1}
    return None  # No se puede unificar

# Ejemplo de uso
term_a = 'X'
term_b = 'John'


# Intentar unificar
result = unify(term_a, term_b)
if result is not None:
    print("Unificación exitosa:", result)
else:
    print("No se puede unificar.")
