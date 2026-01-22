
class UncertaintyFactor:
    def __init__(self):
        self.factors = {}

    def add_factor(self, event, certainty):
        self.factors[event] = certainty

    def evaluate_certainty(self, event):
        return self.factors.get(event, "No hay información sobre este evento.")

# Crear un sistema de factores de certeza
uncertainty_system = UncertaintyFactor()
uncertainty_system.add_factor("Lloverá mañana", 0.8)  # 80% de certeza
uncertainty_system.add_factor("Hará sol", 0.2)         # 20% de certeza

# Evaluar certeza de eventos
print("Certeza de que lloverá mañana:", uncertainty_system.evaluate_certainty("Lloverá mañana"))
print("Certeza de que hará sol:", uncertainty_system.evaluate_certainty("Hará sol"))
print("Certeza de que habrá nieve:", uncertainty_system.evaluate_certainty("Habrá nieve"))  # Sin información
