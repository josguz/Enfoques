

# Definición de una proposición en forma normal prenex
def skolemize(formula):
    # Aquí simplemente se representa un proceso simplificado de skolemización
    return formula.replace("∀", "Skolem_").replace("∃", "Skolem_")

# Ejemplo de proposición
formula = "∀x (P(x) → ∃y Q(x, y))"
print("Fórmula original:", formula)

# Realizar skolemización
skolemized_formula = skolemize(formula)
print("Fórmula Skolemizada:", skolemized_formula)
