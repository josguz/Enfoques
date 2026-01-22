
# Clase para representar una base de conocimiento
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

# Ejemplo de uso
kb = KnowledgeBase()
kb.add_fact("El cielo es azul", True)
kb.add_fact("La tierra es plana", False)

print("Hechos en la base de conocimiento:")
kb.show_facts()

# Recuperar un hecho específico
print("\nVerificando un hecho:")
print(kb.get_fact("El cielo es azul"))
