
class DiagnosticSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, conclusion):
        self.rules.append((condition, conclusion))

    def diagnose(self, facts):
        conclusions = []
        for condition, conclusion in self.rules:
            if condition(facts):
                conclusions.append(conclusion)
        return conclusions

# Definir las reglas
def condition_fever(facts):
    return facts.get("temperature") > 37.5

def condition_cough(facts):
    return facts.get("cough", False)

# Crear el sistema de diagnóstico y agregar reglas
diagnostic_system = DiagnosticSystem()
diagnostic_system.add_rule(condition_fever, "Puede tener fiebre")
diagnostic_system.add_rule(condition_cough, "Puede tener un resfriado")

# Definir hechos para el diagnóstico
facts = {
    "temperature": 38.0,
    "cough": True
}

# Realizar diagnóstico
diagnosis = diagnostic_system.diagnose(facts)
print("Diagnóstico:", diagnosis)
