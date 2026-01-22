
# Definición de las probabilidades de transición y emisión para el modelo oculto de Markov
transiciones = {'Soleado': {'Soleado': 0.7, 'Lluvioso': 0.3}, 'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}}
emisiones = {'Soleado': {'Cálido': 0.6, 'Frío': 0.4}, 'Lluvioso': {'Cálido': 0.3, 'Frío': 0.7}}
estados = ['Soleado', 'Lluvioso']
observaciones = ['Cálido', 'Frío', 'Cálido']

# Implementación del algoritmo hacia adelante para calcular probabilidades de estado
def algoritmo_hacia_delante(observaciones):
    alfa = [{}]
    for estado in estados:
        alfa[0][estado] = emisiones[estado][observaciones[0]] * 0.5  # Probabilidad inicial uniforme
    
    for t in range(1, len(observaciones)):
        alfa.append({})
        for estado in estados:
            alfa[t][estado] = sum(alfa[t-1][prev] * transiciones[prev][estado] * emisiones[estado][observaciones[t]] for prev in estados)
    return alfa

# Ejemplo de uso
alfa = algoritmo_hacia_delante(observaciones)
print("Probabilidades hacia adelante en HMM:", alfa)
