
# Probabilidades conjuntas y marginales de ejemplo
prob_conjunta = {
    ('sol', 'verano'): 0.3,
    ('sol', 'invierno'): 0.1,
    ('lluvia', 'verano'): 0.15,
    ('lluvia', 'invierno'): 0.25,
    ('nieve', 'verano'): 0.05,
    ('nieve', 'invierno'): 0.15
}
prob_marginal_estacion = {'verano': 0.5, 'invierno': 0.5}
prob_marginal_clima = {'sol': 0.4, 'lluvia': 0.4, 'nieve': 0.2}

# Función para verificar independencia condicional P(A | B) = P(A)
def verificar_independencia_condicional(evento, condicion):
    prob_evento_condicion = prob_conjunta[(evento, condicion)] / prob_marginal_estacion[condicion]
    prob_evento = prob_marginal_clima[evento]
    return prob_evento_condicion == prob_evento

# Ejemplo de uso
evento = 'sol'
condicion = 'verano'
independencia = verificar_independencia_condicional(evento, condicion)
print(f"¿'{evento}' es independiente de '{condicion}'?", independencia)
