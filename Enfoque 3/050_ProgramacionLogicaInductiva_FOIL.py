
class FOIL:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def induce(self, examples):
        # Suponiendo que cada ejemplo es una tupla (premisa, conclusión)
        for premise, conclusion in examples:
            if premise not in self.rules:
                self.add_rule((premise, conclusion))
        return self.rules


# Crear un sistema FOIL
foil_system = FOIL()
examples = [
    ("El cielo es azul", "Es de día"),
    ("Está lloviendo", "No es de día"),
]

# Inducir reglas
induced_rules = foil_system.induce(examples)

# Mostrar reglas inducidas
for rule in induced_rules:
    print(f"Regla inducida: {rule[0]} => {rule[1]}")
