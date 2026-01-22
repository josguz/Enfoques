
class CausalGrammar:
    def __init__(self):
        self.rules = {}

    def add_rule(self, cause, effect):
        self.rules[cause] = effect

    def explain(self, cause):
        return self.rules.get(cause, "No hay efecto definido para esta causa.")

# Crear una gramática causal
grammar = CausalGrammar()
grammar.add_rule("Fumar", "Cáncer de pulmón")
grammar.add_rule("Comer saludable", "Buena salud")
grammar.add_rule("Ejercicio regular", "Menor riesgo de enfermedades")

# Explicar efectos basados en causas
print("Efecto de fumar:", grammar.explain("Fumar"))
print("Efecto de comer saludable:", grammar.explain("Comer saludable"))
print("Efecto de no hacer ejercicio:", grammar.explain("No hacer ejercicio"))  # Sin efecto definido
