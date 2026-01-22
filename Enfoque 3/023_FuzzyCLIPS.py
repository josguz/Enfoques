
class FuzzyCLIPS:
    def __init__(self):
        self.facts = {}
        self.rules = []

    def add_fact(self, key, value):
        self.facts[key] = value

    def add_rule(self, condition, conclusion):
        self.rules.append((condition, conclusion))

    def evaluate(self):
        for condition, conclusion in self.rules:
            if condition(self.facts):
                print("Conclusión:", conclusion(self.facts))

# Crear un sistema Fuzzy CLIPS
fuzzy_clips = FuzzyCLIPS()
fuzzy_clips.add_fact("temperatura", 28)  # Temperatura en grados Celsius

# Función de condición para las reglas
def hot_condition(facts):
    return facts.get("temperatura", 0) > 25

# Función de conclusión para las reglas
def fan_speed_conclusion(facts):
    return "Encender ventilador al máximo."

# Agregar reglas
fuzzy_clips.add_rule(hot_condition, fan_speed_conclusion)

# Evaluar las reglas
fuzzy_clips.evaluate()
