
class NonMonotonicLogic:
    def __init__(self):
        self.knowledge_base = {}
    
    def add_rule(self, condition, conclusion):
        self.knowledge_base[condition] = conclusion

    def query(self, condition):
        if condition in self.knowledge_base:
            return self.knowledge_base[condition]
        else:
            return "No hay conclusión."

# Crear un sistema de lógica no monotónica
logic_system = NonMonotonicLogic()
logic_system.add_rule("Está lloviendo", "Lleva paraguas.")
logic_system.add_rule("Es de día", "No lleva paraguas.")

# Consultar conclusiones
print("Consulta: ¿Qué hacer si está lloviendo?", logic_system.query("Está lloviendo"))
print("Consulta: ¿Qué hacer si es de día?", logic_system.query("Es de día"))

# Cambio en la base de conocimiento
logic_system.add_rule("Es de día", "Lleva sombrero.")  # Cambiamos la conclusión
print("Consulta después del cambio:", logic_system.query("Es de día"))
