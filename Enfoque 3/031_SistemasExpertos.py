
class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = {}

    def add_rule(self, condition, conclusion):
        self.rules.append((condition, conclusion))

    def add_fact(self, key, value):
        self.facts[key] = value

    def evaluate(self):
        for condition, conclusion in self.rules:
            if condition(self.facts):
                print("Conclusión:", conclusion(self.facts))

# Crear un sistema experto
expert_system = ExpertSystem()
expert_system.add_fact("fiebre", True)
expert_system.add_fact("tos", False)

# Definir reglas
def fever_condition(facts):
    return facts.get("fiebre", False)

def cough_condition(facts):
    return facts.get("tos", False)

def conclusion(facts):
    if facts["fiebre"] and facts["tos"]:
        return "Puede tener gripe."
    elif facts["fiebre"]:
        return "Puede tener fiebre."
    return "No hay diagnóstico claro."

# Agregar reglas
expert_system.add_rule(fever_condition, conclusion)
expert_system.add_rule(cough_condition, conclusion)

# Evaluar el sistema experto
expert_system.evaluate()
