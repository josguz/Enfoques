
class GrammaticalInduction:
    def __init__(self):
        self.examples = []

    def add_example(self, example):
        self.examples.append(example)

    def induce_grammar(self):
        if not self.examples:
            return "No hay ejemplos para inducir gramática."
        
        # Simulación de inducción de gramática (simplificada)
        induced_rules = {}
        for example in self.examples:
            for symbol in example:
                if symbol not in induced_rules:
                    induced_rules[symbol] = example

        return induced_rules

# Crear un sistema de inducción gramatical
induction_system = GrammaticalInduction()
induction_system.add_example("ab")
induction_system.add_example("aa")
induction_system.add_example("bb")

# Inducir gramática
induced_grammar = induction_system.induce_grammar()
print("Reglas de gramática inducida:", induced_grammar)
