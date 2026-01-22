
class DefaultLogic:
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

# Crear un sistema de lógica por defecto
default_logic = DefaultLogic()
default_logic.add_fact("El cielo es gris", True)

# Reglas por defecto
default_logic.add_default_rule("El cielo es gris", "Puede llover.")

# Consultar conclusiones
print("Consulta: ¿Puede llover?", default_logic.query("Puede llover"))
print("Consulta: ¿El cielo es gris?", default_logic.query("El cielo es gris"))
