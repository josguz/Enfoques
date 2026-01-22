
class Hypothesis:
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy

    def __repr__(self):
        return f"{self.name} (Precisión: {self.accuracy:.2f})"

class HypothesisManager:
    def __init__(self):
        self.hypotheses = []

    def add_hypothesis(self, hypothesis):
        self.hypotheses.append(hypothesis)

    def best_hypothesis(self):
        return max(self.hypotheses, key=lambda h: h.accuracy, default=None)

# Crear un gestor de hipótesis
manager = HypothesisManager()
manager.add_hypothesis(Hypothesis("Hipótesis A", 0.85))
manager.add_hypothesis(Hypothesis("Hipótesis B", 0.90))
manager.add_hypothesis(Hypothesis("Hipótesis C", 0.80))
# Obtener la mejor hipótesis actual
best = manager.best_hypothesis()
print("La mejor hipótesis actual:", best)
