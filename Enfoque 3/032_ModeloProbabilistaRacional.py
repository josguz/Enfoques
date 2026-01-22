
import numpy as np

# Definir un modelo probabilista simple
class ProbabilisticModel:
    def __init__(self):
        self.probabilities = {}

    def add_probability(self, event, probability):
        self.probabilities[event] = probability

    def get_probability(self, event):
        return self.probabilities.get(event, "Evento no encontrado.")

# Crear un modelo probabilista
model = ProbabilisticModel()
model.add_probability("Lloverá mañana", 0.8)
model.add_probability("Hará sol", 0.2)

# Consultar probabilidades
print("Probabilidad de que llueva mañana:", model.get_probability("Lloverá mañana"))
print("Probabilidad de que haga sol:", model.get_probability("Hará sol"))
print("Probabilidad de que haya nieve:", model.get_probability("Habrá nieve"))  # Sin información
