
class KnowledgeBase:
    def __init__(self):
        self.facts = {}
    
    def add_fact(self, key, value):
        self.facts[key] = value
    
    def get_fact(self, key):
        return self.facts.get(key, "Hecho no encontrado.")
    
    def show_facts(self):
        for key, value in self.facts.items():
            print(f"{key}: {value}")

# Sistema experto simple
class ExpertSystem:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
    
    def diagnose(self, symptom):
        if symptom in self.kb.facts:
            return f"Diagnóstico: {self.kb.get_fact(symptom)}"
        else:
            return "No se puede hacer un diagnóstico."

# Crear una base de conocimiento
kb = KnowledgeBase()
kb.add_fact("Fiebre", "Puede ser un signo de infección.")
kb.add_fact("Tos", "Puede ser un signo de resfriado o gripe.")

# Crear un sistema experto
expert_system = ExpertSystem(kb)

# Realizar un diagnóstico
symptom = "Fiebre"
print(expert_system.diagnose(symptom))
