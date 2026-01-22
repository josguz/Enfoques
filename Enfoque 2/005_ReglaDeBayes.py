
# Probabilidades iniciales (prior, likelihood y evidencia)
prob_prior = 0.01          # P(C) - Probabilidad de que una persona esté enferma
prob_sintoma_dado_c = 0.8  # P(S|C) - Probabilidad de presentar un síntoma dado que está enferma
prob_sintoma = 0.05        # P(S) - Probabilidad de presentar el síntoma en general

# Aplicación de la Regla de Bayes
def probabilidad_posterior():
    prob_posterior = (prob_sintoma_dado_c * prob_prior) / prob_sintoma
    return prob_posterior

# Ejemplo de uso
posterior = probabilidad_posterior()
print("Probabilidad posterior de estar enfermo dado el síntoma:", posterior)
