
# Probabilidades de transición y emisión para el modelo
transiciones = {'Soleado': {'Soleado': 0.8, 'Lluvioso': 0.2}, 'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}}
emisiones = {'Soleado': {'Cálido': 0.7, 'Frío': 0.3}, 'Lluvioso': {'Cálido': 0.4, 'Frío': 0.6}}
estados = ['Soleado', 'Lluvioso']
observaciones = ['Cálido', 'Frío', 'Cálido']

# Paso hacia adelante
def hacia_delante(observaciones):
    alfa = [{}]
    for estado in estados:
        alfa[0][estado] = emisiones[estado][observaciones[0]] * 0.5  # Asumiendo probabilidad inicial uniforme
    
    for t in range(1, len(observaciones)):
        alfa.append({})
        for estado in estados:
            alfa[t][estado] = sum(alfa[t-1][prev] * transiciones[prev][estado] * emisiones[estado][observaciones[t]] for prev in estados)
    return alfa

# Paso hacia atrás
def hacia_atras(observaciones):
    beta = [{} for _ in range(len(observaciones))]
    for estado in estados:
        beta[-1][estado] = 1  # Inicialización
    
    for t in range(len(observaciones) - 2, -1, -1):
        for estado in estados:
            beta[t][estado] = sum(transiciones[estado][next_state] * emisiones[next_state][observaciones[t+1]] * beta[t+1][next_state] for next_state in estados)
    return beta

# Ejemplo de uso
alfa = hacia_delante(observaciones)
beta = hacia_atras(observaciones)
print("Probabilidades hacia adelante:", alfa)
print("Probabilidades hacia atrás:", beta)
