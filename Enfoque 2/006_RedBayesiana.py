
# Probabilidades a priori
prob_lluvia = 0.2
prob_sprinkler_dado_lluvia = 0.01
prob_sprinkler_dado_no_lluvia = 0.4

# Probabilidades condicionadas
prob_cesped_mojado_dado_lluvia_sprinkler = 0.99
prob_cesped_mojado_dado_lluvia_no_sprinkler = 0.8
prob_cesped_mojado_dado_no_lluvia_sprinkler = 0.9
prob_cesped_mojado_dado_no_lluvia_no_sprinkler = 0.0

# Función para calcular la probabilidad de césped mojado
def probabilidad_cesped_mojado():
    prob_no_lluvia = 1 - prob_lluvia
    prob_sprinkler = prob_sprinkler_dado_lluvia * prob_lluvia + prob_sprinkler_dado_no_lluvia * prob_no_lluvia
    
    prob_cesped_mojado = (
        prob_cesped_mojado_dado_lluvia_sprinkler * prob_lluvia * prob_sprinkler_dado_lluvia +
        prob_cesped_mojado_dado_lluvia_no_sprinkler * prob_lluvia * (1 - prob_sprinkler_dado_lluvia) +
        prob_cesped_mojado_dado_no_lluvia_sprinkler * prob_no_lluvia * prob_sprinkler_dado_no_lluvia +
        prob_cesped_mojado_dado_no_lluvia_no_sprinkler * prob_no_lluvia * (1 - prob_sprinkler_dado_no_lluvia)
    )
    
    return prob_cesped_mojado

# Ejemplo de uso
resultado = probabilidad_cesped_mojado()
print("Probabilidad de que el césped esté mojado:", resultado)
