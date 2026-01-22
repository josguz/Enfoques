
# Definición de las probabilidades y el manto de Markov
probabilidades = {
    'A': 0.3,
    'B': {'A': 0.5, 'C': 0.6},
    'C': 0.4,
    'D': {'B': 0.8, 'C': 0.7}
}

# Manto de Markov de B son sus vecinos directos A y C
manto_de_B = ['A', 'C']

# Verificar independencia condicional usando el manto
def es_independiente(variable, condicion):
    return condicion in manto_de_B

# Ejemplo de uso
variable_a_evaluar = 'D'
resultado = es_independiente('B', variable_a_evaluar)
print(f"¿La variable 'B' es independiente de '{variable_a_evaluar}' dado su manto?", resultado)
