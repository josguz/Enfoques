
class DefaultReasoning:
    def __init__(self):
        self.facts = {}
        self.default_rules = {}

    def add_fact(self, key, value):
        self.facts[key] = value

    def add_default_rule(self, condition, conclusion):
        self.default_rules[condition] = conclusion

    def query(self, key):
        # Verificar hechos
        if key in self.facts:
            return self.facts[key]

        # Aplicar reglas por defecto
        for condition, conclusion in self.default_rules.items():
            if condition in self.facts:
                return conclusion
        return "No hay conclusión."

# Crear un sistema de razonamiento
default_reasoning = DefaultReasoning()
default_reasoning.add_fact("Está lloviendo", True)

# Reglas por defecto
default_reasoning.add_default_rule("Está lloviendo", "Usa paraguas.")
default_reasoning.add_default_rule("Está soleado", "Usa gafas de sol.")

# Consultar conclusiones
print("Consulta: ¿Qué hacer si está lloviendo?", default_reasoning.query("Usa paraguas."))
print("Consulta: ¿Está lloviendo?", default_reasoning.query("Está lloviendo"))
