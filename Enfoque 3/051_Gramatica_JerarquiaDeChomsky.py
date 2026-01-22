
class Grammar:
    def __init__(self, name, production_rules):
        self.name = name
        self.production_rules = production_rules

    def describe(self):
        print(f"Gramática: {self.name}")
        print("Reglas de producción:")
        for rule in self.production_rules:
            print(f"  {rule}")

# Gramáticas de la jerarquía de Chomsky
regular_grammar = Grammar("Gramática Regular", ["A -> aB", "B -> b"])
context_free_grammar = Grammar("Gramática Libre de Contexto", ["S -> AB", "A -> a", "B -> b"])
context_sensitive_grammar = Grammar("Gramática Sensible al Contexto", ["AB -> aC", "C -> c"])
recursively_enumerable_grammar = Grammar("Gramática Enumerablemente Recursiva", ["S -> aSb", "S -> ε"])

# Describir las gramáticas
for grammar in [regular_grammar, context_free_grammar, context_sensitive_grammar, recursively_enumerable_grammar]:
    grammar.describe()
    print()
