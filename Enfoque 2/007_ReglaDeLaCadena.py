
# Probabilidades individuales y condicionales
probabilidad_A = 0.6                 # P(A)
probabilidad_B_dado_A = 0.7          # P(B|A)
probabilidad_C_dado_A_B = 0.9        # P(C|A, B)

# Aplicación de la regla de la cadena P(A, B, C) = P(A) * P(B|A) * P(C|A, B)
def probabilidad_conjunta():
    prob_conjunta = probabilidad_A * probabilidad_B_dado_A * probabilidad_C_dado_A_B
    return prob_conjunta

# Ejemplo de uso
resultado = probabilidad_conjunta()
print("Probabilidad conjunta de P(A, B, C):", resultado)
