
class KnowledgeBase:
    def __init__(self):
        self.rules = []

    def add_rule(self, premise, conclusion):
        self.rules.append((premise, conclusion))

    def forward_chaining(self, facts):
        inferred = set(facts)
        while True:
            new_inferences = set()
            for premise, conclusion in self.rules:
                if premise.issubset(inferred) and conclusion not in inferred:
                    new_inferences.add(conclusion)
            if not new_inferences:
                break
            inferred.update(new_inferences)
        return inferred

    def backward_chaining(self, query, facts):
        if query in facts:
            return True
        for premise, conclusion in self.rules:
            if conclusion == query:
                if self.backward_chaining(premise, facts):
                    return True
        return False

# Crear la base de conocimiento
kb = KnowledgeBase()
kb.add_rule({"A", "B"}, "C")  # Si A y B, entonces C
kb.add_rule({"C"}, "D")        # Si C, entonces D

# Hechos iniciales
facts = {"A", "B"}

# Realizar inferencia hacia adelante
inferred_facts = kb.forward_chaining(facts)
print("Hechos inferidos (hacia adelante):", inferred_facts)

# Realizar inferencia hacia atrás
query = "D"
is_provable = kb.backward_chaining(query, facts)
print(f"¿Se puede inferir '{query}' (hacia atrás)?", is_provable)
